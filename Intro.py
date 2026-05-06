import streamlit as st
import base64

# =====================================================
# FUNCION PARA IMAGEN LOCAL
# =====================================================
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="Portafolio IA", layout="wide")

# =====================================================
# ESTILOS
# =====================================================
st.markdown("""
<style>

.card {
    border-radius: 18px;
    overflow: hidden;
    transition: 0.35s;
    margin-bottom: 30px;
    color: white;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

.card img {
    width: 100%;
    height: 160px;
    object-fit: cover;
}

.card-content {
    padding: 16px;
    text-align: center;
}

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

.btn {
    background: rgba(255,255,255,0.2);
    padding: 9px 14px;
    border-radius: 10px;
    text-decoration: none;
    color: white;
    font-size: 13px;
    display: inline-block;
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
# DATA
# =====================================================
apps = [
    
    {"titulo":"PRIMERA PÁGINA","desc":"La IA identifica lo que escribes","img":get_base64("gato.png"),"url":"https://intro-isv2-del2s74hdlvmnh4d3xygyw.streamlit.app/","color":"lime"},
    {"titulo":"ANÁLISIS DE TEXTO","desc":"La IA analiza el texto que cargues o escribas y te filtra algunos datos","img":get_base64("analisistexto.jpg"),"url":"https://isv-bit-analisis-de-texto-app-pxurpk.streamlit.app/","color":"butter"},
    {"titulo":"ANÁLISIS PDF","desc":"Analiza datos con IA de un archivo PDF","img":get_base64("pdf.jpg"),"url":"https://chatpdf-isa.streamlit.app/","color":"blue"},
    {"titulo":"TRADUCTOR","desc":"Aplicación que convierte voz o texto de un idioma a otro de forma rápida y automática.","img":get_base64("traductor.jpg"),"url":"https://traductor-isa.streamlit.app/","color":"violet"},
    {"titulo":"CONTROL POR VOZ","desc":"La IA transcribe lo que dices","img":get_base64("controlvoz.jpg"),"url":"https://controlvoz-isa.streamlit.app/","color":"magenta"},
    {"titulo":"ANÁLISIS DE IMAGEN","desc":"La IA describe de forma inteligente la imagen que subes","img":get_base64("analisisimagen.jpg"),"url":"https://visionapp-isa.streamlit.app/","color":"lime"},
    {"titulo":"DEMO PREGUNTAS Y RESPUESTAS EN INGLÉS","desc":"Aplicación que compara textos usando TF-IDF para encontrar el documento más relevante según una pregunta.","img":get_base64("pyr.jpg"),"url":"https://tf-idf-isabel.streamlit.app/","color":"butter"},
    {"titulo":"DEMO PREGUNTAS Y RESPUESTAS EN ESPAÑOL","desc":"Aplicación que compara textos usando TF-IDF para encontrar el documento más relevante según una pregunta.","img":get_base64("pyr.jpg"),"url":"https://tf-espanol.streamlit.app/","color":"blue"},
    {"titulo":"ANÁLISIS DE SENTIMIENTOS","desc":"Aplicación que analiza el sentimiento de un texto y determina si es positivo, negativo o neutral.","img":get_base64("sentimental.jpg"),"url":"https://sentimenta-isa.streamlit.app/","color":"violet"},
    {"titulo":"WORD CLOUD","desc":"Esta aplicación genera una nube de palabras a partir de cualquier texto,resaltando visualmente las palabras más frecuentes.","img":get_base64("cloud.jpg"),"url":"https://wordcloudisa.streamlit.app/","color":"magenta"},
     {"titulo":"PRIMERA PÁGINA","desc":"La IA identifica lo que escribes","img":get_base64("gato.png"),"url":"https://intro-isv2-del2s74hdlvmnh4d3xygyw.streamlit.app/","color":"lime"},
    {"titulo":"ANÁLISIS DE TEXTO","desc":"La IA analiza el texto que cargues o escribas y te filtra algunos datos","img":get_base64("analisistexto.jpg"),"url":"https://isv-bit-analisis-de-texto-app-pxurpk.streamlit.app/","color":"butter"},
    {"titulo":"ANÁLISIS PDF","desc":"Analiza datos con IA de un archivo PDF","img":get_base64("pdf.jpg"),"url":"https://chatpdf-isa.streamlit.app/","color":"blue"},
    {"titulo":"TRADUCTOR","desc":"Aplicación que convierte voz o texto de un idioma a otro de forma rápida y automática.","img":get_base64("traductor.jpg"),"url":"https://traductor-isa.streamlit.app/","color":"violet"},
    {"titulo":"CONTROL POR VOZ","desc":"La IA transcribe lo que dices","img":get_base64("controlvoz.jpg"),"url":"https://controlvoz-isa.streamlit.app/","color":"magenta"},
    {"titulo":"ANÁLISIS DE IMAGEN","desc":"La IA describe de forma inteligente la imagen que subes","img":get_base64("analisisimagen.jpg"),"url":"https://visionapp-isa.streamlit.app/","color":"lime"},
    {"titulo":"DEMO PREGUNTAS Y RESPUESTAS EN INGLÉS","desc":"Aplicación que compara textos usando TF-IDF para encontrar el documento más relevante según una pregunta.","img":get_base64("pyr.jpg"),"url":"https://tf-idf-isabel.streamlit.app/","color":"butter"},
    {"titulo":"DEMO PREGUNTAS Y RESPUESTAS EN ESPAÑOL","desc":"Aplicación que compara textos usando TF-IDF para encontrar el documento más relevante según una pregunta.","img":get_base64("pyr.jpg"),"url":"https://tf-espanol.streamlit.app/","color":"blue"},
    {"titulo":"ANÁLISIS DE SENTIMIENTOS","desc":"Aplicación que analiza el sentimiento de un texto y determina si es positivo, negativo o neutral.","img":get_base64("sentimental.jpg"),"url":"https://sentimenta-isa.streamlit.app/","color":"violet"},
    {"titulo":"WORD CLOUD","desc":"Esta aplicación genera una nube de palabras a partir de cualquier texto,resaltando visualmente las palabras más frecuentes.","img":get_base64("cloud.jpg"),"url":"https://wordcloudisa.streamlit.app/","color":"magenta"},
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
cols = st.columns(3, gap="large")

for i, app in enumerate(apps_filtradas):
    with cols[i % 3]:

        st.markdown(f"""
<div class="card {app['color']}">

<img src="data:image/jpg;base64,{app['img']}">

<div class="card-content">
<div class="card-title">{app['titulo']}</div>
<div class="card-desc">{app['desc']}</div>
<a href="{app['url']}" target="_blank" class="btn">Ir a la app</a>
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.title("📊 Info")
    st.metric("Apps", len(apps))
    st.metric("Estado", "Activo")
