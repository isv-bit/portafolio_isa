import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(
    page_title="Portfolio IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado LIMPIO Y ORDENADO
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        background: #f8f9fa;
    }

    /* Container principal */
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 20px;
    }

    /* Header */
    .header-custom {
        text-align: center;
        padding: 40px 0 30px 0;
    }

    .header-custom h1 {
        color: #1a1a1a;
        font-size: 2.8em;
        margin-bottom: 10px;
        font-weight: 700;
    }

    .header-custom p {
        color: #666;
        font-size: 1.1em;
        font-weight: 300;
    }

    /* Grid de cards */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 24px;
        margin: 40px 0;
    }

    /* Card */
    .card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }

    /* Borde izquierdo coloreado */
    .card-lime { border-left: 5px solid #ADFF2F; }
    .card-butter { border-left: 5px solid #FFD700; }
    .card-magenta { border-left: 5px solid #FF1493; }
    .card-violet { border-left: 5px solid #9D4EDD; }

    /* Imagen */
    .card-image {
        width: 100%;
        height: 140px;
        object-fit: cover;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    /* Contenido */
    .card-content {
        padding: 16px;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    /* Badge */
    .badge-nuevo {
        background: #FF1493;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 0.7em;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 8px;
        width: fit-content;
    }

    /* Categoría */
    .category-badge {
        background: #667eea;
        color: white;
        padding: 4px 10px;
        border-radius: 16px;
        font-size: 0.7em;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
        width: fit-content;
    }

    /* Título */
    .card-title {
        color: #1a1a1a;
        font-size: 1em;
        font-weight: 700;
        margin-bottom: 6px;
        line-height: 1.3;
    }

    /* Descripción */
    .card-description {
        color: #666;
        font-size: 0.85em;
        margin-bottom: 12px;
        flex-grow: 1;
        line-height: 1.4;
    }

    /* Botón */
    .card-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 0.85em;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        display: block;
        text-align: center;
        margin-top: auto;
    }

    .card-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }

    /* Info box */
    .info-box {
        background: white;
        padding: 24px;
        border-radius: 16px;
        border-left: 5px solid #ADFF2F;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin: 30px 0;
    }

    .info-box h3 {
        color: #1a1a1a;
        margin-bottom: 10px;
        font-size: 1.2em;
    }

    .info-box p {
        color: #666;
        line-height: 1.6;
        font-size: 0.95em;
    }

    /* Footer */
    .footer-custom {
        text-align: center;
        padding: 30px 0 40px 0;
        color: #999;
        border-top: 1px solid #e0e0e0;
        margin-top: 40px;
    }

    .footer-custom p {
        font-size: 0.95em;
        margin-bottom: 8px;
    }

    /* Responsive */
    @media (max-width: 1400px) {
        .cards-grid {
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }
    }

    @media (max-width: 1024px) {
        .cards-grid {
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }
    }

    @media (max-width: 768px) {
        .cards-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
        }

        .header-custom h1 {
            font-size: 1.8em;
        }
    }

    @media (max-width: 480px) {
        .cards-grid {
            grid-template-columns: 1fr;
            gap: 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🚀 Portafolio IA")
    st.markdown("### 📊 Estadísticas")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Aplicaciones", "15")
    with col2:
        st.metric("Categorías", "5")
    
    col3, col4 = st.columns(2)
    with col3:
        st.metric("Disponibilidad", "24/7")
    with col4:
        st.metric("Estado", "100%")
    
    st.markdown("---")
    st.markdown("### 📚 Información")
    st.markdown("""
    Las mejores aplicaciones de **Inteligencia Artificial** construidas con **Streamlit**.
    """)

# ==================== HEADER ====================
st.markdown("""
<div class="header-custom">
    <h1>🚀 Portafolio de IA</h1>
    <p>Explora las mejores aplicaciones de Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)

# ==================== BÚSQUEDA Y FILTROS ====================
col1, col2 = st.columns([3, 1])

with col1:
    search_term = st.text_input("🔍 Buscar aplicaciones...", "")

with col2:
    categoria_filter = st.selectbox(
        "Categoría",
        ["Todos", "Audio", "Visión", "Datos", "NLP"]
    )

st.markdown("---")

# ==================== INFO BOX ====================
st.markdown("""
<div class="info-box">
    <h3>📚 Sobre este Portafolio</h3>
    <p>Este portafolio showcasea las mejores aplicaciones de inteligencia artificial construidas con Streamlit. Cada aplicación representa diferentes casos de uso de IA, desde procesamiento de lenguaje natural hasta visión por computadora y análisis de datos avanzado.</p>
</div>
""", unsafe_allow_html=True)

# ==================== DATOS DE 15 APLICACIONES ====================
aplicaciones = [
    {
        "titulo": "Conversión de Texto a Voz",
        "descripcion": "Transforma textos en audio de alta calidad",
        "categoria": "Audio",
        "imagen": "txt_to_audio2.png",
        "enlace": "https://imultimod.streamlit.app/",
        "nuevo": True,
        "color": "lime"
    },
    {
        "titulo": "Conversión de Voz a Texto",
        "descripcion": "Convierte audio en texto con precisión",
        "categoria": "Audio",
        "imagen": "OIG8.jpg",
        "enlace": "https://traductorw.streamlit.app/",
        "nuevo": False,
        "color": "butter"
    },
    {
        "titulo": "Reconocimiento de Objetos",
        "descripcion": "Detecta objetos en imágenes usando YOLO",
        "categoria": "Visión",
        "imagen": "txt_to_audio.png",
        "enlace": "https://yolov5cmc.streamlit.app/",
        "nuevo": False,
        "color": "magenta"
    },
    {
        "titulo": "Análisis de Imagen",
        "descripcion": "Análisis visual avanzado con IA",
        "categoria": "Visión",
        "imagen": "OIG4.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/",
        "nuevo": True,
        "color": "violet"
    },
    {
        "titulo": "Generación en Contexto (RAG)",
        "descripcion": "Analiza PDFs y responde preguntas",
        "categoria": "NLP",
        "imagen": "Chat_pdf.png",
        "enlace": "https://chatpdf-cc.streamlit.app/",
        "nuevo": False,
        "color": "lime"
    },
    {
        "titulo": "Análisis de Datos",
        "descripcion": "Análisis inteligente con agentes IA",
        "categoria": "Datos",
        "imagen": "data_analisis.png",
        "enlace": "https://dataagente.streamlit.app/",
        "nuevo": False,
        "color": "butter"
    },
    {
        "titulo": "Transcriptor Audio y Video",
        "descripcion": "Transcribe automáticamente archivos",
        "categoria": "Audio",
        "imagen": "OIG3.jpg",
        "enlace": "https://transcript-whisper.streamlit.app/",
        "nuevo": True,
        "color": "magenta"
    },
    {
        "titulo": "Entrenando Modelos",
        "descripcion": "Entrena tus propios modelos de IA",
        "categoria": "Datos",
        "imagen": "OIG5.jpg",
        "enlace": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "nuevo": False,
        "color": "violet"
    },
    {
        "titulo": "Sistema Ciberfísico",
        "descripcion": "Interacción física con IA",
        "categoria": "Visión",
        "imagen": "OIG6.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/",
        "nuevo": True,
        "color": "lime"
    },
    {
        "titulo": "Procesamiento NLP",
        "descripcion": "Procesamiento de lenguaje natural",
        "categoria": "NLP",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "butter"
    },
    {
        "titulo": "Síntesis de Audio",
        "descripcion": "Crea audio sintético con voces",
        "categoria": "Audio",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "magenta"
    },
    {
        "titulo": "Detección de Anomalías",
        "descripcion": "Identifica patrones anómalos",
        "categoria": "Datos",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "violet"
    },
    {
        "titulo": "Segmentación de Imágenes",
        "descripcion": "Segmenta elementos en imágenes",
        "categoria": "Visión",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": True,
        "color": "lime"
    },
    {
        "titulo": "Análisis Sentimental",
        "descripcion": "Analiza sentimientos en textos",
        "categoria": "NLP",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "butter"
    },
    {
        "titulo": "Predicción Temporal",
        "descripcion": "Predice series temporales",
        "categoria": "Datos",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "magenta"
    }
]

# ==================== FILTRADO ====================
apps_filtradas = aplicaciones

if search_term:
    apps_filtradas = [
        app for app in apps_filtradas 
        if search_term.lower() in app["titulo"].lower() or 
           search_term.lower() in app["descripcion"].lower()
    ]

if categoria_filter != "Todos":
    apps_filtradas = [
        app for app in apps_filtradas 
        if app["categoria"] == categoria_filter
    ]

# ==================== RENDERIZAR CARDS ====================
color_classes = {
    "lime": "card-lime",
    "butter": "card-butter",
    "magenta": "card-magenta",
    "violet": "card-violet"
}

# HTML de las cards
html_cards = '<div class="cards-grid">'

for app in apps_filtradas:
    color_class = color_classes.get(app["color"], "card-lime")
    
    html_cards += f"""
    <div class="card {color_class}">
        <img src="https://via.placeholder.com/400x140?text={app['titulo']}&bg=667eea&textColor=fff" 
             class="card-image" alt="{app['titulo']}">
        <div class="card-content">
            {'<div class="badge-nuevo">🆕 NUEVO</div>' if app['nuevo'] else ''}
            <div class="category-badge">{app['categoria']}</div>
            <h3 class="card-title">{app['titulo']}</h3>
            <p class="card-description">{app['descripcion']}</p>
            <a href="{app['enlace']}" target="_blank" class="card-button">🔗 Acceder</a>
        </div>
    </div>
    """

html_cards += '</div>'

st.markdown(html_cards, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("""
<div class="footer-custom">
    <p>© 2024 Portafolio de Inteligencia Artificial | Powered by Streamlit</p>
    <p style="font-size: 0.85em;">Diseñado con ❤️ para exploradores de IA</p>
</div>
""", unsafe_allow_html=True)
