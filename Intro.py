<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portafolio de Aplicaciones de IA</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            min-height: 100vh;
            display: flex;
        }

        /* ==================== SIDEBAR PEQUEÑO ==================== */
        .sidebar {
            width: 220px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px 15px;
            min-height: 100vh;
            position: fixed;
            left: 0;
            top: 0;
            color: white;
            overflow-y: auto;
            box-shadow: 5px 0 15px rgba(0, 0, 0, 0.1);
        }

        .sidebar-header {
            text-align: center;
            margin-bottom: 25px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.2);
            padding-bottom: 15px;
        }

        .sidebar-header h2 {
            font-size: 1.1em;
            margin-bottom: 5px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        .sidebar-header p {
            font-size: 0.75em;
            opacity: 0.9;
        }

        .sidebar-stats {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .sidebar-stat-card {
            background: rgba(255, 255, 255, 0.15);
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .sidebar-stat-card:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateX(3px);
        }

        .sidebar-stat-number {
            font-size: 1.5em;
            font-weight: 700;
            margin-bottom: 3px;
        }

        .sidebar-stat-label {
            font-size: 0.75em;
            opacity: 0.9;
        }

        .sidebar-info {
            margin-top: 25px;
            padding-top: 15px;
            border-top: 2px solid rgba(255, 255, 255, 0.2);
        }

        .sidebar-info h3 {
            font-size: 0.8em;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            opacity: 0.9;
        }

        .sidebar-info p {
            font-size: 0.75em;
            line-height: 1.5;
            opacity: 0.85;
            margin-bottom: 10px;
        }

        .sidebar-link {
            display: inline-block;
            color: white;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.75em;
            border-bottom: 2px solid white;
            transition: all 0.3s ease;
        }

        .sidebar-link:hover {
            opacity: 0.8;
        }

        /* ==================== MAIN CONTENT ==================== */
        .main-content {
            margin-left: 220px;
            flex: 1;
            padding: 30px 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        /* ==================== HEADER ==================== */
        .header {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            animation: fadeInDown 0.8s ease;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }

        .header p {
            font-size: 1.1em;
            font-weight: 300;
            color: #666;
        }

        /* ==================== SEARCH ==================== */
        .search-container {
            margin-bottom: 30px;
            display: flex;
            justify-content: center;
        }

        .search-input {
            width: 100%;
            max-width: 500px;
            padding: 12px 20px;
            border: 2px solid #667eea;
            border-radius: 25px;
            font-size: 1em;
            background: white;
            color: #333;
            transition: all 0.3s ease;
        }

        .search-input::placeholder {
            color: #999;
        }

        .search-input:focus {
            outline: none;
            border-color: #764ba2;
            box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
        }

        /* ==================== FILTROS ==================== */
        .filters {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 35px;
            flex-wrap: wrap;
            animation: fadeInUp 0.8s ease;
        }

        .filter-btn {
            padding: 10px 20px;
            border: 2px solid #667eea;
            background: white;
            color: #667eea;
            border-radius: 25px;
            cursor: pointer;
            font-size: 0.95em;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .filter-btn:hover,
        .filter-btn.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-2px);
        }

        /* ==================== GRID DE CARDS ==================== */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        /* ==================== COLORS PARA BORDES ==================== */
        .card-border-1 { border-left: 6px solid #ADFF2F; }
        .card-border-2 { border-left: 6px solid #FFD700; }
        .card-border-3 { border-left: 6px solid #FF1493; }
        .card-border-4 { border-left: 6px solid #9D4EDD; }
        .card-border-5 { border-left: 6px solid #ADFF2F; }
        .card-border-6 { border-left: 6px solid #FFD700; }
        .card-border-7 { border-left: 6px solid #FF1493; }
        .card-border-8 { border-left: 6px solid #9D4EDD; }

        /* ==================== CARDS ==================== */
        .card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            animation: fadeInUp 0.6s ease;
            display: flex;
            flex-direction: column;
            height: 100%;
            position: relative;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .card-image {
            width: 100%;
            height: 180px;
            object-fit: cover;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .card-content {
            padding: 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .card-category {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.7em;
            font-weight: 600;
            margin-bottom: 10px;
            width: fit-content;
        }

        .card-title {
            font-size: 1.2em;
            font-weight: 700;
            color: #333;
            margin-bottom: 8px;
            line-height: 1.3;
        }

        .card-description {
            font-size: 0.9em;
            color: #666;
            margin-bottom: 15px;
            line-height: 1.5;
            flex-grow: 1;
        }

        .card-footer {
            display: flex;
            gap: 10px;
            margin-top: auto;
        }

        .btn {
            flex: 1;
            padding: 11px 16px;
            border: none;
            border-radius: 8px;
            font-size: 0.9em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        /* ==================== BADGE NUEVO ==================== */
        .badge-new {
            position: absolute;
            top: 10px;
            right: 10px;
            background: #FF1493;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.7em;
            font-weight: 700;
        }

        .card-image-container {
            position: relative;
            overflow: hidden;
        }

        .card-image-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(102, 126, 234, 0.3);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .card:hover .card-image-overlay {
            opacity: 1;
        }

        /* ==================== INFO BOX ==================== */
        .info-box {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin-bottom: 40px;
            border-left: 6px solid #ADFF2F;
        }

        .info-box h2 {
            color: #333;
            margin-bottom: 12px;
            font-size: 1.2em;
        }

        .info-box p {
            color: #666;
            line-height: 1.6;
            font-size: 0.95em;
        }

        .info-box a {
            color: #667eea;
            font-weight: 600;
            text-decoration: none;
        }

        .info-box a:hover {
            text-decoration: underline;
        }

        /* ==================== FOOTER ==================== */
        .footer {
            text-align: center;
            color: #666;
            padding: 25px 0;
            border-top: 1px solid #ddd;
            margin-top: 40px;
        }

        .footer p {
            font-size: 0.95em;
        }

        /* ==================== ANIMACIONES ==================== */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* ==================== RESPONSIVO ==================== */
        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                height: auto;
                position: relative;
                padding: 20px;
                min-height: auto;
            }

            .main-content {
                margin-left: 0;
                padding: 20px 10px;
            }

            .header h1 {
                font-size: 1.8em;
            }

            .grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }

            .filters {
                gap: 8px;
            }

            .filter-btn {
                padding: 8px 15px;
                font-size: 0.85em;
            }

            .sidebar-stats {
                flex-direction: row;
                flex-wrap: wrap;
            }

            .sidebar-stat-card {
                flex: 1;
                min-width: 100px;
            }
        }
    </style>
</head>
<body>
    <!-- ==================== SIDEBAR PEQUEÑO ==================== -->
    <div class="sidebar">
        <div class="sidebar-header">
            <h2>🚀 Portafolio</h2>
            <p>Aplicaciones IA</p>
        </div>

        <div class="sidebar-stats">
            <div class="sidebar-stat-card">
                <div class="sidebar-stat-number">20</div>
                <div class="sidebar-stat-label">Aplicaciones</div>
            </div>
            <div class="sidebar-stat-card">
                <div class="sidebar-stat-number">8</div>
                <div class="sidebar-stat-label">Categorías</div>
            </div>
            <div class="sidebar-stat-card">
                <div class="sidebar-stat-number">100%</div>
                <div class="sidebar-stat-label">Funcional</div>
            </div>
            <div class="sidebar-stat-card">
                <div class="sidebar-stat-number">24/7</div>
                <div class="sidebar-stat-label">Disponible</div>
            </div>
        </div>

        <div class="sidebar-info">
            <h3>📚 Info</h3>
            <p>Las mejores aplicaciones de IA con Streamlit.</p>
            <p>
                <a href="#" class="sidebar-link">Contacta</a>
            </p>
        </div>
    </div>

    <!-- ==================== CONTENIDO PRINCIPAL ==================== -->
    <div class="main-content">
        <div class="container">
            <!-- ==================== HEADER ==================== -->
            <div class="header">
                <h1>🚀 Portafolio de IA</h1>
                <p>Explora aplicaciones inteligentes de Streamlit</p>
            </div>

            <!-- ==================== BARRA DE BÚSQUEDA ==================== -->
            <div class="search-container">
                <input 
                    type="text" 
                    class="search-input" 
                    id="searchInput" 
                    placeholder="🔍 Buscar aplicaciones..."
                >
            </div>

            <!-- ==================== FILTROS ==================== -->
            <div class="filters">
                <button class="filter-btn active" data-filter="todos">Todos</button>
                <button class="filter-btn" data-filter="audio">Audio</button>
                <button class="filter-btn" data-filter="vision">Visión</button>
                <button class="filter-btn" data-filter="datos">Datos</button>
                <button class="filter-btn" data-filter="nlp">NLP</button>
            </div>

            <!-- ==================== INFO BOX ==================== -->
            <div class="info-box">
                <h2>📚 Sobre este Portafolio</h2>
                <p>Este portafolio showcasea las mejores aplicaciones de inteligencia artificial construidas con Streamlit. Cada aplicación representa diferentes casos de uso de IA, desde procesamiento de lenguaje natural hasta visión por computadora y análisis de datos avanzado.</p>
            </div>

            <!-- ==================== GRID DE CARDS ==================== -->
            <div class="grid" id="cardsGrid">
                <!-- Las cards se cargarán aquí con JavaScript -->
            </div>

            <!-- ==================== FOOTER ==================== -->
            <div class="footer">
                <p>© 2024 Portafolio de Inteligencia Artificial | Powered by Streamlit</p>
                <p style="margin-top: 8px; font-size: 0.85em;">Diseñado con ❤️ para exploradores de IA</p>
            </div>
        </div>
    </div>

    <script>
        // ==================== DATOS DE APLICACIONES ====================
        const aplicaciones = [
            {
                id: 1,
                titulo: "Conversión de Texto a Voz",
                descripcion: "Transforma textos en audio de alta calidad usando IA avanzada",
                categoria: "audio",
                imagen: "https://via.placeholder.com/300x200?text=Texto+a+Voz&bg=667eea&textColor=fff",
                enlace: "https://imultimod.streamlit.app/",
                nuevo: true,
                borderClass: "card-border-1"
            },
            {
                id: 2,
                titulo: "Conversión de Voz a Texto",
                descripcion: "Convierte audio en texto con precisión y en tiempo real",
                categoria: "audio",
                imagen: "https://via.placeholder.com/300x200?text=Voz+a+Texto&bg=764ba2&textColor=fff",
                enlace: "https://traductorw.streamlit.app/",
                nuevo: false,
                borderClass: "card-border-2"
            },
            {
                id: 3,
                titulo: "Reconocimiento de Objetos",
                descripcion: "Detecta y clasifica objetos en imágenes usando YOLO",
                categoria: "vision",
                imagen: "https://via.placeholder.com/300x200?text=Detección+Objetos&bg=667eea&textColor=fff",
                enlace: "https://yolov5cmc.streamlit.app/",
                nuevo: false,
                borderClass: "card-border-3"
            },
            {
                id: 4,
                titulo: "Análisis de Imagen",
                descripcion: "Análisis visual avanzado con modelos de visión IA",
                categoria: "vision",
                imagen: "https://via.placeholder.com/300x200?text=Análisis+Imagen&bg=764ba2&textColor=fff",
                enlace: "https://vision2-gpt4o.streamlit.app/",
                nuevo: true,
                borderClass: "card-border-4"
            },
            {
                id: 5,
                titulo: "Generación en Contexto (RAG)",
                descripcion: "Analiza documentos PDF y responde preguntas inteligentes",
                categoria: "nlp",
                imagen: "https://via.placeholder.com/300x200?text=RAG&bg=667eea&textColor=fff",
                enlace: "https://chatpdf-cc.streamlit.app/",
                nuevo: false,
                borderClass: "card-border-1"
            },
            {
                id: 6,
                titulo: "Análisis de Datos",
                descripcion: "Análisis inteligente de datos con agentes de IA",
                categoria: "datos",
                imagen: "https://via.placeholder.com/300x200?text=Análisis+Datos&bg=764ba2&textColor=fff",
                enlace: "https://dataagente.streamlit.app/",
                nuevo: false,
                borderClass: "card-border-2"
            },
            {
                id: 7,
                titulo: "Transcriptor Audio y Video",
                descripcion: "Transcribe automáticamente audio y video a texto",
                categoria: "audio",
                imagen: "https://via.placeholder.com/300x200?text=Transcriptor&bg=667eea&textColor=fff",
                enlace: "https://transcript-whisper.streamlit.app/",
                nuevo: true,
                borderClass: "card-border-3"
            },
            {
                id: 8,
                titulo: "Entrenando Modelos",
                descripcion: "Aprende a entrenar y usar tus propios modelos de IA",
                categoria: "datos",
                imagen: "https://via.placeholder.com/300x200?text=Modelos&bg=764ba2&textColor=fff",
                enlace: "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
                nuevo: false,
                borderClass: "card-border-4"
            },
            {
                id: 9,
                titulo: "Sistema Ciberfísico",
                descripcion: "Interacción inteligente con el mundo físico",
                categoria: "vision",
                imagen: "https://via.placeholder.com/300x200?text=Ciberfísico&bg=667eea&textColor=fff",
                enlace: "https://vision2-gpt4o.streamlit.app/",
                nuevo: true,
                borderClass: "card-border-1"
            },
            {
                id: 10,
                titulo: "Aplicación 10",
                descripcion: "Descripción de la aplicación 10",
                categoria: "datos",
                imagen: "https://via.placeholder.com/300x200?text=App+10&bg=764ba2&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-2"
            },
            {
                id: 11,
                titulo: "Aplicación 11",
                descripcion: "Descripción de la aplicación 11",
                categoria: "audio",
                imagen: "https://via.placeholder.com/300x200?text=App+11&bg=667eea&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-3"
            },
            {
                id: 12,
                titulo: "Aplicación 12",
                descripcion: "Descripción de la aplicación 12",
                categoria: "vision",
                imagen: "https://via.placeholder.com/300x200?text=App+12&bg=764ba2&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-4"
            },
            {
                id: 13,
                titulo: "Aplicación 13",
                descripcion: "Descripción de la aplicación 13",
                categoria: "nlp",
                imagen: "https://via.placeholder.com/300x200?text=App+13&bg=667eea&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-1"
            },
            {
                id: 14,
                titulo: "Aplicación 14",
                descripcion: "Descripción de la aplicación 14",
                categoria: "datos",
                imagen: "https://via.placeholder.com/300x200?text=App+14&bg=764ba2&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-2"
            },
            {
                id: 15,
                titulo: "Aplicación 15",
                descripcion: "Descripción de la aplicación 15",
                categoria: "audio",
                imagen: "https://via.placeholder.com/300x200?text=App+15&bg=667eea&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-3"
            },
            {
                id: 16,
                titulo: "Aplicación 16",
                descripcion: "Descripción de la aplicación 16",
                categoria: "vision",
                imagen: "https://via.placeholder.com/300x200?text=App+16&bg=764ba2&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-4"
            },
            {
                id: 17,
                titulo: "Aplicación 17",
                descripcion: "Descripción de la aplicación 17",
                categoria: "nlp",
                imagen: "https://via.placeholder.com/300x200?text=App+17&bg=667eea&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-1"
            },
            {
                id: 18,
                titulo: "Aplicación 18",
                descripcion: "Descripción de la aplicación 18",
                categoria: "datos",
                imagen: "https://via.placeholder.com/300x200?text=App+18&bg=764ba2&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-2"
            },
            {
                id: 19,
                titulo: "Aplicación 19",
                descripcion: "Descripción de la aplicación 19",
                categoria: "audio",
                imagen: "https://via.placeholder.com/300x200?text=App+19&bg=667eea&textColor=fff",
                enlace: "#",
                nuevo: false,
                borderClass: "card-border-3"
            },
            {
                id: 20,
                titulo: "Aplicación 20",
                descripcion: "Descripción de la aplicación 20",
                categoria: "vision",
                imagen: "https://via.placeholder.com/300x200?text=App+20&bg=764ba2&textColor=fff",
                enlace: "#",
                nuevo: true,
                borderClass: "card-border-4"
            }
        ];

        // ==================== FUNCIÓN PARA RENDERIZAR CARDS ====================
        function renderCards(filter = 'todos', search = '') {
            const cardsGrid = document.getElementById('cardsGrid');
            cardsGrid.innerHTML = '';

            const filtered = aplicaciones.filter(app => {
                const matchFilter = filter === 'todos' || app.categoria === filter;
                const matchSearch = app.titulo.toLowerCase().includes(search.toLowerCase()) ||
                                  app.descripcion.toLowerCase().includes(search.toLowerCase());
                return matchFilter && matchSearch;
            });

            filtered.forEach(app => {
                const card = document.createElement('div');
                card.className = `card ${app.borderClass}`;
                card.innerHTML = `
                    <div class="card-image-container">
                        <img src="${app.imagen}" alt="${app.titulo}" class="card-image">
                        <div class="card-image-overlay"></div>
                        ${app.nuevo ? '<span class="badge-new">NUEVO</span>' : ''}
                    </div>
                    <div class="card-content">
                        <span class="card-category">${app.categoria.toUpperCase()}</span>
                        <h3 class="card-title">${app.titulo}</h3>
                        <p class="card-description">${app.descripcion}</p>
                        <div class="card-footer">
                            <a href="${app.enlace}" target="_blank" class="btn btn-primary">
                                🔗 Acceder
                            </a>
                        </div>
                    </div>
                `;
                cardsGrid.appendChild(card);
            });

            if (filtered.length === 0) {
                cardsGrid.innerHTML = '<p style="text-align: center; color: #666; font-size: 1.2em; grid-column: 1/-1;">No se encontraron resultados</p>';
            }
        }

        // ==================== EVENT LISTENERS PARA FILTROS ====================
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                renderCards(btn.getAttribute('data-filter'), document.getElementById('searchInput').value);
            });
        });

        // ==================== EVENT LISTENER PARA BÚSQUEDA ====================
        document.getElementById('searchInput').addEventListener('input', (e) => {
            const activeFilter = document.querySelector('.filter-btn.active').getAttribute('data-filter');
            renderCards(activeFilter, e.target.value);
        });

        // ==================== RENDERIZAR CARDS AL CARGAR ====================
        renderCards();
    </script>
</body>
</html>
