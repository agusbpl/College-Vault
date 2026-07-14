# 📂 Visualización

## 👨‍🏫 Cátedra y Contacto
- **Profesor**: Esp. César Estrebou
- **Email**: cesarest@lidi.info.unlp.edu.ar
- **Plataforma**: Moodle

## 📚 Recursos
```dataviewjs
const folderPath = dv.current().file.folder + "/Recursos";
const pdfFiles = app.vault.getFiles().filter(file => 
    file.extension === 'pdf' && 
    file.path.startsWith(folderPath)
);

if (pdfFiles.length > 0) {
    dv.list(pdfFiles.map(file => dv.fileLink(file.path)));
} else {
    dv.paragraph("*No hay libros ni filminas cargados en la carpeta de Recursos.*");
}
```

## 📝 Apuntes y Notas de Clase
```dataview
TABLE fecha as Fecha, estado as Estado
FROM "10 Asignaturas/Visualización"
WHERE file.name != "Visualización" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

## 🎯 Tareas y Entregas
*No hay tareas pendientes*

## 📝 Requisitos de Evaluación
- **Aprobación de la materia**:
  1. Aprobar las actividades prácticas obligatorias definidas por la cátedra.
  2. Aprobar un trabajo práctico integrador grupal (exploración, diseño, construcción de visualizaciones y justificación de decisiones).
  3. Aprobar una instancia de evaluación individual escrita sobre contenidos conceptuales.

## 📅 Cronograma y Hoja de Ruta
| Semana | Fecha | Contenidos / Actividades |
| ------ | ----- | ------------------------ |
| 1 | 26-ago | Introducción a la Visualización de Datos. Objetivos, aplicaciones y áreas. Visualización para exploración, análisis y comunicación. |
| 2 | 02-sep | Percepción y cognición visual. Procesamiento preatencional. Principios gestálticos. Variables visuales. Uso efectivo del color. |
| 3 | 09-sep | El proceso de visualización. Pipeline de visualización. Transformación de datos. Relación entre datos, representación e interacción. |
| 4 | 16-sep | Técnicas de visualización para datos tabulares. Comparación, distribución y correlación. Histogramas, boxplots y diagramas de dispersión. |
| 5 | 23-sep | Visualización de datos multidimensionales. Mapas de calor. Coordenadas paralelas. Reducción de dimensionalidad para visualización. |
| 6 | 30-sep | Visualización de datos temporales. Series de tiempo. Tendencias, estacionalidad y eventos. |
| 7 | 07-oct | Visualización de datos geoespaciales. Mapas temáticos. Introducción a la visualización de redes y grafos. |
| 8 | 14-oct | Interacción y análisis visual. Filtrado, selección, navegación, zoom y detalles bajo demanda. Visualizaciones coordinadas. |
| 9 | 21-oct | Diseño y evaluación de visualizaciones. Storytelling con datos. Dashboards y comunicación efectiva de resultados. |
| 10 | 28-oct | Visualización de grandes volúmenes de datos. Escalabilidad, agregación, muestreo, representación de densidades y visualización progresiva. |
| 11 | 04-nov | **1ra. Fecha de Examen Escrito** |
| 12 | 11-nov | Consultas y muestra de exámenes (1ra. Fecha). |
| 13 | 18-nov | **2da. Fecha de Examen Escrito (Recuperatorio)** |
| 14 | 25-nov | Consultas y muestra de exámenes (2da. Fecha). |
| 15 | 02-dic | **3ra. Fecha de Examen Escrito (Recuperatorio)** |
| 16 | 09-dic | Muestra de exámenes (3ra. Fecha). |

---
[[Estudios Index|Volver al Índice General]]
