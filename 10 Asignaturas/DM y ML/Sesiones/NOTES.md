# Working Notes: Minería y ML

## Flow Activo
- Modalidad: Sistema "Learn" Integral (Clases 1 a 5) con desglose paso a paso de fórmulas, analogías, videos embebidos de YouTube, simuladores JS interactivos, laboratorios de código locales y notebooks de Google Colab.
- Estado actual:
  - [x] **Clase 1: Introducción a la IA & Machine Learning**: Completada por el alumno (`lessons/0003-clase1-fundamentos-ia-ml.html`, `practica_clase1.py`, `Clase1_Learn_Practica.ipynb`).
  - [x] **Clase 2: MD, Preprocesamiento & KNN (Titanic)**: Lección HTML interactiva (`lessons/0004-clase2-eda-preprocesamiento-knn.html`), script de validación local (`practica_clase2.py`) y notebook (`Clase2_Learn_Practica.ipynb`). EN CURSO.
  - [x] **Clase 3: Árboles de Decisión (ID3, CART, Entropía, Gini)**: Lección HTML interactiva (`lessons/0005-clase3-arboles-decision-gini-entropy.html`) con audio neural ElenaNeural, simulador de pureza Gini/Entropía, resolución de Actividades 1 a 8 y drawer lateral de notas.
  - [x] **Master Notebook Integral (Clases 1 a 5)**: Cuaderno unificado (`Master_DM_ML_Clases_1_a_5.ipynb`) con desglose exhaustivo de fórmulas en LaTeX, implementaciones vectorizadas manuales en NumPy y pipelines completos en Scikit-Learn.
  - [ ] **Clase 4: Métricas de Evaluación & Ensambles**: Pendiente lección HTML interactiva.
  - [ ] **Clase 5: Balance de Clases, Feature Selection & Sistemas de Recomendación**: Pendiente lección HTML interactiva (material cacheado).

## Preferencias del Estudiante
- Explicaciones con desglose analítico de cada variable y operador matemático.
- Intercalación constante: Teoría formal &rarr; Analogía intuitiva &rarr; Video &rarr; Simulador interactivo &rarr; Mini-ejercicio en código &rarr; Ejercicios oficiales de la cátedra.
- Validación de código local con terminal (`practica_claseX.py`) y Colab.
- **Embeds de YouTube**: 100% limpios y minimalistas (solo el reproductor embebido sin cabeceras superiores ni títulos/botones externos).
- **Servidor Web Local Obligatorio**: Las lecciones deben abrirse siempre a través de `http://localhost:8088/...` (`vault-server.service`) para garantizar cabeceras `Referer`/CORS válidas y evitar el *Error 153* de YouTube.
- **Audio de Lecciones Obligatorio**: Cada lección HTML debe contar con su audio en voz alta con **voz femenina** (`es-AR-ElenaNeural`) y el reproductor (`#audio-studio-player`) embebido, con lectura literal continua de los apuntes (sin formato de podcast, a menos que se pida explícitamente).
- **Entorno de Ejecución**: Dell Celeron bajo X11/Qtile (`DISPLAY=:0`), usar `xdg-open` o `thorium-browser` acoplándose a la sesión activa (sin flags de Wayland).
- **Interactividad**: Auto-scroll con sincronización de audio (pausable con scroll manual y reanudable con botón en el player), selección de texto para agregar notas/preguntas/resaltados con persistencia local, y botón de exportación JSON de dudas acumuladas.
