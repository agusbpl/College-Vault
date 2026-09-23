# 📂 Tecnologías para la Gestión

## 👨‍🏫 Cátedra, Horarios y Contacto
- **Profesor Teoría**: Diego Erben
- **Profesor Práctica**: Francisco Rubio
  - **Email**: `rubiofa@gmail.com`
  - **WhatsApp**: `+54 9 11 3195 8424`
  - **Horario de Consulta**: Jueves de 18:30 a 19:00 hs.
- **Plataforma**: Aula Virtual UNLP
- **Horarios de Cursada**:
  - 📖 **Teoría**: Martes de 19:00 a 22:00 hs
  - 💻 **Práctica**: Jueves de 19:00 a 22:00 hs

## 📌 Enlaces Rápidos de la Materia
- 📋 [[Programa y Bibliografía|Programa Analítico y Bibliografía Completa]]
- 🚀 [[TPI - Trabajo Práctico Integrador|Guía, Entregables y Rúbrica del TPI]]
- 📅 [[00 Organizador/Dashboard|Organizador General del Cuatrimestre]]

---

## 📝 Apuntes y Notas de Clase
```dataview
TABLE fecha as Fecha, tipo as Tipo, bloque as Bloque, estado as Estado
FROM "10 Asignaturas/Tecnologías para la Gestión"
WHERE file.name != "Tecnologías para la Gestión" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

---

## 📚 Recursos y Materiales de Estudio
```dataviewjs
const folderPath = dv.current().file.folder + "/Recursos";
const pdfFiles = app.vault.getFiles().filter(file => 
    (file.extension === pdf || file.extension === xlsx || file.extension === docx) && 
    file.path.startsWith(folderPath)
);

if (pdfFiles.length > 0) {
    dv.list(pdfFiles.map(file => dv.fileLink(file.path)));
} else {
    dv.paragraph("*No hay archivos cargados en la carpeta de Recursos.*");
}
```

---

## 🎯 Tareas y Entregas
- [ ] Resolver repaso interactivo de Bloque 1 y ERP para 1º Parcial en /teach con evaluator loop 📅 2026-09-23 #gestion

## 🎯 Requisitos de Evaluación y Fechas Clave

### Instancias de Examen
| Instancia | Fecha | Modalidad | Temas / Alcance |
| :--- | :--- | :--- | :--- |
| **1º Parcial Teórico** | Martes **20/10/2026** | Individual / Escrito | Bloque 1 y conceptos vistos hasta la fecha. |
| **2º Parcial Teórico** | Martes **01/12/2026** | Individual / Escrito | Bloques 2 y 3. |
| **Presentación TPI (Grupo 1)** | Jueves **03/12/2026** | Grupal / Oral | Defensa del Informe de Consultoría Final. |
| **Presentación TPI (Grupo 2)** | Jueves **10/12/2026** | Grupal / Oral | Defensa del Informe de Consultoría Final. |
| **Recuperatorio General** | Martes **16/12/2026** | Individual / Escrito u Oral | Integrador de teoría. |
| **Cierre de Notas** | Jueves **17/12/2026** | Cierre de actas | Mesa final. |

### Régimen de Aprobación
- **Promoción Directa**: Nota promedio general $\ge 7$ puntos (parciales + TPI aprobado).
- **Aprobación de Cursada / Final**: Nota entre $4$ y $6$ puntos.
- **Desaprobado**: Nota $< 4$ puntos.

---

## 📅 Cronograma Completo 2026 (Teórico - Práctico)

| Sem. | Martes (Teoría) | Tema Teórico | Jueves (Práctica) | Tema Práctico & Entregas TPI |
| :---: | :---: | :--- | :---: | :--- |
| **1** | 18/08 | *Mesa de Examen* | 20/08 | *Mesa Final* |
| **2** | 25/08 | [[2026-08-25 - Clase 01 (Teoría) - Introducción y Transformación Digital\|Introducción a la materia. Temas conceptuales]] | 27/08 | [[2026-08-27 - Clase 01 (Práctica) - Kick-off TPI, Diagnóstico Digital y Procesos AS-IS\|KO del Proyecto, Diagnóstico digital y Mapeo AS-IS]] |
| **3** | 01/09 | [[2026-09-01 - Clase 02 (Teoría) - Unidad 1 - TIC en la Gestión Organizacional\|Unidad 1: Introducción a TIC en la gestión]] | 03/09 | [[2026-09-03 - Clase 02 (Práctica) - Oportunidades de Mejora y Diseño TO-BE\|Oportunidades de mejora y Diseño TO-BE — [Entrega 1] ]] |
| **4** | 08/09 | [[2026-09-08 - Clase 03 (Teoría) - Sistemas de Información y Rol Gerencial\|Unidad 2: Sistemas de información y rol gerencial]] | 10/09 | [[2026-09-10 - Clase 03 (Práctica) - Arquitectura de Sistemas y Cierre Bloque 1\|Arquitectura de sistemas — [Entrega 2 - Cierre B1] ]] |
| **5** | 15/09 | [[2026-09-15 - Clase 04 (Teoría) - Unidad 3 - Sistemas ERP (Parte 1)\|Unidad 3: Sistemas ERP (Parte 1)]] | 17/09 | Introducción práctica a ERP |
| **6** | 22/09 | [[2026-09-22 - Clase 05 (Teoría) - Unidad 3 - Sistemas ERP (Parte 2)|Unidad 3: Sistemas ERP (Parte 2)]] | 24/09 | ERP en profundidad — **[Entrega 3]** |
| **7** | 29/09 | Unidad 3: Sistemas ERP (Parte 3) | 01/10 | Evaluación del mercado ERP — **[Entrega 4]** |
| **8** | 06/10 | Unidad 4: Gestión de clientes (CRM) y SCM | 08/10 | CRM + Ecommerce — **[Entrega 5]** |
| **9** | 13/10 | Unidad 5: Inteligencia de Negocios (BI) | 15/10 | Propuesta de BI y Dashboards — **[Entrega 6 - Cierre B2]** |
| **10** | 20/10 | 📝 **1º Parcial Teórico** | 22/10 | Status y seguimiento de trabajos |
| **11** | 27/10 | Unidad 6: Automatización (RPA) e IA | 29/10 | Casos de IA y Automatización |
| **12** | 03/11 | Unidad 7: Tecnologías Digitales Emergentes | 05/11 | Smart Everything (IoT, Big Data, Cloud) — **[Entrega 7]** |
| **12b**| 10/11 | Unidad 8: Transformación Digital y Gestión del Cambio | 12/11 | Roadmap de implementación y Riesgos — **[Entrega 8 - Cierre B3]** |
| **13** | 17/11 | Unidad 9: Selección e implementación de tecnología | 19/11 | *Feriado — Día de La Plata* |
| **14** | 24/11 | Unidad 10: Evaluación de proyectos y ROI | 26/11 | Gestión del cambio y Business Case — **[Entrega 9]** |
| **15** | 01/12 | 📝 **2º Parcial Teórico** | 03/12 | 🎤 **Presentación Final TPI (Grupo 1)** |
| **16** | 08/12 | *Feriado* | 10/12 | 🎤 **Presentación Final TPI (Grupo 2)** |
| **Fin** | 16/12 | 📝 **Recuperatorio General Teórico** | 17/12 | 🏁 **Mesa Final y Cierre de Notas** |

---
[[Estudios Index|Volver al Índice General]]
