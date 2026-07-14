# 📂 Minería y ML

## 👨‍🏫 Cátedra y Contacto
- **Profesores**: Dr. Franco Ronchetti y Dr. Waldo Hasperué
- **Emails**: fronchetti@lidi.info.unlp.edu.ar / whasperue@lidi.info.unlp.edu.ar
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
FROM "10 Asignaturas/Minería y ML"
WHERE file.name != "Minería y ML" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

## 🎯 Tareas y Entregas
*No hay tareas pendientes*

---
[[Estudios Index|Volver al Índice General]]
