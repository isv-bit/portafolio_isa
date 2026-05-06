import streamlit as st

# =====================================================
# CONFIGURACIÓN DE PÁGINA
# =====================================================
st.set_page_config(
    page_title="Portfolio IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# ESTILOS (CSS)
# =====================================================
def load_css():
    st.markdown("""
    <style>
    /* RESET */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        background: #f8f9fa;
    }

    /* HEADER */
    .header-custom {
        text-align: center;
        padding: 40px 0 30px;
    }

    .header-custom h1 {
        font-size: 2.8em;
        font-weight: 700;
        color: #1a1a1a;
    }

    .header-custom p {
        font-size: 1.1em;
        color: #666;
    }

    /* GRID */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 24px;
        margin: 40px 0;
    }

    /* CARD */
    .card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: 0.3s;
        display: flex;
        flex-direction: column;
    }

    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }

    .card-image {
        width: 100%;
        height: 140px;
        object-fit: cover;
    }

    .card-content {
        padding: 16px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    /* BADGES */
    .badge-nuevo {
        background: #FF1493;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.7em;
        font-weight: 700;
        margin-bottom: 8px;
        width: fit-content;
    }

    .category-badge {
        background: #667eea;
        color: white;
        padding: 4px 10px;
        border-radius: 16px;
        font-size: 0.7em;
        margin-bottom: 8px;
        width: fit-content;
    }

    /* TEXTO */
    .card-title {
        font-size: 1em;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .card-description {
        font-size: 0.85em;
        color: #666;
        margin-bottom: 12px;
        flex-grow: 1;
    }

    /* BOTÓN */
    .card-button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        text-decoration: none;
        font-size: 0.85em;
        font-weight: 600;
    }

    /* COLORES */
    .card-lime { border-left: 5px solid #ADFF2F; }
    .card-butter { border-left: 5px solid #FFD700; }
    .card-magenta { border-left: 5px solid #FF1493; }
    .card-violet { border-left: 5px solid #9D4EDD; }

    /* INFO BOX */
    .info-box {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border-left: 5px solid #ADFF2F;
        margin: 30px 0;
    }

    /* FOOTER */
    .footer-custom {
        text-align: center;
        margin-top: 40px;
        padding: 30px 0;
        color: #999;
        border-top: 1px solid #e0e0e0;
    }

    /* RESPONSIVE */
    @media (max-width: 1024px) {
        .cards-grid { grid-template-columns: repeat(3, 1fr); }
    }

    @media (max-width: 768px) {
        .cards-grid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 480px) {
        .cards-grid { grid-template-columns: 1fr; }
    }
    </style>
    """, unsafe_allow_html=True)

load_css()

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.title("🚀 Portafolio IA")

    st.subheader("📊 Estadísticas")
    col1, col2 = st.columns(2)
    col1.metric("Apps", "15")
    col2.metric("Categorías", "5")

    col3, col4 = st.columns(2)
    col3.metric("Disponibilidad", "24/7")
    col4.metric("Estado", "100%")

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<div class="header-custom">
    <h1>🚀 Portafolio de IA</h1>
    <p>Explora aplicaciones de Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# FILTROS
# =====================================================
col1, col2 = st.columns([3, 1])

search_term = col1.text_input("🔍 Buscar...")
categoria_filter = col2.selectbox("Categoría", ["Todos", "Audio", "Visión", "Datos", "NLP"])

# =====================================================
# DATA
# =====================================================
aplicaciones = [
    {"titulo": "Texto a Voz", "descripcion": "Convierte texto en audio", "categoria": "Audio", "enlace": "#", "nuevo": True, "color": "lime"},
    {"titulo": "Voz a Texto", "descripcion": "Transcribe audio", "categoria": "Audio", "enlace": "#", "nuevo": False, "color": "butter"},
    {"titulo": "YOLO Objetos", "descripcion": "Detecta objetos", "categoria": "Visión", "enlace": "#", "nuevo": False, "color": "magenta"},
]

# =====================================================
# FILTRADO
# =====================================================
apps_filtradas = [
    app for app in aplicaciones
    if (search_term.lower() in app["titulo"].lower() or search_term.lower() in app["descripcion"].lower())
]

if categoria_filter != "Todos":
    apps_filtradas = [app for app in apps_filtradas if app["categoria"] == categoria_filter]

# =====================================================
# RENDER CARDS
# =====================================================
color_classes = {
    "lime": "card-lime",
    "butter": "card-butter",
    "magenta": "card-magenta",
    "violet": "card-violet"
}

html = '<div class="cards-grid">'

for app in apps_filtradas:
    html += f"""
    <div class="card {color_classes.get(app['color'], 'card-lime')}">
        <img src="https://via.placeholder.com/400x140" class="card-image">
        <div class="card-content">
            {"<div class='badge-nuevo'>🆕 NUEVO</div>" if app["nuevo"] else ""}
            <div class="category-badge">{app["categoria"]}</div>
            <h3 class="card-title">{app["titulo"]}</h3>
            <p class="card-description">{app["descripcion"]}</p>
            <a href="{app["enlace"]}" class="card-button">Ver</a>
        </div>
    </div>
    """

html += "</div>"
st.markdown(html, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<div class="footer-custom">
    <p>© 2024 Portafolio IA</p>
</div>
""", unsafe_allow_html=True)
