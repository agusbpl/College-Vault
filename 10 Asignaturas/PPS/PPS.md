# 📂 PPS (Práctica Profesional Supervisada)

## 👨‍🏫 Cátedra y Contacto
- **Coordinador**: Profesor Coordinador

## 📚 Recursos
*   [[10 Asignaturas/PPS/Recursos|Carpeta de Recursos de la Materia]]

## 📝 Documentación y Registro
```dataview
TABLE fecha as Fecha, estado as Estado
FROM "10 Asignaturas/PPS"
WHERE file.name != "PPS" AND !contains(file.path, "Recursos")
SORT file.name ASC
```

- [ ] Definir tema/proyecto de PPS
- [ ] Contactar con el tutor/coordinador

---
[[Estudios Index|Volver al Índice General]]
