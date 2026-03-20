import streamlit as st
import base64
import json
import os
from datetime import datetime

UPLOAD_DIR = "data/uploads"
META_FILE  = os.path.join(UPLOAD_DIR, "metadata.json")

MEAL_OPTIONS = {
    "Desayuno": {"emoji": "🌅", "hint": "Energía para empezar el día"},
    "Almuerzo": {"emoji": "☀️", "hint": "El plato fuerte del día"},
    "Cena":     {"emoji": "🌙", "hint": "Ligero y reconfortante"},
}


def load_recipes_count() -> int:
    if os.path.exists(META_FILE):
        with open(META_FILE, "r", encoding="utf-8") as f:
            return len(json.load(f))
    return 0


def image_to_b64(image_file) -> str:
    return base64.b64encode(image_file.read()).decode()


# ── Topbar ────────────────────────────────────────────────────────────────────
def _topbar():
    col_logo, col_space, col_user = st.columns([2, 5, 2])
    with col_logo:
        st.markdown("""
        <div style="padding:1.1rem 0 0.5rem;">
            <span class="cv-logo">Chef<span>Vision</span></span>
        </div>
        """, unsafe_allow_html=True)
    with col_user:
        st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:flex-end;
                    gap:0.6rem; padding-top:1.1rem;">
            <div style="text-align:right;">
                <div style="font-weight:600; font-size:0.88rem; color:var(--cocoa);">
                    {st.session_state.username}
                </div>
                <div style="font-size:0.75rem; color:var(--sage); font-weight:600;">Usuario</div>
            </div>
            <div style="width:36px; height:36px; background:var(--sage); border-radius:50%;
                        display:flex; align-items:center; justify-content:center;
                        color:white; font-size:1.1rem;">👤</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr style="margin:0 0 2rem; border:none; border-top:1px solid var(--mist);">', 
                unsafe_allow_html=True)


# ── Recipe display ────────────────────────────────────────────────────────────
def _show_recipe(meal: str, images_count: int):
    """Placeholder recipe output — replace with real LLM call later."""
    meal_emoji = MEAL_OPTIONS[meal]["emoji"]

    sample_ingredients = [
        "2 huevos frescos", "1 taza de arroz cocido",
        "½ cebolla picada", "2 dientes de ajo",
        "Sal, pimienta y aceite de oliva al gusto",
        "Hierbas frescas (perejil, cilantro)",
    ]
    sample_steps = [
        "Calienta una sartén a fuego medio con un chorrito de aceite de oliva.",
        "Sofríe la cebolla y el ajo hasta que estén transparentes (aprox. 3 min).",
        "Añade los demás ingredientes identificados en tus fotos y mezcla bien.",
        "Cocina a fuego medio-alto por 5–7 minutos revolviendo ocasionalmente.",
        "Ajusta la sazón con sal y pimienta. ¡Sirve caliente y disfruta!",
    ]

    st.markdown(f"""
    <div class="recipe-card">
        <div class="recipe-header">
            <div style="font-size:0.8rem; text-transform:uppercase; letter-spacing:0.12em;
                        opacity:0.65; margin-bottom:0.5rem; font-weight:600;">
                {meal_emoji} Receta para {meal}
            </div>
            <div class="recipe-title">Combinación Creativa del Chef</div>
            <div style="opacity:0.65; font-size:0.9rem; margin-top:0.5rem;">
                Basada en {images_count} foto(s) de tus ingredientes
            </div>
        </div>
        <div class="recipe-body">
            <h4 style="font-family:'DM Sans',sans-serif; font-size:0.8rem; text-transform:uppercase;
                       letter-spacing:0.1em; color:var(--amber); margin:0 0 0.75rem;">
                🧺 Ingredientes identificados
            </h4>
    """, unsafe_allow_html=True)

    for ing in sample_ingredients:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:0.5rem; padding:0.3rem 0;
                    border-bottom:1px solid var(--mist); font-size:0.9rem;">
            <span style="color:var(--amber);">·</span> {ing}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <h4 style="font-family:'DM Sans',sans-serif; font-size:0.8rem; text-transform:uppercase;
                   letter-spacing:0.1em; color:var(--sage); margin:1.5rem 0 0.75rem;">
            👨‍🍳 Preparación paso a paso
        </h4>
    """, unsafe_allow_html=True)

    for i, step in enumerate(sample_steps, 1):
        st.markdown(f"""
        <div style="display:flex; gap:0.9rem; margin-bottom:0.9rem; align-items:flex-start;">
            <div style="min-width:28px; height:28px; background:var(--cocoa); color:var(--cream);
                        border-radius:50%; display:flex; align-items:center; justify-content:center;
                        font-size:0.78rem; font-weight:700; flex-shrink:0;">
                {i}
            </div>
            <div style="font-size:0.9rem; padding-top:0.3rem; line-height:1.5;">{step}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="cv-info" style="margin-top:1rem;">
            💡 <strong>Consejo del chef:</strong> Esta receta es una sugerencia basada en los
            ingredientes detectados. Puedes adaptar las porciones y tiempos a tu gusto.
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Main user view ────────────────────────────────────────────────────────────
def show_user():
    _topbar()

    recipes_available = load_recipes_count()

    # ── Greeting
    hour = datetime.now().hour
    greeting = "Buenos días" if hour < 12 else ("Buenas tardes" if hour < 19 else "Buenas noches")

    st.markdown(f"""
    <div style="margin-bottom:2rem;">
        <h1 style="font-size:2rem; margin:0 0 0.4rem;">
            {greeting}, {st.session_state.username.split()[0]} 👋
        </h1>
        <p style="color:var(--espresso); opacity:0.7; margin:0; font-size:0.95rem;">
            Fotografía tus ingredientes y te sugiero una receta perfecta
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Knowledge base status
    if recipes_available == 0:
        st.markdown("""
        <div class="cv-warn" style="margin-bottom:1.5rem;">
            📚 El administrador aún no ha cargado recetas de referencia. Las sugerencias serán
            genéricas por el momento.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="cv-info" style="margin-bottom:1.5rem;">
            📚 Asistente entrenado con <strong>{recipes_available}</strong>
            libro(s) de recetas · Listo para inspirarte
        </div>
        """, unsafe_allow_html=True)

    # ── STEP 1: Meal type selector
    st.markdown("""
    <div class="cv-card">
        <h3 style="font-size:1.1rem; margin:0 0 0.25rem;">1 · ¿Para qué momento del día?</h3>
        <p style="font-size:0.85rem; color:var(--espresso); opacity:0.65; margin:0 0 1rem;">
            Generar receta para:
        </p>
    """, unsafe_allow_html=True)

    # Initialize meal selection
    if "selected_meal" not in st.session_state:
        st.session_state.selected_meal = "Almuerzo"

    # Meal buttons as columns
    m1, m2, m3 = st.columns(3)
    for col, (meal, info) in zip([m1, m2, m3], MEAL_OPTIONS.items()):
        with col:
            is_active = st.session_state.selected_meal == meal
            border_style = "2px solid var(--amber)" if is_active else "2px solid var(--mist)"
            bg_style = "rgba(212,132,58,0.08)" if is_active else "var(--warm-white)"

            if st.button(
                f"{info['emoji']}\n{meal}",
                key=f"meal_{meal}",
                use_container_width=True,
            ):
                st.session_state.selected_meal = meal
                st.rerun()

            # Visual indicator under each button
            indicator_color = "var(--amber)" if is_active else "transparent"
            st.markdown(f"""
            <div style="height:3px; background:{indicator_color}; border-radius:2px;
                        margin-top:-0.5rem; transition:background 0.2s;"></div>
            <div style="text-align:center; font-size:0.75rem; color:var(--espresso);
                        opacity:0.55; margin-top:0.3rem;">{info['hint']}</div>
            """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="margin-top:1rem; padding:0.6rem 1rem; background:rgba(212,132,58,0.08);
                border-radius:var(--radius-sm); font-size:0.88rem; font-weight:600;
                color:var(--amber);">
        ✓ Seleccionado: {MEAL_OPTIONS[st.session_state.selected_meal]['emoji']} 
        {st.session_state.selected_meal}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── STEP 2: Photo upload
    st.markdown("""
    <div class="cv-card">
        <h3 style="font-size:1.1rem; margin:0 0 0.25rem;">2 · Fotografía tus ingredientes</h3>
        <p style="font-size:0.85rem; color:var(--espresso); opacity:0.65; margin:0 0 1rem;">
            Puedes subir una o varias fotos · Desde cámara o galería
        </p>
    """, unsafe_allow_html=True)

    uploaded_images = st.file_uploader(
        "Sube tus fotos de alimentos",
        type=["jpg", "jpeg", "png", "webp", "heic"],
        accept_multiple_files=True,
        label_visibility="collapsed",
        key="food_photos",
    )

    if uploaded_images:
        # Show image previews in a grid
        st.markdown(f"""
        <div style="font-size:0.82rem; color:var(--espresso); opacity:0.6; 
                    margin:0.5rem 0; font-weight:600; text-transform:uppercase; 
                    letter-spacing:0.06em;">
            {len(uploaded_images)} imagen(es) cargada(s)
        </div>
        """, unsafe_allow_html=True)

        # Preview grid — up to 4 thumbnails
        preview_cols = st.columns(min(len(uploaded_images), 4))
        for i, img in enumerate(uploaded_images[:4]):
            with preview_cols[i]:
                st.image(img, use_container_width=True,
                         caption=f"📷 {img.name[:18]}…" if len(img.name) > 18 else img.name)

        if len(uploaded_images) > 4:
            st.markdown(f"""
            <div style="font-size:0.82rem; color:var(--espresso); opacity:0.55; 
                        text-align:center; margin-top:0.3rem;">
                +{len(uploaded_images)-4} imagen(es) adicional(es)
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align:center; padding:1.5rem 0; color:var(--espresso); opacity:0.45;">
            <div style="font-size:2.5rem; margin-bottom:0.5rem;">📷</div>
            <div style="font-size:0.88rem;">
                Toca aquí para seleccionar fotos<br>
                <span style="font-size:0.78rem; opacity:0.7;">
                    Compatible con cámara del celular
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── STEP 3: Generate
    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)

    can_generate = bool(uploaded_images)

    if not can_generate:
        st.markdown("""
        <div style="text-align:center; padding:0.5rem 0;">
        """, unsafe_allow_html=True)

    col_gen, col_clear = st.columns([3, 1])
    with col_gen:
        meal_emoji = MEAL_OPTIONS[st.session_state.selected_meal]["emoji"]
        generate_clicked = st.button(
            f"{meal_emoji} Generar receta para {st.session_state.selected_meal}",
            use_container_width=True,
            disabled=not can_generate,
        )

    with col_clear:
        if st.button("🔄 Reiniciar", use_container_width=True):
            for k in list(st.session_state.keys()):
                if k.startswith("food_") or k == "recipe_generated":
                    del st.session_state[k]
            st.rerun()

    if not can_generate:
        st.markdown("""
        <div style="text-align:center; font-size:0.82rem; color:var(--espresso);
                    opacity:0.5; margin-top:0.5rem;">
            Sube al menos una foto para habilitar la generación
        </div>
        """, unsafe_allow_html=True)

    # ── Recipe output
    if generate_clicked and uploaded_images:
        with st.spinner("Analizando ingredientes y creando tu receta…"):
            import time
            time.sleep(1.5)  # Simulate processing — replace with real API call

        st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)
        st.markdown('<h3 style="font-size:1.1rem; margin:0 0 1rem;">🍽️ Tu receta personalizada</h3>',
                    unsafe_allow_html=True)
        _show_recipe(st.session_state.selected_meal, len(uploaded_images))

        # Tags
        st.markdown("""
        <div style="margin-top:1rem; display:flex; flex-wrap:wrap; gap:0.4rem;">
            <span class="cv-chip cv-chip-amber">⏱ 20–30 min</span>
            <span class="cv-chip cv-chip-sage">🥗 Saludable</span>
            <span class="cv-chip cv-chip-terra">🌶 Moderado</span>
            <span class="cv-chip">👥 2 porciones</span>
        </div>
        """, unsafe_allow_html=True)

    # ── Logout
    st.markdown('<div style="height:2.5rem"></div>', unsafe_allow_html=True)
    col_lx, _ = st.columns([1, 4])
    with col_lx:
        if st.button("← Cerrar sesión", use_container_width=True):
            for k in ["authenticated", "role", "username"]:
                st.session_state[k] = None if k == "role" else (
                    False if k == "authenticated" else "")
            st.rerun()
