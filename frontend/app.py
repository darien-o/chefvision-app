import streamlit as st
from components.auth import show_login
from components.admin import show_admin
from components.user import show_user
from components.styles import inject_styles

# ── App-wide config ──────────────────────────────────────────────
st.set_page_config(
    page_title="ChefVision",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_styles()

# ── Session defaults ─────────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "role" not in st.session_state:
    st.session_state.role = None
if "username" not in st.session_state:
    st.session_state.username = ""

# ── Router ───────────────────────────────────────────────────────
if not st.session_state.authenticated:
    show_login()
elif st.session_state.role == "admin":
    show_admin()
else:
    show_user()
