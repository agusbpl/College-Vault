# 🎓 Vault de Obsidian - Segundo Cuatrimestre

¡Bienvenido a tu bóveda (Vault) de Obsidian para organizar tus estudios universitarios! Este repositorio está estructurado bajo las mejores prácticas de gestión del conocimiento personal (PKM) adaptado al ámbito académico.

---

## 📂 Estructura del Vault

La organización de carpetas está diseñada de la siguiente manera:

*   **`00 Organizador/`**: Tu panel de control. Aquí puedes tener calendarios, listas de tareas pendientes, tableros Kanban y tu diario o notas semanales.
*   **`10 Asignaturas/`**: La zona de estudio principal. Contiene una carpeta por cada materia:
    *   `Bases de Datos/`
    *   `Minería y ML/`
    *   `Tecnologías para la Gestión/`
    *   `Visualización/`
    *   *Nota*: Dentro de cada una hay una carpeta **`Recursos/`** donde se guardan los libros y filminas (PDFs) para no mezclar el material de lectura con tus propios apuntes.
*   **`30 Plantillas/`**: Contiene la `Plantilla de Clase.md`. Te permite crear rápidamente apuntes estructurados con metadatos útiles (fecha, estado de revisión, etiquetas).
*   **`40 Adjuntos/`**: Carpeta centralizada donde se guardarán automáticamente todas las capturas de pantalla, imágenes o diagramas que pegues en tus notas. Esto evita que tu raíz se llene de archivos basura.

---

## ⚙️ Configuración Inicial Recomendada en Obsidian

Para sacarle el máximo partido, abre esta carpeta como un "Vault" en Obsidian y realiza los siguientes ajustes:

### 1. Ubicación de Archivos Adjuntos
Evita que las imágenes se guarden en cualquier lado:
*   Ve a **Settings (Configuración) > Files & Links (Archivos y Enlaces)**.
*   Busca **Default location for new attachments (Ubicación predeterminada para nuevos adjuntos)**.
*   Cámbialo a: `In the folder specified below (En la carpeta especificada abajo)`.
*   En la ruta de la carpeta, selecciona: `40 Adjuntos`.

### 2. Configuración de Plantillas (Templates)
Para poder insertar tu plantilla de notas rápidamente:
*   Ve a **Settings > Core Plugins (Complementos principales)** y asegúrate de activar **Templates**.
*   Ve a la sección **Templates** en la configuración de la izquierda.
*   En **Template folder path (Ruta de la carpeta de plantillas)**, pon: `30 Plantillas`.
*   En **Date format (Formato de fecha)**, puedes usar: `YYYY-MM-DD`.

---

## 🔌 Plugins de la Comunidad Recomendados

Puedes instalarlos desde **Settings > Community Plugins** (deberás activar los plugins de la comunidad primero):

1.  **Dataview**: *Esencial*. Te permite crear tablas y listas dinámicas de tus notas usando código sencillo. Por ejemplo, listar todos los exámenes pendientes o ver qué clases no has repasado.
2.  **Kanban**: Crea tableros visuales tipo Trello. Ideal para organizar las entregas y proyectos de las asignaturas.
3.  **Obsidian Git**: Si quieres automatizar tus copias de seguridad de Git desde la propia aplicación móvil o de escritorio sin usar la terminal. Hace commits y pushes automáticos cada determinado tiempo.
4.  **Calendar**: Agrega un widget de calendario en la barra lateral para crear y abrir notas diarias fácilmente.
5.  **Admonition / Callout Manager**: Para agregar cuadros de texto estilizados (como Advertencias, Notas o Tips) a tus apuntes.

---

## 🤝 Gestión con Git

El repositorio cuenta con un archivo `.gitignore` optimizado para Obsidian que previene conflictos de sincronización (ignora estados de ventana como `workspace.json`). 

Para subir este repositorio a GitHub/GitLab:
```bash
git remote add origin TU_URL_DEL_REPOSITORIO
git branch -M main
git push -u origin main
```
