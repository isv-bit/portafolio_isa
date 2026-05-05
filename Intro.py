import streamlit as st
from PIL import Image
import base64

# Configuración de página
st.set_page_config(
    page_title="Portfolio IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para diseño colorido
st.markdown("""
<style>
    /* Colores principales */
    :root {
        --primary: #6C5CE7;
        --secondary: #00B894;
        --accent: #FF6B6B;
        --warning: #FDCB6E;
        --info: #74B9FF;
    }
    
    /* Estilos generales */
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main {
        background-color: #f8f9fa;
    }
    
    /* Tarjetas de aplicaciones */
    .app-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        color: white;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 20px;
        border-left: 5px solid #00B894;
    }
    
    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    
    .app-card-title {
        font-size: 1.4em;
        font-weight: bold;
        margin-bottom: 10px;
        color: #FFD700;
    }
    
    .app-card-text {
        font-size: 0.95em;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .app-card-link {
        display: inline-block;
        background-color: #00B894;
        color: white;
        padding: 8px 16px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    
    .app-card-link:hover {
        background-color: #FF6B6B;
    }
    
    /* Encabezado */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }
    
    .header-container h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Sidebar */
    .sidebar-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
    }
    
    /* Columnas con gradientes diferentes */
    .col-gradient-1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .col-gradient-2 {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .col-gradient-3 {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar mejorado
with st.sidebar:
    st.markdown("### 🤖 Sobre la IA")
    
    parrafo = (
        "La **Inteligencia Artificial** permite mejorar la toma de decisiones con datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, "
        "resultando en mayor eficiencia y precisión."
    )
    st.info(parrafo)
    
    st.markdown("---")
    st.markdown("### 📚 Recursos")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f"**[📖 Accede a más ejercicios y recursos]({url_ia})**")
    
    st.markdown("---")
    st.markdown("### 🎯 Categorías de Aplicaciones")
    st.caption("Explora diferentes aplicaciones de IA clasificadas por función")

# Header principal
st.markdown("""
<div class="header-container">
    <h1>🚀 Aplicaciones de Inteligencia Artificial</h1>
    <p>Descubre el poder transformador de la IA en diferentes campos</p>
</div>
""", unsafe_allow_html=True)

# Aplicaciones en 3 columnas con mejor distribución
aplicaciones = [
    {
        "titulo": "🎙️ Conversión de Texto a Voz",
        "descripcion": "Transforma textos en audio de alta calidad usando IA avanzada",
        "imagen": "txt_to_audio2.png",
        "enlace": "https://imultimod.streamlit.app/",
        "etiqueta": "TTS",
        "color": "#FF6B6B"
    },
    {
        "titulo": "👂 Conversión de Voz a Texto",
        "descripcion": "Convierte el audio en texto con precisión y en tiempo real",
        "imagen": "OIG8.jpg",
        "enlace": "https://traductorw.streamlit.app/",
        "etiqueta": "STT",
        "color": "#FDCB6E"
    },
    {
        "titulo": "📄 Generación en Contexto (RAG)",
        "descripcion": "Analiza documentos PDF y responde preguntas inteligentes",
        "imagen": "Chat_pdf.png",
        "enlace": "https://chatpdf-cc.streamlit.app/",
        "etiqueta": "RAG",
        "color": "#6C5CE7"
    },
    {
        "titulo": "🔍 Reconocimiento de Objetos",
        "descripcion": "Detecta y clasifica objetos en imágenes usando YOLO",
        "imagen": "txt_to_audio.png",
        "enlace": "https://yolov5cmc.streamlit.app/",
        "etiqueta": "YOLO",
        "color": "#00B894"
    },
    {
        "titulo": "📊 Análisis de Datos",
        "descripcion": "Análisis inteligente de datos con agentes de IA",
        "imagen": "data_analisis.png",
        "enlace": "https://dataagente.streamlit.app/",
        "etiqueta": "Datos",
        "color": "#74B9FF"
    },
    {
        "titulo": "🎓 Entrenando Modelos",
        "descripcion": "Aprende a entrenar y usar tus propios modelos de IA",
        "imagen": "OIG5.jpg",
        "enlace": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "etiqueta": "ML",
        "color": "#FFA502"
    },
    {
        "titulo": "🎬 Transcriptor Audio y Video",
        "descripcion": "Transcribe automáticamente audio y video a texto",
        "imagen": "OIG3.jpg",
        "enlace": "https://transcript-whisper.streamlit.app/",
        "etiqueta": "Whisper",
        "color": "#E84393"
    },
    {
        "titulo": "👁️ Análisis de Imagen",
        "descripcion": "Análisis visual avanzado con modelos de visión IA",
        "imagen": "OIG4.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/",
        "etiqueta": "Vision",
        "color": "#00D2D3"
    },
    {
        "titulo": "🌐 Sistema Ciberfísico",
        "descripcion": "Interacción inteligente con el mundo físico",
        "imagen": "OIG6.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/",
        "etiqueta": "IoT",
        "color": "#B19CD9"
    }
]

# Mostrar aplicaciones en grid 3x3
cols = st.columns(3)
for idx, app in enumerate(aplicaciones):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="app-card" style="border-left-color: {app['color']};">
            <div class="app-card-title">{app['titulo']}</div>
            <div class="app-card-text">{app['descripcion']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Mostrar imagen
        try:
            image = Image.open(app['imagen'])
            st.image(image, use_column_width=True)
        except:
            st.warning(f"Imagen no encontrada: {app['imagen']}")
        
        # Botón de enlace mejorado
        col_btn1, col_btn2 = st.columns([2, 1])
        with col_btn1:
            st.markdown(f"""
            <a href="{app['enlace']}" target="_blank" style="
                display: inline-block;
                background: linear-gradient(135deg, {app['color']}, #667eea);
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                text-align: center;
                width: 100%;
                box-sizing: border-box;
                transition: transform 0.2s;
            " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                🚀 Acceder
            </a>
            """, unsafe_allow_html=True)
        
        with col_btn2:
            st.markdown(f"""
            <div style="
                background: {app['color']};
                color: white;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
                font-size: 0.85em;
            ">
                {app['etiqueta']}
            </div>
            """, unsafe_allow_html=True)

# Sección de estadísticas
st.markdown("---")
st.markdown("### 📈 Estadísticas de Aplicaciones")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Total de Apps", "9", "100% Funcionales", delta_color="off")

with stat_col2:
    st.metric("Categorías", "8", "Diferentes usos", delta_color="off")

with stat_col3:
    st.metric("Disponibilidad", "24/7", "Acceso libre", delta_color="off")

with stat_col4:
    st.metric("Usuarios", "∞", "Bienvenidos!", delta_color="off")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666;">
    <p><strong>¿Listo para explorar el futuro de la IA?</strong></p>
    <p>Selecciona cualquiera de las aplicaciones anterior para comenzar tu viaje en Inteligencia Artificial</p>
    <p style="margin-top: 20px; font-size: 0.85em;">
        © 2024 Portfolio de Inteligencia Artificial | 🚀 Potenciado por Streamlit
    </p>
</div>
""", unsafe_allow_html=True)


