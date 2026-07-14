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

---
[[Estudios Index|Volver al Índice General]]
