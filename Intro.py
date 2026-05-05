import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portfolio IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .card {
        background: white;
        border-radius: 18px;
        padding: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border-top: 4px solid #667eea;
        transition: box-shadow 0.3s ease, transform 0.2s ease;
        aspect-ratio: 1;
    }
    
    .card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    .card-title {
        font-size: 0.95em;
        font-weight: bold;
        margin: 2px 0;
        color: #333;
        line-height: 1.3;
    }
    
    .card-description {
        font-size: 0.8em;
        color: #666;
        margin-bottom: 6px;
        flex-grow: 1;
        line-height: 1.3;
    }
    
    .card-image {
        width: 100%;
        height: 120px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 6px;
    }
    
    .btn {
        padding: 6px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        transition: all 0.2s;
        width: 100%;
        box-sizing: border-box;
        font-size: 0.85em;
    }
    
    .btn-primary {
        background-color: #667eea;
        color: white;
    }
    
    .btn-primary:hover {
        background-color: #5568d3;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
    }
    
    .header {
        text-align: center;
        padding: 30px 0;
        margin-bottom: 20px;
    }
    
    .header h1 {
        color: #333;
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    
    .header p {
        color: #666;
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

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

st.markdown("""
<div class="header">
    <h1>🚀 Aplicaciones de Inteligencia Artificial</h1>
    <p>Explora el poder transformador de la IA</p>
</div>
""", unsafe_allow_html=True)

aplicaciones = [
    {
        "titulo": "Conversión de Texto a Voz",
        "descripcion": "Transforma textos en audio de alta calidad",
        "imagen": "txt_to_audio2.png",
        "enlace": "https://imultimod.streamlit.app/"
    },
    {
        "titulo": "Conversión de Voz a Texto",
        "descripcion": "Convierte audio en texto con precisión",
        "imagen": "OIG8.jpg",
        "enlace": "https://traductorw.streamlit.app/"
    },
    {
        "titulo": "Reconocimiento de Objetos",
        "descripcion": "Detecta objetos en imágenes con YOLO",
        "imagen": "txt_to_audio.png",
        "enlace": "https://yolov5cmc.streamlit.app/"
    },
    {
        "titulo": "Análisis de Imagen",
        "descripcion": "Análisis visual avanzado con IA",
        "imagen": "OIG4.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "titulo": "Generación en Contexto (RAG)",
        "descripcion": "Analiza PDFs y responde preguntas",
        "imagen": "Chat_pdf.png",
        "enlace": "https://chatpdf-cc.streamlit.app/"
    },
    {
        "titulo": "Análisis de Datos",
        "descripcion": "Análisis inteligente con agentes IA",
        "imagen": "data_analisis.png",
        "enlace": "https://dataagente.streamlit.app/"
    },
    {
        "titulo": "Transcriptor Audio y Video",
        "descripcion": "Transcribe audio/video automáticamente",
        "imagen": "OIG3.jpg",
        "enlace": "https://transcript-whisper.streamlit.app/"
    },
    {
        "titulo": "Entrenando Modelos",
        "descripcion": "Entrena tus propios modelos de IA",
        "imagen": "OIG5.jpg",
        "enlace": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
    },
    {
        "titulo": "Sistema Ciberfísico",
        "descripcion": "Interacción con el mundo físico",
        "imagen": "OIG6.jpg",
        "enlace": "https://vision2-gpt4o.streamlit.app/"
    },
    {
        "titulo": "Aplicación 10",
        "descripcion": "Descripción de la aplicación 10",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 11",
        "descripcion": "Descripción de la aplicación 11",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 12",
        "descripcion": "Descripción de la aplicación 12",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 13",
        "descripcion": "Descripción de la aplicación 13",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 14",
        "descripcion": "Descripción de la aplicación 14",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 15",
        "descripcion": "Descripción de la aplicación 15",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 16",
        "descripcion": "Descripción de la aplicación 16",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 17",
        "descripcion": "Descripción de la aplicación 17",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 18",
        "descripcion": "Descripción de la aplicación 18",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 19",
        "descripcion": "Descripción de la aplicación 19",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    },
    {
        "titulo": "Aplicación 20",
        "descripcion": "Descripción de la aplicación 20",
        "imagen": "txt_to_audio2.png",
        "enlace": "#"
    }
]

cols = st.columns(4)

for idx, app in enumerate(aplicaciones):
    with cols[idx % 4]:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{app['titulo']}</div>
            <div class="card-description">{app['descripcion']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            image = Image.open(app['imagen'])
            st.image(image, use_column_width=True)
        except:
            st.info("📷 Imagen no disponible")
        
        st.markdown(f"""
        <a href="{app['enlace']}" target="_blank">
            <button class="btn btn-primary">
                🔗 Acceder a la App
            </button>
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #999;">
    <p>© 2024 Portfolio de Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)
