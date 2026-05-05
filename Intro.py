import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(
    page_title="Portfolio IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS con cards pequeñas
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 40px 20px;
    }
    
    .header {
        text-align: center;
        margin-bottom: 40px;
    }
    
    .header h1 {
        color: #1a1a1a;
        font-size: 2.2em;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }
    
    .header p {
        color: #666;
        font-size: 1em;
        font-weight: 300;
    }
    
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        max-width: 1000px;
        margin: 0 auto;
    }
    
    .card {
        background: white;
        border-radius: 8px;
        padding: 12px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        border-top: 2px solid #667eea;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    
    .card:hover {
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    .card-image {
        width: 100%;
        height: 100px;
        object-fit: cover;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    
    .card-title {
        font-size: 0.8em;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 5px;
        line-height: 1.2;
        min-height: 25px;
    }
    
    .card-description {
        font-size: 0.7em;
        color: #999;
        margin-bottom: 8px;
        flex-grow: 1;
        line-height: 1.3;
    }
    
    .card-button {
        background-color: #667eea;
        color: white;
        border: none;
        padding: 6px 10px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.7em;
        font-weight: 600;
        text-decoration: none;
        display: block;
        text-align: center;
        transition: background-color 0.2s ease;
        width: 100%;
        box-sizing: border-box;
    }
    
    .card-button:hover {
        background-color: #5568d3;
    }
    
    @media (max-width: 1200px) {
        .cards-grid {
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
        }
    }
    
    @media (max-width: 768px) {
        .cards-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🤖 Sobre la IA")
    st.markdown("""
    La **Inteligencia Artificial** permite mejorar la toma de decisiones con datos, 
    automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real.
    """)
    
    st.markdown("---")
    st.markdown("## 📚 Recursos")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.markdown(f"[📖 Más ejercicios y recursos]({url_ia})")

# Header
st.markdown("""
<div class="header">
    <h1>🚀 Aplicaciones de Inteligencia Artificial</h1>
    <p>Explora el poder transformador de la IA</p>
</div>
""", unsafe_allow_html=True)

# Lista de 20 aplicaciones
aplicaciones = [
    {
        "titulo": "Conversión de Texto a Voz",
        "descripcion": "Transforma textos en audio",
        "imagen": "txt_to_audio2.png",
        "enlace": "https://imultimod.streamlit.app/"
    },
    {
        "titulo": "Conversión de Voz a Texto",
        "descripcion": "Convierte audio en texto",
        "imagen": "OIG8.jpg",
        "enlace": "https://traductorw.streamlit.app/"
    },
    {
        "titulo": "Reconocimiento de Objetos",
        "descripcion": "Detecta objetos con YOLO",
        "imagen": "txt_to_audio.png",
        "enlace": "https://yolov5cmc.streamlit.app/"
    },
    {
        "titulo": "Análisis de Imagen",
        "descripcion": "Análisis visual con IA",
        "imagen": "OIG4.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "titulo": "Generación en Contexto",
        "descripcion": "Analiza PDFs inteligentemente",
        "imagen": "Chat_pdf.png",
        "enlace": "https://chatpdf-cc.streamlit.app/"
    },
    {
        "titulo": "Análisis de Datos",
        "descripcion": "Análisis con agentes IA",
        "imagen": "data_analisis.png",
        "enlace": "https://dataagente.streamlit.app/"
    },
    {
        "titulo": "Transcriptor Audio y Video",
        "descripcion": "Transcribe automáticamente",
        "imagen": "OIG3.jpg",
        "enlace": "https://transcript-whisper.streamlit.app/"
    },
    {
        "titulo": "Entrenando Modelos",
        "descripcion": "Entrena modelos de IA",
        "imagen": "OIG5.jpg",
        "enlace": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "titulo": "Sistema Ciberfísico",
        "descripcion": "Interacción física con IA",
        "imagen": "OIG6.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "titulo": "Aplicación 10",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 11",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 12",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 13",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 14",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 15",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 16",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 17",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 18",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 19",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 20",
        "descripcion": "Descripción aquí",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    }
]

# Contenedor principal centrado
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Grid de cards
st.markdown('<div class="cards-grid">', unsafe_allow_html=True)

for app in aplicaciones:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{app['titulo']}</div>
        <div class="card-description">{app['descripcion']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Imagen
    try:
        image = Image.open(app['imagen'])
        st.image(image, use_column_width=True)
    except:
        st.image("https://via.placeholder.com/150x100?text=No+image", use_column_width=True)
    
    # Botón
    st.markdown(f"""
    <a href="{app['enlace']}" target="_blank" style="text-decoration: none;">
        <button class="card-button">🔗 Acceder</button>
    </a>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #999; font-size: 0.9em;">
    <p>© 2024 Portfolio de Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)
