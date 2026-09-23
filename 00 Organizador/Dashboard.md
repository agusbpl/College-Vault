# 📅 Dashboard de Organización

## 📋 Tareas Pendientes
```dataview
TASK
WHERE !completed AND file.folder != "30 Plantillas" AND text != "" AND text != " "
```

## 📝 Próximos Exámenes y Entregas
| Asignatura                      | Fecha  | Tipo (Examen/Proyecto)             | Estado    |
| :------------------------------ | :----- | :--------------------------------- | :-------- |
| **Bases de Datos**              | 01-oct | Definición de Trabajo Experimental | Pendiente |
| **Tecnologías para la Gestión** | 01-oct | TPI - Entrega 4 (Evaluación y Selección ERP) | Pendiente |
| **Tecnologías para la Gestión** | 06-oct | Entrega Trabajo de Investigación Teórico (Mercado ERP) | Pendiente |
| **Tecnologías para la Gestión** | 08-oct | TPI - Entrega 5 (CRM + Ecommerce)  | Pendiente |
| **Tecnologías para la Gestión** | 15-oct | TPI - Entrega 6 (Business Intelligence - Cierre B2) | Pendiente |
| **Tecnologías para la Gestión** | 20-oct | 1º Parcial Teórico                 | Pendiente |
| **Bases de Datos**              | 22-oct | Entrega de Trabajo Experimental    | Pendiente |
| **Tecnologías para la Gestión** | 05-nov | TPI - Entrega 7 (IA y Automatización / RPA) | Pendiente |
| **Minería y ML**                | 04-nov | 1ra. Fecha de Examen Escrito       | Pendiente |
| **Visualización**               | 04-nov | 1ra. Fecha de Examen Escrito       | Pendiente |
| **Bases de Datos**              | 05-nov | Defensa de Trabajo Experimental    | Pendiente |
| **Tecnologías para la Gestión** | 12-nov | TPI - Entrega 8 (Roadmap, Riesgos y ROI - Cierre B3) | Pendiente |
| **Minería y ML**                | 18-nov | 2da. Fecha de Examen Escrito       | Pendiente |
| **Visualización**               | 18-nov | 2da. Fecha de Examen Escrito       | Pendiente |
| **Tecnologías para la Gestión** | 01-dic | 2º Parcial Teórico                 | Pendiente |
| **Minería y ML**                | 02-dic | 3ra. Fecha de Examen Escrito       | Pendiente |
| **Visualización**               | 02-dic | 3ra. Fecha de Examen Escrito       | Pendiente |
| **Tecnologías para la Gestión** | 03-dic | Presentación Final TPI (Grupo 1)   | Pendiente |
| **Tecnologías para la Gestión** | 10-dic | Presentación Final TPI (Grupo 2)   | Pendiente |
| **Tecnologías para la Gestión** | 16-dic | Recuperatorio General Teórico      | Pendiente |

## 🏫 Horario de Clases Semanal

|      Horario      | Lunes |                         Martes                         |                                     Miércoles                                      |                           Jueves                           |                       Viernes                        |
| :---------------: | :---: | :----------------------------------------------------: | :--------------------------------------------------------------------------------: | :--------------------------------------------------------: | :--------------------------------------------------: |
| **10:00 - 13:00** |   —   |                           —                            |           🗄️ **Bases de Datos (Teoría)**<br>*(Aula Android, Ed. CIyTT)*            |                             —                              |                          —                           |
| **13:00 - 16:00** |   —   |                           —                            |                                         —                                          |                             —                              | 🤖 **Minería de Datos y ML (Teoría)**<br>*(Aula 14)* |
| **14:00 - 16:30** |   —   |                           —                            | 📊 **Visualización Big Data (Teórico-Práctica)**<br>*(Aula 9 - 14:00 a 16:30 hs)* |                             —                              |                          —                           |
| **18:00 - 19:00** |   —   |                           —                            |                                         —                                          | 🗄️ **Bases de Datos (Práctica)**<br>*(Aula 9 - 18:00 hs)* |                          —                           |
| **19:00 - 22:00** |   —   |      🏢 **Tecnologías para la Gestión (Teoría)**       |                                         —                                          |       🏢 **Tecnologías para la Gestión (Práctica)**        |                          —                           |

## 📝 Notas Recientes de Clase
```dataview
TABLE materia as Materia, fecha as Fecha, estado as Estado
FROM "10 Asignaturas"
WHERE file.name != "Bases de Datos" AND file.name != "Minería y ML" AND file.name != "Tecnologías para la Gestión" AND file.name != "Visualización" AND file.name != "PPS" AND file.name != "Programa y Bibliografía" AND file.name != "TPI - Trabajo Práctico Integrador"
SORT file.mtime DESC
LIMIT 5
```

## 👨‍🏫 Contactos de Cátedras
| Cátedra | Profesor(es) | Medio | Sitio |
| :--- | :--- | :--- | :--- |
| **Base de Datos** | Esp. Luciano Marrero | lmarrero@lidi.info.unlp.edu.ar | IDEAS |
| **Minería de Datos y Aprendizaje Automático** | Dr. Franco Ronchetti y Dr. Waldo Hasperué | fronchetti@lidi.info.unlp.edu.ar <br> whasperue@lidi.info.unlp.edu.ar | Moodle |
| **Tecnologías para la Gestión** | Diego Erben (Teoría) <br> Francisco Rubio (Práctica) | `rubiofa@gmail.com` <br> WhatsApp: `+54 9 11 3195 8424` | Aula Virtual |
| **Visualización de Grandes Volúmenes de Datos** | Esp. César Estrebou | cesarest@lidi.info.unlp.edu.ar | [Moodle de Asignaturas](https://asignaturas.info.unlp.edu.ar/) |
| **PPS (Práctica Profesional Supervisada)** | Profesor Coordinador | - | - |

---
📖 **[[00 Organizador/Compendio de Cátedras - Segundo Cuatrimestre|Ver Compendio Integral de Cátedras]]** | [[Estudios Index|Volver al Índice General]]
