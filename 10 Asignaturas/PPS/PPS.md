# 📂 PPS (Práctica Profesional Supervisada)

## 👨‍🏫 Cátedra y Contacto
- **Coordinador**: Profesor Coordinador

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

## 📝 Documentación y Registro
```dataview
TABLE fecha as Fecha, estado as Estado
FROM "10 Asignaturas/PPS"
WHERE file.name != "PPS" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

- [ ] Definir tema/proyecto de PPS
- [ ] Contactar con el tutor/coordinador

## 📝 Reglamento y Requisitos Clave
- **Carga Horaria**: Mínimo de 100 horas acreditadas.
- **Duración Máxima**: 6 meses continuos desde el inicio.
- **Actores**: Estudiante, Profesor Coordinador (PC) y Tutor de la Entidad (TE).
- **Entregables Obligatorios**:
  1. **Formulario de Propuesta**: Para asentar la solicitud con el Plan de Trabajo.
  2. **Informe Técnico Final**: 5 a 10 páginas describiendo tareas, metodologías, resultados y reflexión final.
  3. **Informe del Tutor de la Entidad**: Cuestionario final evaluando desempeño.

---
[[Estudios Index|Volver al Índice General]]
