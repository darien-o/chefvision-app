"""Semantic search service for querying recipe chunks in ChromaDB."""

from __future__ import annotations

import logging
import random

from backend.config import settings
from backend.model.schema import SearchResult
from backend.services.vector_store import _get_collection

logger = logging.getLogger(__name__)


def search_recipes(
    query_terms: list[str],
    top_k: int | None = None,
    min_relevance: float | None = None,
) -> list[SearchResult]:
    """Search ChromaDB for recipe chunks matching the given query terms.

    Fetches more results than needed, then randomly samples from the top
    candidates to add variety across requests.

    Args:
        query_terms: List of ingredient names (translated) to search for.
        top_k: Maximum number of results to return. Defaults to settings.TOP_K.
        min_relevance: Minimum relevance score threshold. Defaults to settings.MIN_RELEVANCE_SCORE.

    Returns:
        A list of SearchResult ordered by relevance score (descending),
        filtered by min_relevance and limited to top_k entries.
    """
    if not query_terms:
        return []

    if top_k is None:
        top_k = settings.TOP_K
    if min_relevance is None:
        min_relevance = settings.MIN_RELEVANCE_SCORE

    query_string = f"receta con {', '.join(query_terms)}"

    # Fetch extra candidates so we can shuffle and still return top_k
    fetch_k = min(top_k * 3, 60)

    collection = _get_collection()
    results = collection.query(
        query_texts=[query_string],
        n_results=fetch_k,
    )

    search_results: list[SearchResult] = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for doc, metadata, distance in zip(documents, metadatas, distances):
        relevance_score = 1.0 / (1.0 + distance)

        if relevance_score < min_relevance:
            continue

        search_results.append(
            SearchResult(
                text=doc,
                source_filename=metadata.get("source_filename", ""),
                page_number=metadata.get("page_number", 0),
                chunk_index=metadata.get("chunk_index", 0),
                relevance_score=relevance_score,
            )
        )

    # Shuffle among candidates to add variety, then sort by relevance
    if len(search_results) > top_k:
        # Keep top 3 always, shuffle the rest and pick from them
        top_fixed = search_results[:3]
        rest = search_results[3:]
        random.shuffle(rest)
        search_results = top_fixed + rest

    search_results = search_results[:top_k]
    search_results.sort(key=lambda r: r.relevance_score, reverse=True)

    return search_results
