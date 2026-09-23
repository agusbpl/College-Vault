# 📂 Minería y ML

## 👨‍🏫 Cátedra, Horarios y Contacto
- **Profesores**: Dr. Franco Ronchetti y Dr. Waldo Hasperué
- **Emails**: `fronchetti@lidi.info.unlp.edu.ar` / `whasperue@lidi.info.unlp.edu.ar`
- **Plataforma**: Moodle
- **Horarios de Cursada**:
  - 📖 **Teoría**: Viernes a partir de las 13:00 hs (Aula 14)

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
FROM "10 Asignaturas/Minería y ML"
WHERE file.name != "Minería y ML" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

## 🎯 Tareas y Entregas
- [x] Completar y validar actividades 1 a 8 de Árboles de Decisión (Clase 3) #dm-y-ml 📅 2026-09-14
- [ ] Definir grupo y propuesta de tema para el Trabajo Grupal de Extracción de Conocimiento #dm-y-ml
- [ ] Repasar Clases 1 a 3 (CRISP-DM, KNN, Métricas y Árboles) 📅 2026-09-18 #dm-y-ml
- [ ] Resolver práctica interactiva de KNN y Árboles de Decisión en /teach con evaluator loop 📅 2026-09-23 #dm-y-ml

## 📝 Requisitos de Evaluación
- **Aprobación de la materia**:
  1. Entregar y aprobar con nota $\ge 6$ un trabajo práctico integrador grupal (preparación de datos, modelos, evaluación e interpretación).
  2. Aprobar con nota $\ge 6$ un examen escrito individual (cuenta con 2 instancias de recuperación).
- **Promoción**: Promedio de ambas notas.

## 📅 Cronograma y Hoja de Ruta
| Semana | Fecha | Contenidos / Actividades |
| ------ | ----- | ------------------------ |
| 1 | 26-ago | Introducción a la IA. Metodologías (Crisp-DM / KDD). Aprendizaje supervisado y no supervisado. |
| 2 | 02-sep | Evaluación de modelos. Preparación de los datos (limpieza, transformación, valores faltantes, normalización). |
| 3 | 09-sep | Árboles de decisión (algoritmos ID3, C4.5, CART, entropía, ganancia de información, Gini, poda y sobreajuste). |
| 4 | 16-sep | Ensambles (Bagging, Random Forest, Boosting). |
| 5 | 23-sep | Técnicas de Machine Learning: extracción de características, balance de clases y sistemas de recomendación. |
| 6 | 30-sep | Aprendizaje No Supervisado. K-means, Silhouette, DBSCAN. Reducción de dimensionalidad (PCA y t-SNE). |
| 7 | 07-oct | Redes neuronales artificiales. Regresión lineal, regresión logística. Perceptrón multicapa y backpropagation. |
| 8 | 14-oct | Redes neuronales: segunda parte. Métricas de clasificación y regresión. |
| 9 | 21-oct | Deep Learning. Redes Neuronales Convolucionales (CNN) y recurrentes (RNN). Visión por computadora y NLP. |
| 10 | 28-oct | Deep Learning: segunda parte. Autoencoders. Transformers. NLP. Modelos Generativos. |
| 11 | 04-nov | **1ra. Fecha de Examen Escrito** |
| 12 | 11-nov | Consultas y muestra de exámenes (1ra. Fecha). |
| 13 | 18-nov | **2da. Fecha de Examen Escrito (Recuperatorio)** |
| 14 | 25-nov | Consultas y muestra de exámenes (2da. Fecha). |
| 15 | 02-dic | **3ra. Fecha de Examen Escrito (Recuperatorio)** |
| 16 | 09-dic | Muestra de exámenes (3ra. Fecha). |

---
[[Estudios Index|Volver al Índice General]]
