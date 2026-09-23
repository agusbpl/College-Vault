# 📂 Bases de Datos

## 👨‍🏫 Cátedra, Horarios y Contacto
- **Profesor**: Esp. Luciano Marrero
- **Email**: `lmarrero@lidi.info.unlp.edu.ar`
- **Plataforma**: IDEAS
- **Horarios de Cursada**:
  - 📖 **Teoría**: Miércoles de 10:00 a 13:00 hs (Aula Android, Ed. CIyTT)
  - 💻 **Práctica**: Jueves a las 18:00 hs (Aula 9)

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
FROM "10 Asignaturas/Bases de Datos"
WHERE file.name != "Bases de Datos" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

## 🎯 Tareas y Entregas
- [ ] Resolver práctica de normalización (1FN, 2FN, 3FN) y NoSQL (Mongo/Redis) en /teach con evaluator loop 📅 2026-09-23 #bd

## 📝 Requisitos de Evaluación
- **Modalidad**: Coloquio presencial y defensa de un trabajo práctico experimental individual o grupal sobre bases de datos NoSQL.
- **Fechas Clave**:
  - **01-oct**: Definición del trabajo experimental.
  - **22-oct**: Entrega del trabajo experimental.
  - **05-nov**: Defensa presencial y coloquio.

## 📅 Cronograma y Hoja de Ruta
| Clase | Fecha | Actividad Teórica | Actividad Práctica |
| ----- | ----- | ----------------- | ------------------ |
| 1 | Miércoles 13/08 | Bases de datos relacionales. Normalización. | Repaso de modelado de datos y consultas. |
| 2 | Miércoles 20/08 | Sin clases | Normalización |
| 3 | Miércoles 27/08 | Bases de datos NoSQL. Introducción. | Normalización |
| 4 | Miércoles 03/09 | Bases de datos NoSQL clave-valor | Práctica experimental NoSQL clave-valor |
| 5 | Miércoles 10/09 | Bases de datos NoSQL documental | Práctica experimental NoSQL documental |
| 6 | Miércoles 17/09 | Bases de datos NoSQL orientada a grafos | Práctica experimental NoSQL orientada a grafos |
| 7 | Miércoles 24/09 | Bases de datos NoSQL familia de columnas | Práctica experimental NoSQL familia de columnas |
| 8 | Lunes 01/10 | Repaso general | Definición del trabajo experimental NoSQL |
| 9 | Miércoles 08/10 | Consulta general | Consulta general |
| 10 | Miércoles 15/10 | Consulta general | Consulta general |
| 11 | Miércoles 22/10 | | Entrega del trabajo experimental (Sin clases) |
| 12 | Miércoles 05/11 | | Defensa del trabajo experimental |

---
[[Estudios Index|Volver al Índice General]]
