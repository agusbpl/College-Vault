# 📂 Tecnologías para la Gestión

## 👨‍🏫 Cátedra y Contacto
- **Profesor**: Por definir
- **Plataforma**: Aula virtual

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
FROM "10 Asignaturas/Tecnologías para la Gestión"
WHERE file.name != "Tecnologías para la Gestión" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

## 🎯 Tareas y Entregas
*No hay tareas pendientes*

## 📝 Requisitos de Evaluación
- **Aprobación de la materia**: 
  - **Parciales**: Evaluaciones parciales de carácter teórico-práctico (con recuperatorio integrador).
  - **Trabajo Integrador Final**: Presentación y exposición de un proyecto grupal final.
- **Régimen de Aprobación**:
  - **Promoción Directa**: Calificación final $\ge 7$.
  - **Examen Final**: Calificación entre $4$ y $6$.
  - **Desaprobado**: Calificación $< 4$.

## 📅 Unidades del Programa
- **Unidad 1**: Introducción a las Tecnologías de Información en la Gestión Organizacional (ventajas competitivas, transformación digital).
- **Unidad 2**: Sistemas de Información y su Rol Gerencial (sistemas transaccionales, DSS, EIS, MIS, arquitectura digital).
- **Unidad 3**: Sistemas ERP (Enterprise Resource Planning, características, módulos, mapa de soluciones, desafíos de implementación).
- **Unidad 4**: Gestión de Clientes y Cadena de Suministro (Ecommerce, CRM, SCM, integración 360°).
- **Unidad 5**: Inteligencia de Negocios y Toma de Decisiones Basada en Datos (BI, Analytics, Data Warehouses, dashboards, KPIs).
- **Unidad 6**: Automatización de Procesos e Inteligencia Artificial en la Gestión (RPA, IA aplicada a la gestión).
- **Unidad 7**: Tecnologías Digitales Emergentes (Big Data, IoT, Cloud Computing, Blockchain).
- **Unidad 8**: Estrategia de Transformación Digital y Gestión del Cambio (redefinición de modelos de negocio, empresas data-driven).
- **Unidad 9**: Selección e Implementación de Tecnologías (a medida vs. estándar, on-premise vs. nube, criterios de selección).
- **Unidad 10**: Evaluación de Proyectos Tecnológicos y Factores de Éxito (viabilidad, ROI, indicadores post-implementación).

---
[[Estudios Index|Volver al Índice General]]
