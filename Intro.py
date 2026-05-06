import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(layout="wide")

# =====================================================
# DATA
# =====================================================
aplicaciones = [
    {"titulo": "Texto a Voz", "descripcion": "Convierte texto en audio", "categoria": "Audio", "nuevo": True, "color": "lime"},
    {"titulo": "Voz a Texto", "descripcion": "Transcribe audio", "categoria": "Audio", "nuevo": False, "color": "butter"},
    {"titulo": "YOLO Objetos", "descripcion": "Detecta objetos", "categoria": "Visión", "nuevo": False, "color": "magenta"},
    {"titulo": "Análisis Imagen", "descripcion": "IA visual avanzada", "categoria": "Visión", "nuevo": True, "color": "violet"},
    {"titulo": "RAG PDF", "descripcion": "Pregunta sobre PDFs", "categoria": "NLP", "nuevo": False, "color": "lime"},
]

# =====================================================
# HTML + CSS PRO
# =====================================================
html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

/* RESET */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* BODY */
body {
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: #0f172a;
    color: white;
}

/* GRID RESPONSIVE REAL */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 24px;
    padding: 20px;
}

/* CARD */
.card {
    background: #1e293b;
    border-radius: 18px;
    overflow: hidden;
    transition: 0.3s ease;
    display: flex;
    flex-direction: column;
}

.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}

/* BORDE COLOR */
.card.lime { border-left: 5px solid #84cc16; }
.card.butter { border-left: 5px solid #facc15; }
.card.magenta { border-left: 5px solid #ec4899; }
.card.violet { border-left: 5px solid #8b5cf6; }

/* IMAGE */
.card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
}

/* CONTENT */
.content {
    padding: 16px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

/* BADGES */
.badge {
    background: #ec4899;
    font-size: 11px;
    padding: 4px 8px;
    border-radius: 6px;
    margin-bottom: 6px;
    width: fit-content;
}

.category {
    background: #334155;
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 999px;
    margin-bottom: 8px;
    width: fit-content;
}

/* TEXT */
.title {
    font-size: 16px;
    font-weight: 700;
}

.desc {
    font-size: 13px;
    color: #cbd5f5;
    margin: 10px 0;
    flex-grow: 1;
}

/* BUTTON */
.btn {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    text-decoration: none;
    color: white;
    font-size: 13px;
    transition: 0.2s;
}

.btn:hover {
    transform: scale(1.05);
}

</style>
</head>

<body>

<div class="grid">
"""

# =====================================================
# GENERAR CARDS
# =====================================================
for app in aplicaciones:
    titulo_safe = urllib.parse.quote(app["titulo"])

    html += f"""
    <div class="card {app['color']}">
        <img src="https://via.placeholder.com/400x150?text={titulo_safe}">
        <div class="content">
            {"<div class='badge'>🆕 NUEVO</div>" if app["nuevo"] else ""}
            <div class="category">{app["categoria"]}</div>
            <div class="title">{app["titulo"]}</div>
            <div class="desc">{app["descripcion"]}</div>
            <a href="#" class="btn">Ver app</a>
        </div>
    </div>
    """

html += """
</div>
</body>
</html>
"""

# =====================================================
# RENDER PERFECTO
# =====================================================
components.html(html, height=800, scrolling=True)
