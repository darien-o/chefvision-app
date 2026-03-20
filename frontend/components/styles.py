import streamlit as st

def inject_styles():
    st.markdown("""
    <style>
    /* ── Google Fonts ─────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,500&family=DM+Sans:wght@300;400;500;600&display=swap');

    /* ── CSS Variables ────────────────────────────────────── */
    :root {
        --cream:      #FAF6F0;
        --warm-white: #FFF9F2;
        --cocoa:      #2C1A0E;
        --espresso:   #4A2C1A;
        --amber:      #D4843A;
        --amber-light:#F0A857;
        --sage:       #6B8F71;
        --terracotta: #C4614A;
        --mist:       #E8DDD4;
        --shadow:     rgba(44,26,14,0.12);
        --radius-lg:  20px;
        --radius-md:  12px;
        --radius-sm:  8px;
    }

    /* ── Global Reset ────────────────────────────────────── */
    html, body, [data-testid="stAppViewContainer"] {
        background: var(--cream) !important;
        font-family: 'DM Sans', sans-serif !important;
        color: var(--cocoa) !important;
    }

    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    #MainMenu, footer { display: none !important; }

    [data-testid="stAppViewContainer"] > div:first-child {
        padding-top: 0 !important;
    }

    /* ── Hide sidebar toggle ─────────────────────────────── */
    [data-testid="collapsedControl"] { display: none !important; }

    /* ── Scrollbar ───────────────────────────────────────── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--cream); }
    ::-webkit-scrollbar-thumb { background: var(--mist); border-radius: 3px; }

    /* ── Buttons ─────────────────────────────────────────── */
    .stButton > button {
        background: var(--cocoa) !important;
        color: var(--cream) !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0.65rem 1.8rem !important;
        transition: all 0.25s ease !important;
        letter-spacing: 0.02em !important;
        cursor: pointer !important;
    }
    .stButton > button:hover {
        background: var(--espresso) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px var(--shadow) !important;
    }
    .stButton > button:active { transform: translateY(0) !important; }

    .btn-amber > button {
        background: var(--amber) !important;
    }
    .btn-amber > button:hover {
        background: var(--amber-light) !important;
    }

    .btn-outline > button {
        background: transparent !important;
        color: var(--cocoa) !important;
        border: 2px solid var(--mist) !important;
    }
    .btn-outline > button:hover {
        border-color: var(--cocoa) !important;
        background: var(--mist) !important;
    }

    /* ── Inputs ──────────────────────────────────────────── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--warm-white) !important;
        border: 1.5px solid var(--mist) !important;
        border-radius: var(--radius-md) !important;
        font-family: 'DM Sans', sans-serif !important;
        color: var(--cocoa) !important;
        padding: 0.65rem 1rem !important;
        transition: border 0.2s ease !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--amber) !important;
        box-shadow: 0 0 0 3px rgba(212,132,58,0.15) !important;
    }

    /* ── File uploader ───────────────────────────────────── */
    [data-testid="stFileUploader"] {
        background: var(--warm-white) !important;
        border: 2px dashed var(--mist) !important;
        border-radius: var(--radius-lg) !important;
        padding: 1.5rem !important;
        transition: border-color 0.2s ease !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--amber) !important;
    }

    /* ── Radio / Segmented control ───────────────────────── */
    .stRadio > div {
        gap: 0.5rem !important;
    }
    .stRadio > div > label {
        background: var(--warm-white) !important;
        border: 1.5px solid var(--mist) !important;
        border-radius: var(--radius-md) !important;
        padding: 0.5rem 1.2rem !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        font-family: 'DM Sans', sans-serif !important;
    }
    .stRadio > div > label:has(input:checked) {
        background: var(--cocoa) !important;
        border-color: var(--cocoa) !important;
        color: var(--cream) !important;
    }

    /* ── Cards ───────────────────────────────────────────── */
    .cv-card {
        background: var(--warm-white);
        border-radius: var(--radius-lg);
        padding: 1.75rem;
        box-shadow: 0 2px 16px var(--shadow);
        margin-bottom: 1.25rem;
        transition: box-shadow 0.25s ease;
    }
    .cv-card:hover { box-shadow: 0 6px 28px var(--shadow); }

    /* ── Topbar ──────────────────────────────────────────── */
    .cv-topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.2rem 2rem;
        background: var(--warm-white);
        border-bottom: 1px solid var(--mist);
        margin-bottom: 2rem;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .cv-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--cocoa);
        letter-spacing: -0.02em;
    }
    .cv-logo span { color: var(--amber); }

    /* ── Hero / Login ────────────────────────────────────── */
    .cv-hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(145deg, var(--cream) 0%, #F5E6D3 50%, var(--cream) 100%);
        position: relative;
        overflow: hidden;
    }

    .cv-login-card {
        background: var(--warm-white);
        border-radius: 28px;
        padding: 3rem 2.5rem;
        box-shadow: 0 20px 60px rgba(44,26,14,0.18);
        width: 100%;
        max-width: 420px;
        position: relative;
        z-index: 2;
    }

    /* ── Tags / Chips ────────────────────────────────────── */
    .cv-chip {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: var(--mist);
        color: var(--espresso);
        padding: 0.3rem 0.8rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    .cv-chip-amber { background: rgba(212,132,58,0.15); color: var(--amber); }
    .cv-chip-sage  { background: rgba(107,143,113,0.15); color: var(--sage); }
    .cv-chip-terra { background: rgba(196,97,74,0.15); color: var(--terracotta); }

    /* ── Progress / stats ────────────────────────────────── */
    .cv-stat {
        text-align: center;
        padding: 1rem;
    }
    .cv-stat-num {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--amber);
        line-height: 1;
    }
    .cv-stat-label {
        font-size: 0.8rem;
        font-weight: 500;
        color: var(--espresso);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0.3rem;
    }

    /* ── Meal selector ───────────────────────────────────── */
    .meal-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        margin: 1rem 0;
    }
    .meal-btn {
        background: var(--warm-white);
        border: 2px solid var(--mist);
        border-radius: var(--radius-lg);
        padding: 1.2rem 0.8rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s ease;
        font-family: 'DM Sans', sans-serif;
    }
    .meal-btn:hover, .meal-btn.active {
        border-color: var(--amber);
        background: rgba(212,132,58,0.08);
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(212,132,58,0.2);
    }
    .meal-btn .meal-emoji { font-size: 2rem; display: block; margin-bottom: 0.4rem; }
    .meal-btn .meal-label { font-size: 0.9rem; font-weight: 600; color: var(--cocoa); }

    /* ── Divider ─────────────────────────────────────────── */
    .cv-divider {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin: 1.5rem 0;
        color: var(--espresso);
        opacity: 0.5;
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    .cv-divider::before, .cv-divider::after {
        content: '';
        flex: 1;
        height: 1px;
        background: var(--mist);
    }

    /* ── Alert / info boxes ──────────────────────────────── */
    .cv-info {
        background: rgba(107,143,113,0.12);
        border-left: 3px solid var(--sage);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 0.9rem 1.2rem;
        font-size: 0.88rem;
        margin: 0.75rem 0;
    }
    .cv-warn {
        background: rgba(212,132,58,0.12);
        border-left: 3px solid var(--amber);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 0.9rem 1.2rem;
        font-size: 0.88rem;
        margin: 0.75rem 0;
    }

    /* ── Recipe output ───────────────────────────────────── */
    .recipe-card {
        background: var(--warm-white);
        border-radius: var(--radius-lg);
        border: 1px solid var(--mist);
        overflow: hidden;
    }
    .recipe-header {
        background: linear-gradient(135deg, var(--espresso) 0%, var(--cocoa) 100%);
        padding: 2rem;
        color: var(--cream);
    }
    .recipe-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        color: var(--cream);
    }
    .recipe-body { padding: 1.75rem; }

    /* ── Responsive ──────────────────────────────────────── */
    @media (max-width: 768px) {
        .cv-login-card { padding: 2rem 1.5rem; margin: 1rem; }
        .cv-topbar { padding: 1rem; }
        .cv-logo { font-size: 1.3rem; }
        .meal-grid { grid-template-columns: repeat(3, 1fr); gap: 0.6rem; }
        .cv-card { padding: 1.25rem; }
        .recipe-header { padding: 1.5rem; }
        .recipe-title { font-size: 1.3rem; }
        [data-testid="column"] { min-width: 0; }
    }

    /* ── Streamlit overrides ─────────────────────────────── */
    [data-testid="stVerticalBlock"] { gap: 0 !important; }
    .block-container {
        max-width: 900px !important;
        padding: 0 1rem 3rem !important;
        margin: 0 auto !important;
    }
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: var(--cocoa) !important;
    }
    .stSelectbox > div > div {
        background: var(--warm-white) !important;
        border: 1.5px solid var(--mist) !important;
        border-radius: var(--radius-md) !important;
    }
    [data-baseweb="notification"] { display: none; }

    /* ── Floating orbs decoration ────────────────────────── */
    .bg-orb {
        position: fixed;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.35;
        pointer-events: none;
        z-index: 0;
    }
    .orb-1 {
        width: 400px; height: 400px;
        background: var(--amber-light);
        top: -100px; right: -100px;
    }
    .orb-2 {
        width: 300px; height: 300px;
        background: var(--sage);
        bottom: -80px; left: -80px;
    }
    </style>
    """, unsafe_allow_html=True)
