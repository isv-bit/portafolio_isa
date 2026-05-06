import streamlit as st

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="Portafolio IA", layout="wide")

# =====================================================
# ESTILOS (COLORES + CARDS)
# =====================================================
st.markdown("""
<style>
.card {
    background: #ffffff;
    border-radius: 16px;
    padding: 15px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    text-align: center;
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.2);
}

.card img {
    border-radius: 12px;
    margin-bottom: 10px;
}

.card-title {
    font-weight: bold;
    font-size: 16px;
    margin-bottom: 5px;
}

.card-desc {
    font-size: 13px;
    color: gray;
    margin-bottom: 10px;
}

.btn {
    background: linear-gradient(135deg, #ff4b2b, #ff416c);
    color: white;
    padding: 8px 14px;
    border-radius: 8px;
    text-decoration: none;
    font-size: 13px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("🚀 Portafolio de Inteligencia Artificial")
st.write("Explora aplicaciones de IA organizadas en un diseño moderno e interactivo.")

# =====================================================
# BUSCADOR
# =====================================================
search = st.text_input("🔍 Buscar aplicación...")

# =====================================================
# DATA
# =====================================================
apps = [
    {"titulo":"Texto a Voz","desc":"Convierte texto en audio","img":"txt_to_audio2.png","url":"https://imultimod.streamlit.app/"},
    {"titulo":"Voz a Texto","desc":"Transcribe audio","img":"OIG8.jpg","url":"https://traductorw.streamlit.app/"},
    {"titulo":"YOLO Objetos","desc":"Detecta objetos","img":"txt_to_audio.png","url":"https://yolov5cmc.streamlit.app/"},
    {"titulo":"Análisis de Datos","desc":"Analiza datos con IA","img":"data_analisis.png","url":"https://dataagente.streamlit.app/"},
    {"titulo":"Transcriptor","desc":"Audio y video a texto","img":"OIG3.jpg","url":"https://transcript-whisper.streamlit.app/"},
    {"titulo":"RAG PDF","desc":"Consulta documentos","img":"Chat_pdf.png","url":"https://chatpdf-cc.streamlit.app/"},
    {"titulo":"Visión IA","desc":"Análisis de imágenes","img":"OIG4.jpg","url":"https://vision2-gpt4o.streamlit.app/"},
    {"titulo":"Sistema Ciberfísico","desc":"IA + mundo físico","img":"OIG6.jpg","url":"https://vision2-gpt4o.streamlit.app/"},
    {"titulo":"Entrenamiento","desc":"Entrena modelos IA","img":"OIG5.jpg","url":"https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"},
]

# =====================================================
# FILTRO
# =====================================================
apps_filtradas = [
    app for app in apps
    if search.lower() in app["titulo"].lower()
]

# =====================================================
# GRID DE CARDS (3 COLUMNAS)
# =====================================================
cols = st.columns(3)

for i, app in enumerate(apps_filtradas):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
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
    st.write("Aplicaciones de IA organizadas en cards interactivas.")
    st.metric("Apps", len(apps))
    st.metric("Estado", "Activo")
