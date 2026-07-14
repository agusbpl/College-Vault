# 📅 Dashboard de Organización

## 📋 Tareas Pendientes
```dataview
TASK
WHERE !completed AND file.folder != "30 Plantillas" AND text != "" AND text != " "
```

## 📝 Próximos Exámenes y Entregas
| Asignatura         | Fecha  | Tipo (Examen/Proyecto)             | Estado    |
| ------------------ | ------ | ---------------------------------- | --------- |
| **Bases de Datos** | 01-oct | Definición de Trabajo Experimental | Pendiente |
| **Bases de Datos** | 22-oct | Entrega de Trabajo Experimental    | Pendiente |
| **Bases de Datos** | 05-nov | Defensa de Trabajo Experimental    | Pendiente |
| **Minería y ML**   | 04-nov | 1ra. Fecha de Examen Escrito       | Pendiente |
| **Visualización**  | 04-nov | 1ra. Fecha de Examen Escrito       | Pendiente |
| **Minería y ML**   | 18-nov | 2da. Fecha de Examen Escrito       | Pendiente |
| **Visualización**  | 18-nov | 2da. Fecha de Examen Escrito       | Pendiente |
| **Minería y ML**   | 02-dic | 3ra. Fecha de Examen Escrito       | Pendiente |
| **Visualización**  | 02-dic | 3ra. Fecha de Examen Escrito       | Pendiente |

## 🏫 Horario de Clases
| Hora | Lunes | Martes | Miércoles | Jueves | Viernes |
| ---- | ----- | ------ | --------- | ------ | ------- |
|      |       |        |           |        |         |

## 📝 Notas Recientes de Clase
```dataview
TABLE materia as Materia, fecha as Fecha, estado as Estado
FROM "10 Asignaturas"
WHERE file.name != "Bases de Datos" AND file.name != "Minería y ML" AND file.name != "Tecnologías para la Gestión" AND file.name != "Visualización" AND file.name != "PPS"
SORT file.mtime DESC
LIMIT 5
```

## 👨‍🏫 Contactos de Cátedras
| Cátedra                                         | Profesor(es)                              | Medio                                                                 | Sitio        |
| :---------------------------------------------- | :---------------------------------------- | :-------------------------------------------------------------------- | :----------- |
| **Base de Datos**                               | Esp. Luciano Marrero                      | lmarrero@lidi.info.unlp.edu.ar                                        | IDEAS        |
| **Minería de Datos y Aprendizaje Automático**   | Dr. Franco Ronchetti y Dr. Waldo Hasperué | fronchetti@lidi.info.unlp.edu.ar <br> whasperue@lidi.info.unlp.edu.ar | Moodle       |
| **Tecnologías para la Gestión**                 | -                                         | -                                                                     | Aula virtual |
| **Visualización de Grandes Volúmenes de Datos** | Esp. César Estrebou                       | cesarest@lidi.info.unlp.edu.ar                                        | Moodle       |
| **PPS (Práctica Profesional Supervisada)**      | Profesor Coordinador                      | -                                                                     | -            |

---
[[Estudios Index|Volver al Índice General]]
