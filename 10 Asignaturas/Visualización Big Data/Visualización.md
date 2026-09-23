# 📂 Visualización de Grandes Volúmenes de Datos

## 👨‍🏫 Cátedra, Horarios y Contacto
- **Profesor Responsable**: Esp. César Estrebou
- **Email**: cesarest@lidi.info.unlp.edu.ar
- **Plataforma**: [Moodle de Asignaturas](https://asignaturas.info.unlp.edu.ar/)
- **Horarios de Cursada**:
  - 📖💻 **Clases Teórico-Prácticas**: Miércoles de 14:00 a 16:30 hs (Aula 9).
- **Asistencia**: No se requiere asistencia obligatoria.

---

## 📚 Recursos y Bibliografía
```dataviewjs
const folderPath = dv.current().file.folder + "/Recursos";
const pdfFiles = app.vault.getFiles().filter(file => 
    file.extension === 'pdf' && 
    file.path.startsWith(folderPath)
);

if (pdfFiles.length > 0) {
    dv.list(pdfFiles.map(file => dv.fileLink(file.path)));
} else {
    dv.paragraph("*No hay libros cargados en la carpeta de Recursos.*");
}
```

### 📖 Bibliografía de la Cátedra
- **Básica**:
  - Cairo, A. (2016). [[The Truthful Art - Alberto Cairo.pdf|The Truthful Art: Data, Charts, and Maps for Communication]]. New Riders.
  - Cairo, A. (2019). [[How Charts Lie - Alberto Cairo.pdf|How Charts Lie: Getting Smarter about Visual Information]]. W. W. Norton.
  - Healy, K. (2018). [[Data Visualization - A Practical Introduction - Kieran Healy.pdf|Data Visualization: A Practical Introduction]]. Princeton University Press.
  - Kirk, A. (2023). *Data Visualisation: A Handbook for Data Driven Design* (3ra Ed.). Sage.
  - Ware, C. (2020). *Information Visualization: Perception for Design* (4ta Ed.). Morgan Kaufmann.
  - Fisher, D. y Meyer, M. (2018). *Making Data Visual: A Practical Guide to Using Visualization for Insight*. O'Reilly.
- **Complementaria**:
  - Munzner, T. (2014). *Visualization Analysis and Design*. CRC Press.
  - Tominski, C. y Schumann, H. (2020). *Interactive Visual Data Analysis*. CRC Press.
  - Knaflic, C. N. (2015). *Storytelling with Data*. Wiley.
  - Wilke, C. (2019). *Fundamentals of Data Visualization*. O'Reilly.
  - Wexler, S., Shaffer, J. y Cotgreave, A. (2017). *The Big Book of Dashboards*. Wiley.
  - Few, S. (2013). *Information Dashboard Design*. Analytics Press.
  - Bertin, J. (2010). *Semiology of Graphics*. ESRI Press.
  - Murray, S. (2017). *Interactive Data Visualization for the Web*. O'Reilly.

---

## 📝 Apuntes y Notas de Clase
```dataview
TABLE fecha as Fecha, estado as Estado, tags as Tags
FROM "10 Asignaturas/Visualización Big Data"
WHERE file.name != "Visualización" AND !contains(file.path, "Recursos") AND file.extension = "md"
SORT file.name ASC
```

---

## 🎯 Tareas y Entregas
- [ ] Completar Práctica 1 y repaso interactivo de fundamentos visuales en /teach 📅 2026-09-23 #visualizacion

---

## 📝 Requisitos de Evaluación y Modalidad de Aprobación

- **Estructura de Evaluación**:
  1. **Trabajo Práctico Integrador Grupal**: Grupos de **3 personas estrictamente** (*"ni más ni menos"*). Incluye exploración de un dataset, diseño y construcción de visualizaciones interactivas/dashboards y justificación de decisiones de diseño.
  2. **Examen Conceptual Individual**: Evaluación escrita individual con **2 instancias de recuperación**.

- **Régimen de Calificación**:
  - 🏆 **Aprobación con Promoción Directa**:
    - Trabajo grupal $\ge 6$
    - Examen individual $\ge 6$
    - Nota final: promedio de ambas notas.
    - *(Quienes promocionen sin estar inscriptos bajo esa modalidad deberán anotarse en mesa de examen final para asentar la nota)*.
  - 📄 **Aprobación de Cursada (Regular)**:
    - Trabajo grupal $\ge 5$
    - Examen individual $\ge 5$
    - Deberán rendir examen final tradicional.

---

## 📋 Programa Analítico de la Asignatura

- **Unidad 1. Introducción a la Visualización de Datos**: Conceptos fundamentales. Visualización para exploración, análisis y comunicación. Visualización científica vs. de información. Hitos históricos.
- **Unidad 2. Percepción y Cognición Visual**: Procesamiento preatencional. Principios gestálticos. Variables visuales. Codificación visual y uso efectivo del color. Limitaciones perceptuales.
- **Unidad 3. El Proceso de Visualización**: Pipeline de visualización. Transformación de datos. Relación datos-representación-interacción. Tareas de análisis visual.
- **Unidad 4. Técnicas de Visualización de Datos**: Datos tabulares, univariados y multivariados. Histogramas, boxplots, scatter plots, mapas de calor, coordenadas paralelas. Reducción de dimensionalidad.
- **Unidad 5. Visualización de Datos Especializados**: Series temporales. Datos geoespaciales y mapas temáticos. Grafos, redes y árboles. Visualización de texto y documentos.
- **Unidad 6. Interacción y Análisis Visual**: Filtrado, selección, navegación, zoom y detalles bajo demanda (*details-on-demand*). Visualizaciones coordinadas (*multiple coordinated views*).
- **Unidad 7. Diseño de Visualizaciones y Comunicación**: Proceso de diseño y evaluación. Accesibilidad y diseño inclusivo. Storytelling con datos. Detección y corrección de errores comunes. Dashboards.
- **Unidad 8. Herramientas y Aplicaciones**: Herramientas modernas de visualización, tableros interactivos e integración con flujos de análisis de datos.
- **Unidad 9. Visualización de Grandes Volúmenes de Datos (Big Data)**: Desafíos de volumen, velocidad y variedad. Escalabilidad, sobrecarga visual y oclusión. Técnicas de agregación, muestreo, densidades y visualización progresiva.

---

## 📅 Cronograma y Hoja de Ruta (Segundo Cuatrimestre 2026)

| Semana | Fecha | Contenidos / Actividades | Estado |
| :---: | :---: | :--- | :---: |
| 1 | 26-ago | [[10 Asignaturas/Visualización Big Data/26-08-2026 Clase 1 - Introducción a la Visualización de Datos\|Clase 1: Introducción a la Visualización de Datos]]. Objetivos, aplicaciones y áreas. Exploración, análisis y comunicación. | ✅ Dictada |
| 2 | 02-sep | Percepción y cognición visual. Procesamiento preatencional. Principios gestálticos. Variables visuales. Uso efectivo del color. | ⏳ Próxima |
| 3 | 09-sep | El proceso de visualización. Pipeline de visualización. Transformación de datos. Relación entre datos, representación e interacción. | ⏳ Pendiente |
| 4 | 16-sep | Técnicas de visualización para datos tabulares. Comparación, distribución y correlación. Histogramas, boxplots y diagramas de dispersión. | ⏳ Pendiente |
| 5 | 23-sep | Visualización de datos multidimensionales. Mapas de calor. Coordenadas paralelas. Reducción de dimensionalidad para visualización. | ⏳ Pendiente |
| 6 | 30-sep | Visualización de datos temporales. Series de tiempo. Tendencias, estacionalidad y eventos. | ⏳ Pendiente |
| 7 | 07-oct | Visualización de datos geoespaciales. Mapas temáticos. Introducción a la visualización de redes y grafos. | ⏳ Pendiente |
| 8 | 14-oct | Interacción y análisis visual. Filtrado, selección, navegación, zoom y detalles bajo demanda. Visualizaciones coordinadas. | ⏳ Pendiente |
| 9 | 21-oct | Diseño y evaluación de visualizaciones. Storytelling con datos. Dashboards y comunicación efectiva de resultados. | ⏳ Pendiente |
| 10 | 28-oct | Visualización de grandes volúmenes de datos. Escalabilidad, agregación, muestreo, representación de densidades y visualización progresiva. | ⏳ Pendiente |
| 11 | 04-nov | 📝 **1ra. Fecha de Examen Escrito Individual** | 🔴 Examen |
| 12 | 11-nov | Consultas y muestra de exámenes (1ra. Fecha). | ⏳ Pendiente |
| 13 | 18-nov | 📝 **2da. Fecha de Examen Escrito (1er Recuperatorio)** | 🔴 Examen |
| 14 | 25-nov | Consultas y muestra de exámenes (2da. Fecha). | ⏳ Pendiente |
| 15 | 02-dic | 📝 **3ra. Fecha de Examen Escrito (2do Recuperatorio)** | 🔴 Examen |
| 16 | 09-dic | Muestra final de exámenes (3ra. Fecha). | ⏳ Pendiente |

---
[[Estudios Index|Volver al Índice General]]
