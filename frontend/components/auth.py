import streamlit as st

# ── Dummy credentials ─────────────────────────────────────────────────────────
USERS = {
    "admin": {"password": "chef123", "role": "admin",  "name": "Chef Admin"},
    "maria": {"password": "cocina1", "role": "user",   "name": "María García"},
    "juan":  {"password": "receta1", "role": "user",   "name": "Juan Pérez"},
}


def show_login():
    st.markdown("""
    <div class="bg-orb orb-1"></div>
    <div class="bg-orb orb-2"></div>
    """, unsafe_allow_html=True)

    # Centered container
    col_l, col_c, col_r = st.columns([1, 1.6, 1])
    with col_c:
        # Logo area
        st.markdown("""
        <div style="text-align:center; padding: 3rem 0 2rem;">
            <div style="font-size:3rem; margin-bottom:0.5rem;">🍽️</div>
            <div style="font-family:'Playfair Display',serif; font-size:2.4rem;
                        font-weight:700; color:var(--cocoa); letter-spacing:-0.02em;">
                Chef<span style="color:var(--amber);">Vision</span>
            </div>
            <div style="font-family:'DM Sans',sans-serif; color:var(--espresso);
                        opacity:0.65; font-size:0.95rem; margin-top:0.4rem; font-style:italic;">
                Tu asistente culinario inteligente
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Card open
        st.markdown('<div class="cv-login-card">', unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-bottom:1.5rem;">
            <h2 style="font-family:'Playfair Display',serif; font-size:1.45rem;
                       margin:0 0 0.3rem; color:var(--cocoa);">Bienvenido de vuelta</h2>
            <p style="font-size:0.88rem; color:var(--espresso); opacity:0.7; margin:0;">
                Ingresa tus credenciales para continuar
            </p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input("Usuario", placeholder="tu_usuario", label_visibility="collapsed",
                                  key="login_user")
        st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
        password = st.text_input("Contraseña", type="password", placeholder="••••••••",
                                  label_visibility="collapsed", key="login_pass")

        st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)

        login_clicked = st.button("Iniciar sesión →", use_container_width=True)

        if login_clicked:
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.authenticated = True
                st.session_state.role = USERS[username]["role"]
                st.session_state.username = USERS[username]["name"]
                st.rerun()
            else:
                st.markdown("""
                <div class="cv-warn" style="margin-top:1rem;">
                    ⚠️ Usuario o contraseña incorrectos. Intenta de nuevo.
                </div>
                """, unsafe_allow_html=True)

        # Demo credentials hint
        st.markdown("""
        <div class="cv-divider" style="margin-top:1.5rem;">cuentas de demo</div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.8rem;">
            <div class="cv-card" style="padding:0.7rem 0.9rem; margin:0;">
                <div style="font-weight:600; color:var(--amber);">👑 Admin</div>
                <div style="opacity:0.7;">admin / chef123</div>
            </div>
            <div class="cv-card" style="padding:0.7rem 0.9rem; margin:0;">
                <div style="font-weight:600; color:var(--sage);">👤 Usuario</div>
                <div style="opacity:0.7;">maria / cocina1</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # close cv-login-card

        st.markdown("""
        <div style="text-align:center; margin-top:2rem; font-size:0.78rem;
                    color:var(--espresso); opacity:0.5;">
            © 2025 ChefVision · Todos los derechos reservados
        </div>
        """, unsafe_allow_html=True)
