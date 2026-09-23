---
materia: "[[Tecnologías para la Gestión]]"
fecha: "2026-09-08 19:00"
tipo: Clase
bloque: Teoría
estado: En Curso
tags:
  - clase
  - teoria
  - sistemas-de-informacion
  - tps
  - mis
  - dss
  - ess
  - arquitectura-empresarial
---

# 📚 Clase 03 (Teoría) — Sistemas de Información y Rol Gerencial

> [!abstract] Enfoque de la Sesión
> Clasificación de los sistemas de información según el nivel organizacional (operativo, táctico y estratégico), atributos de calidad de la información y composición de la arquitectura empresarial digital.

---

## 📁 Material y Filminas de la Cátedra
- 📄 [[Recursos/Teoría/Clase 03/TPG - Clase 03 - Unidad 2 - DE.pdf|Filminas Unidad 2 - Diego Erben (PDF)]]
- 📄 [[Recursos/Teoría/Clase 03/TPG - Clase 03 - Unidad 2 - LAUDON.pdf|Capítulo Laudon - Unidad 2 (PDF)]]

---

## 🏛️ Pirámide y Tipos de Sistemas de Información
- **TPS (Transaction Processing Systems)**: Nivel operativo. Procesamiento masivo de transacciones del día a día.
- **MIS (Management Information Systems)**: Nivel de gestión / táctico. Informes periódicos y estructurados sobre el rendimiento interno.
- **DSS (Decision Support Systems)**: Nivel táctico / estratégico. Soporte para decisiones semiestructuradas o no estructuradas mediante modelos de simulación y análisis de datos.
- **ESS / EIS (Executive Support / Information Systems)**: Nivel estratégico / directivo. Dashboards ejecutivos, Big Data e indicadores clave del negocio para la alta gerencia.

---

## 💎 Atributos de Calidad de la Información

### De Exactitud
- Precisión
- Integridad
- Consistencia

### De Contenido
- Compleción
- Validez

### De Entrega
- Puntualidad
- Accesibilidad

---

## 🧩 Ecosistema y Arquitectura de Sistemas

![[Pasted image 20260908194712.png]]

- **ERP (Enterprise Resource Planning)**: El corazón del sistema transaccional.
- **CRM (Customer Relationship Management)**: Procesos comerciales, marketing y atención al cliente.
- **RRHH / HCM**: Gestión de personas, presentismo y liquidación de sueldos y jornales (ej. BigMat, PeopleSoft, SAP HCM, Meta4; cubre reclutamiento, vacaciones, capacitación y promoción interna).
- **DBMS**: Sistema gestor de bases de datos.
- **BPM (Business Process Management)**: Gestión continua y automatizada de flujos de procesos (ej. Bizagi).
- **DMS (Document Management System)**: Gestión documental (ej. AndesDocs).
- **BI (Business Intelligence)**: Visualización y analítica gerencial (ej. Tableau, Power BI, Metabase, Qlik, Looker).

![[Pasted image 20260908195002.png]]

> [!important] Criterio de Arquitectura según el Negocio
> Según el tipo de comercio e industria, tiene o no sentido incorporar ciertos componentes a la arquitectura:
> - Si se requiere poder auditar y eliminar registros por derecho al olvido, no se puede utilizar Blockchain.
> - Un e-commerce tradicional no tiene sentido en el núcleo de un hospital público.
> - **Interoperabilidad**: El objetivo principal de la arquitectura es lograr que todos los sistemas se comuniquen fluidamente (ej. Tango no dispone de MRP integrado nativo pero se integra con Capataz).

---

## ⚠️ Seguridad y Riesgos
- Amenazas críticas: **Ransomware** y contingencia de continuidad del negocio.
