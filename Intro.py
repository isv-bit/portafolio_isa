import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(
    page_title="Portfolio IA",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado con colores vibrantes
st.markdown("""
<style>
    /* Variables de color */
    :root {
        --lime: #ADFF2F;
        --butter: #FFD700;
        --magenta: #FF1493;
        --violet: #9D4EDD;
        --primary: #667eea;
        --secondary: #764ba2;
    }

    /* Estilos generales */
    body {
        background: #f5f5f5;
    }

    /* Card base */
    .card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border-top: 6px solid #667eea;
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
    }

    /* Colores de bordes alternados */
    .card-lime { border-left: 6px solid #ADFF2F; border-top: none; }
    .card-butter { border-left: 6px solid #FFD700; border-top: none; }
    .card-magenta { border-left: 6px solid #FF1493; border-top: none; }
    .card-violet { border-left: 6px solid #9D4EDD; border-top: none; }

    /* Header */
    .header-custom {
        text-align: center;
        padding: 20px 0;
        margin-bottom: 30px;
    }

    .header-custom h1 {
        color: #333;
        font-size: 2.5em;
        margin-bottom: 10px;
    }

    .header-custom p {
        color: #666;
        font-size: 1.1em;
    }

    /* Info box */
    .info-box {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ADFF2F;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }

    /* Estadísticas */
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 15px;
    }

    .stat-number {
        font-size: 1.8em;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .stat-label {
        font-size: 0.9em;
        opacity: 0.9;
    }

    /* Badge nuevo */
    .badge-nuevo {
        background: #FF1493;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8em;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* Botón personalizado */
    .btn-custom {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s ease;
        text-decoration: none;
    }

    .btn-custom:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }

    /* Categoría badge */
    .category-badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: 600;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🚀 Portafolio IA")
    st.markdown("### 📊 Estadísticas")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Aplicaciones", "15", "100% Funcionales")
    with col2:
        st.metric("Categorías", "5", "Diferentes")
    
    col3, col4 = st.columns(2)
    with col3:
        st.metric("Disponibilidad", "24/7", "Activo")
    with col4:
        st.metric("Estado", "100%", "Operativo")
    
    st.markdown("---")
    st.markdown("### 📚 Información")
    st.markdown("""
    Las mejores aplicaciones de **Inteligencia Artificial** construidas con **Streamlit**.
    
    Cada aplicación representa diferentes casos de uso de IA desde procesamiento de lenguaje natural hasta visión por computadora.
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 Enlaces")
    st.markdown("[GitHub](https://github.com)")
    st.markdown("[Documentación](https://docs.streamlit.io)")

# ==================== HEADER PRINCIPAL ====================
st.markdown("""
<div class="header-custom">
    <h1>🚀 Portafolio de Inteligencia Artificial</h1>
    <p>Explora las mejores aplicaciones de IA con Streamlit</p>
</div>
""", unsafe_allow_html=True)

# ==================== BÚSQUEDA Y FILTROS ====================
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    search_term = st.text_input("🔍 Buscar aplicaciones...", "")

with col2:
    categoria_filter = st.selectbox(
        "Categoría",
        ["Todos", "Audio", "Visión", "Datos", "NLP"]
    )

with col3:
    sort_by = st.selectbox(
        "Ordenar por",
        ["Recientes", "Populares", "A-Z"]
    )

st.markdown("---")

# ==================== INFO BOX ====================
st.markdown("""
<div class="info-box">
    <h3>📚 Sobre este Portafolio</h3>
    <p>Este portafolio showcasea las mejores aplicaciones de inteligencia artificial construidas con Streamlit. 
    Cada aplicación representa diferentes casos de uso de IA, desde procesamiento de lenguaje natural hasta 
    visión por computadora y análisis de datos avanzado. Todas las aplicaciones están disponibles 24/7 y son completamente funcionales.</p>
</div>
""", unsafe_allow_html=True)

# ==================== DATOS DE APLICACIONES (15 apps) ====================
aplicaciones = [
    {
        "id": 1,
        "titulo": "Conversión de Texto a Voz",
        "descripcion": "Transforma textos en audio de alta calidad usando IA avanzada",
        "categoria": "Audio",
        "imagen": "txt_to_audio2.png",
        "enlace": "https://imultimod.streamlit.app/",
        "nuevo": True,
        "color": "lime"
    },
    {
        "id": 2,
        "titulo": "Conversión de Voz a Texto",
        "descripcion": "Convierte audio en texto con precisión y en tiempo real",
        "categoria": "Audio",
        "imagen": "OIG8.jpg",
        "enlace": "https://traductorw.streamlit.app/",
        "nuevo": False,
        "color": "butter"
    },
    {
        "id": 3,
        "titulo": "Reconocimiento de Objetos",
        "descripcion": "Detecta y clasifica objetos en imágenes usando YOLO",
        "categoria": "Visión",
        "imagen": "txt_to_audio.png",
        "enlace": "https://yolov5cmc.streamlit.app/",
        "nuevo": False,
        "color": "magenta"
    },
    {
        "id": 4,
        "titulo": "Análisis de Imagen",
        "descripcion": "Análisis visual avanzado con modelos de visión IA",
        "categoria": "Visión",
        "imagen": "OIG4.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/",
        "nuevo": True,
        "color": "violet"
    },
    {
        "id": 5,
        "titulo": "Generación en Contexto (RAG)",
        "descripcion": "Analiza documentos PDF y responde preguntas inteligentes",
        "categoria": "NLP",
        "imagen": "Chat_pdf.png",
        "enlace": "https://chatpdf-cc.streamlit.app/",
        "nuevo": False,
        "color": "lime"
    },
    {
        "id": 6,
        "titulo": "Análisis de Datos",
        "descripcion": "Análisis inteligente de datos con agentes de IA",
        "categoria": "Datos",
        "imagen": "data_analisis.png",
        "enlace": "https://dataagente.streamlit.app/",
        "nuevo": False,
        "color": "butter"
    },
    {
        "id": 7,
        "titulo": "Transcriptor Audio y Video",
        "descripcion": "Transcribe automáticamente audio y video a texto",
        "categoria": "Audio",
        "imagen": "OIG3.jpg",
        "enlace": "https://transcript-whisper.streamlit.app/",
        "nuevo": True,
        "color": "magenta"
    },
    {
        "id": 8,
        "titulo": "Entrenando Modelos",
        "descripcion": "Aprende a entrenar y usar tus propios modelos de IA",
        "categoria": "Datos",
        "imagen": "OIG5.jpg",
        "enlace": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "nuevo": False,
        "color": "violet"
    },
    {
        "id": 9,
        "titulo": "Sistema Ciberfísico",
        "descripcion": "Interacción inteligente con el mundo físico",
        "categoria": "Visión",
        "imagen": "OIG6.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/",
        "nuevo": True,
        "color": "lime"
    },
    {
        "id": 10,
        "titulo": "Procesamiento de NLP",
        "descripcion": "Procesamiento avanzado de lenguaje natural",
        "categoria": "NLP",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "butter"
    },
    {
        "id": 11,
        "titulo": "Síntesis de Audio",
        "descripcion": "Crea audio sintético con voces naturales",
        "categoria": "Audio",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "magenta"
    },
    {
        "id": 12,
        "titulo": "Detección de Anomalías",
        "descripcion": "Identifica patrones anómalos en datos",
        "categoria": "Datos",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "violet"
    },
    {
        "id": 13,
        "titulo": "Segmentación de Imágenes",
        "descripcion": "Segmenta automáticamente elementos en imágenes",
        "categoria": "Visión",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": True,
        "color": "lime"
    },
    {
        "id": 14,
        "titulo": "Análisis Sentimental",
        "descripcion": "Analiza sentimientos en textos y redes sociales",
        "categoria": "NLP",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "butter"
    },
    {
        "id": 15,
        "titulo": "Predicción Temporal",
        "descripcion": "Predice series temporales con modelos avanzados",
        "categoria": "Datos",
        "imagen": "txt_to_audio2.png",
        "enlace": "#",
        "nuevo": False,
        "color": "magenta"
    }
]

# ==================== FILTRADO ====================
apps_filtradas = aplicaciones

# Filtrar por búsqueda
if search_term:
    apps_filtradas = [
        app for app in apps_filtradas 
        if search_term.lower() in app["titulo"].lower() or 
           search_term.lower() in app["descripcion"].lower()
    ]

# Filtrar por categoría
if categoria_filter != "Todos":
    apps_filtradas = [
        app for app in apps_filtradas 
        if app["categoria"] == categoria_filter
    ]

# ==================== MOSTRAR CARDS (GRID 5 COLUMNAS) ====================
color_classes = {
    "lime": "card-lime",
    "butter": "card-butter",
    "magenta": "card-magenta",
    "violet": "card-violet"
}

# Crear grid de 5 columnas para 15 apps (3 filas de 5)
cols = st.columns(5)

for idx, app in enumerate(apps_filtradas):
    with cols[idx % 5]:
        color_class = color_classes.get(app["color"], "card-lime")
        
        # Badge nuevo
        if app["nuevo"]:
            st.markdown('<span class="badge-nuevo">🆕 NUEVO</span>', unsafe_allow_html=True)
        
        # Card
        st.markdown(f"""
        <div class="card {color_class}">
        """, unsafe_allow_html=True)
        
        # Categoría
        st.markdown(f'<span class="category-badge">{app["categoria"]}</span>', unsafe_allow_html=True)
        
        # Título
        st.markdown(f'<h3 style="color: #333; margin-bottom: 8px; font-size: 1.1em; line-height: 1.3;">{app["titulo"]}</h3>', unsafe_allow_html=True)
        
        # Descripción
        st.markdown(f'<p style="color: #666; margin-bottom: 12px; font-size: 0.9em; line-height: 1.4;">{app["descripcion"]}</p>', unsafe_allow_html=True)
        
        # Imagen
        try:
            image = Image.open(app["imagen"])
            st.image(image, use_column_width=True)
        except:
            st.info("📷 Imagen no disponible")
        
        # Botón
        st.markdown(f"""
        <a href="{app['enlace']}" target="_blank" style="text-decoration: none;">
            <button class="btn-custom" style="width: 100%; cursor: pointer; font-size: 0.9em; padding: 9px 16px;">
                🔗 Acceder
            </button>
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #999;">
    <p>© 2024 Portafolio de Inteligencia Artificial | Powered by Streamlit</p>
    <p style="font-size: 0.85em;">Diseñado con ❤️ para exploradores de IA</p>
</div>
""", unsafe_allow_html=True)
