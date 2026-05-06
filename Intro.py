import streamlit as st

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="Portafolio IA", layout="wide")

# =====================================================
# ESTILOS MEJORADOS (ESPACIADO + DISEÑO)
# =====================================================
st.markdown("""
<style>

/* CONTENEDOR GENERAL */
.block-container {
    padding-top: 2rem;
}

/* GRID MÁS LIMPIO */
.row-widget.stHorizontal {
    gap: 30px;
}

/* CARD */
.card {
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    transition: all 0.35s ease;
    color: white;
    margin-bottom: 25px;
}

.card:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

/* IMAGEN */
.card img {
    border-radius: 12px;
    margin-bottom: 12px;
}

/* TEXTO */
.card-title {
    font-weight: bold;
    font-size: 16px;
    margin-bottom: 6px;
}

.card-desc {
    font-size: 13px;
    opacity: 0.9;
    margin-bottom: 14px;
}

/* BOTÓN */
.btn {
    background: rgba(255,255,255,0.2);
    padding: 9px 14px;
    border-radius: 10px;
    text-decoration: none;
    color: white;
    font-size: 13px;
    transition: 0.3s;
}

.btn:hover {
    background: white;
    color: black;
}

/* COLORES */
.magenta { background: linear-gradient(135deg, #ff0080, #ff4da6); }
.lime { background: linear-gradient(135deg, #a8ff00, #3cff00); color:black;}
.butter { background: linear-gradient(135deg, #fff200, #ffd000); color:black;}
.blue { background: linear-gradient(135deg, #00c6ff, #0072ff); }
.violet { background: linear-gradient(135deg, #8e2de2, #4a00e0); }

h1 { color: white !important; }

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("🚀 Portafolio de Inteligencia Artificial")
st.write("Explora aplicaciones de IA con diseño moderno y organizado.")

# =====================================================
# BUSCADOR
# =====================================================
search = st.text_input("🔍 Buscar aplicación...")

# =====================================================
# DATA (19 APPS)
# =====================================================
apps = [
    # ORIGINALES
    {"titulo":"CONTROL POR VOZ","desc":"A la hora de habalr la ia lo transcribe","img":"controlvoz.jpg","url":"https://controlvoz-isa.streamlit.app/","color":"magenta"},
    {"titulo":"Voz a Texto","desc":"Transcribe audio","img":"OIG8.jpg","url":"https://traductorw.streamlit.app/","color":"lime"},
    {"titulo":"YOLO Objetos","desc":"Detecta objetos","img":"txt_to_audio.png","url":"https://yolov5cmc.streamlit.app/","color":"butter"},
    {"titulo":"Análisis de Datos","desc":"Analiza datos con IA","img":"data_analisis.png","url":"https://dataagente.streamlit.app/","color":"blue"},
    {"titulo":"Transcriptor","desc":"Audio/video a texto","img":"OIG3.jpg","url":"https://transcript-whisper.streamlit.app/","color":"violet"},
    {"titulo":"RAG PDF","desc":"Consulta documentos","img":"Chat_pdf.png","url":"https://chatpdf-cc.streamlit.app/","color":"magenta"},
    {"titulo":"Visión IA","desc":"Análisis de imágenes","img":"OIG4.jpg","url":"https://vision2-gpt4o.streamlit.app/","color":"blue"},
    {"titulo":"Sistema Ciberfísico","desc":"IA + mundo físico","img":"OIG6.jpg","url":"https://vision2-gpt4o.streamlit.app/","color":"lime"},
    {"titulo":"Entrenamiento","desc":"Modelos IA","img":"OIG5.jpg","url":"https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/","color":"violet"},

    # NUEVAS 10
    {"titulo":"Chat IA","desc":"Asistente inteligente","img":"txt_to_audio2.png","url":"#","color":"magenta"},
    {"titulo":"Resumen IA","desc":"Resume textos","img":"txt_to_audio2.png","url":"#","color":"butter"},
    {"titulo":"Traducción IA","desc":"Traduce idiomas","img":"txt_to_audio2.png","url":"#","color":"blue"},
    {"titulo":"Clasificación","desc":"Clasifica datos","img":"txt_to_audio2.png","url":"#","color":"lime"},
    {"titulo":"Generador Imagen","desc":"Crea imágenes","img":"txt_to_audio2.png","url":"#","color":"violet"},
    {"titulo":"Detector Spam","desc":"Filtra mensajes","img":"txt_to_audio2.png","url":"#","color":"magenta"},
    {"titulo":"Predicción","desc":"Predice valores","img":"txt_to_audio2.png","url":"#","color":"blue"},
    {"titulo":"OCR IA","desc":"Lee imágenes","img":"txt_to_audio2.png","url":"#","color":"butter"},
    {"titulo":"Recomendador","desc":"Sugiere contenido","img":"txt_to_audio2.png","url":"#","color":"lime"},
    {"titulo":"Audio IA","desc":"Procesa sonido","img":"txt_to_audio2.png","url":"#","color":"violet"},
]

# =====================================================
# FILTRO
# =====================================================
apps_filtradas = [
    app for app in apps
    if search.lower() in app["titulo"].lower()
]

# =====================================================
# GRID (MEJOR DISTRIBUCIÓN)
# =====================================================
cols = st.columns(3, gap="large")

for i, app in enumerate(apps_filtradas):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card {app['color']}">
            <img src="{app['img']}" width="100%">
            <div class="card-title">{app['titulo']}</div>
            <div class="card-desc">{app['desc']}</div>
            <a href="{app['url']}" target="_blank" class="btn">Ir a la app</a>
        </div>
        """, unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.title("📊 Info")
    st.metric("Apps", len(apps))
    st.metric("Estado", "Activo")
