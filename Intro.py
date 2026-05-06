import streamlit as st

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="Portafolio IA", layout="wide")

# =====================================================
# ESTILOS (COLORES LLAMATIVOS)
# =====================================================
st.markdown("""
<style>

/* FONDO GENERAL */
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* CARD BASE */
.card {
    border-radius: 18px;
    padding: 16px;
    text-align: center;
    transition: all 0.35s ease;
    color: white;
    position: relative;
    overflow: hidden;
}

/* EFECTO HOVER */
.card:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

/* IMAGEN */
.card img {
    border-radius: 12px;
    margin-bottom: 10px;
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
    margin-bottom: 12px;
}

/* BOTÓN */
.btn {
    background: rgba(255,255,255,0.2);
    padding: 8px 14px;
    border-radius: 10px;
    text-decoration: none;
    color: white;
    font-size: 13px;
    transition: 0.3s;
    display: inline-block;
}

.btn:hover {
    background: white;
    color: black;
}

/* 🎨 COLORES POR CARD */
.magenta {
    background: linear-gradient(135deg, #ff0080, #ff4da6);
}

.lime {
    background: linear-gradient(135deg, #a8ff00, #3cff00);
    color: black;
}

.butter {
    background: linear-gradient(135deg, #fff200, #ffd000);
    color: black;
}

.blue {
    background: linear-gradient(135deg, #00c6ff, #0072ff);
}

.violet {
    background: linear-gradient(135deg, #8e2de2, #4a00e0);
}

/* HEADER */
h1 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("🚀 Portafolio de Inteligencia Artificial")
st.write("Explora aplicaciones de IA con un diseño moderno, colorido y visualmente atractivo.")

# =====================================================
# BUSCADOR
# =====================================================
search = st.text_input("🔍 Buscar aplicación...")

# =====================================================
# DATA (CON COLORES)
# =====================================================
apps = [
    {"titulo":"Texto a Voz","desc":"Convierte texto en audio","img":"txt_to_audio2.png","url":"https://imultimod.streamlit.app/","color":"magenta"},
    {"titulo":"Voz a Texto","desc":"Transcribe audio","img":"OIG8.jpg","url":"https://traductorw.streamlit.app/","color":"lime"},
    {"titulo":"YOLO Objetos","desc":"Detecta objetos","img":"txt_to_audio.png","url":"https://yolov5cmc.streamlit.app/","color":"butter"},
    {"titulo":"Análisis de Datos","desc":"Analiza datos con IA","img":"data_analisis.png","url":"https://dataagente.streamlit.app/","color":"blue"},
    {"titulo":"Transcriptor","desc":"Audio y video a texto","img":"OIG3.jpg","url":"https://transcript-whisper.streamlit.app/","color":"violet"},
    {"titulo":"RAG PDF","desc":"Consulta documentos","img":"Chat_pdf.png","url":"https://chatpdf-cc.streamlit.app/","color":"magenta"},
    {"titulo":"Visión IA","desc":"Análisis de imágenes","img":"OIG4.jpg","url":"https://vision2-gpt4o.streamlit.app/","color":"blue"},
    {"titulo":"Sistema Ciberfísico","desc":"IA + mundo físico","img":"OIG6.jpg","url":"https://vision2-gpt4o.streamlit.app/","color":"lime"},
    {"titulo":"Entrenamiento","desc":"Entrena modelos IA","img":"OIG5.jpg","url":"https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/","color":"violet"},
]

# =====================================================
# FILTRO
# =====================================================
apps_filtradas = [
    app for app in apps
    if search.lower() in app["titulo"].lower()
]

# =====================================================
# GRID
# =====================================================
cols = st.columns(3)

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
    st.write("Aplicaciones de IA organizadas en cards modernas.")
    st.metric("Apps", len(apps))
    st.metric("Estado", "Activo")
