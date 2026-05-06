import streamlit as st

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="Portafolio IA", layout="wide")

# =====================================================
# CSS ANIMADO PRO
# =====================================================
st.markdown("""
<style>

/* FONDO GENERAL */
html, body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER */
.title {
    text-align: center;
    color: white;
    font-size: 2.5em;
    font-weight: 700;
    margin-bottom: 5px;
    animation: fadeDown 0.8s ease;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
    animation: fadeDown 1s ease;
}

/* GRID */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 25px;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 15px;
    text-align: center;
    transition: all 0.35s cubic-bezier(.2,.8,.2,1);
    animation: fadeUp 0.6s ease forwards;
    opacity: 0;
}

/* ANIMACIÓN ESCALONADA */
.card:nth-child(1){ animation-delay: 0.1s;}
.card:nth-child(2){ animation-delay: 0.2s;}
.card:nth-child(3){ animation-delay: 0.3s;}
.card:nth-child(4){ animation-delay: 0.4s;}
.card:nth-child(5){ animation-delay: 0.5s;}
.card:nth-child(6){ animation-delay: 0.6s;}

/* HOVER PRO */
.card:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
}

/* IMAGEN */
.card img {
    border-radius: 12px;
    margin-bottom: 10px;
    transition: transform 0.3s ease;
}

.card:hover img {
    transform: scale(1.05);
}

/* TEXTOS */
.card-title {
    color: white;
    font-weight: 600;
    margin-bottom: 5px;
}

.card-desc {
    color: #cbd5e1;
    font-size: 13px;
    margin-bottom: 12px;
}

/* BOTÓN */
.btn {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    padding: 10px;
    border-radius: 10px;
    color: white;
    text-decoration: none;
    display: inline-block;
    transition: all 0.25s ease;
}

.btn:hover {
    transform: scale(1.08);
    box-shadow: 0 0 20px rgba(139,92,246,0.7);
}

/* INPUT */
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 10px;
}

/* KEYFRAMES */
@keyframes fadeUp {
    from {
        transform: translateY(40px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

@keyframes fadeDown {
    from {
        transform: translateY(-20px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.markdown('<div class="title">🚀 Portafolio IA</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Explora aplicaciones con animaciones modernas</div>', unsafe_allow_html=True)

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
    {"titulo":"Datos IA","desc":"Analiza datos","img":"data_analisis.png","url":"https://dataagente.streamlit.app/"},
    {"titulo":"Transcriptor","desc":"Audio a texto","img":"OIG3.jpg","url":"https://transcript-whisper.streamlit.app/"},
    {"titulo":"RAG PDF","desc":"Consulta documentos","img":"Chat_pdf.png","url":"https://chatpdf-cc.streamlit.app/"},
    {"titulo":"Visión IA","desc":"Analiza imágenes","img":"OIG4.jpg","url":"https://vision2-gpt4o.streamlit.app/"},
    {"titulo":"Ciberfísico","desc":"IA + mundo real","img":"OIG6.jpg","url":"https://vision2-gpt4o.streamlit.app/"},
]

# =====================================================
# FILTRO
# =====================================================
apps_filtradas = [
    app for app in apps
    if search.lower() in app["titulo"].lower()
]

# =====================================================
# RENDER GRID
# =====================================================
html = '<div class="grid">'

for app in apps_filtradas:
    html += f"""
    <div class="card">
        <img src="{app['img']}" width="100%">
        <div class="card-title">{app['titulo']}</div>
        <div class="card-desc">{app['desc']}</div>
        <a href="{app['url']}" target="_blank" class="btn">Ir a la app</a>
    </div>
    """

html += "</div>"

st.markdown(html, unsafe_allow_html=True)
