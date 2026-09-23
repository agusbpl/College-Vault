---
materia: Minería y ML
fecha: "2026-09-14 18:48"
tipo: Repaso Examen
examen_ref: "10 Asignaturas/DM y ML/Sesiones/lessons/0001-flash-teorico-clases-1-a-3.html"
puntaje: "10/10"
nota_sobre_10: "10"
tags:
  - repaso
  - evaluacion
  - estudio-activo
  - arboles-de-decision
  - dm-y-ml
---

# 📊 Sesión de Repaso: Árboles de Decisión y Modelos (Clases 1 a 3)

## 🎯 Resumen de Desempeño
- **Materia**: [[10 Asignaturas/DM y ML/Minería y ML|Minería y ML]]
- **Fecha**: 2026-09-14
- **Estado**: Práctica de Actividades 1 a 8 resuelta y validada.
- **Material Teórico Flash**: [[10 Asignaturas/DM y ML/Sesiones/lessons/0001-flash-teorico-clases-1-a-3.html|Ver Lección HTML]]
- **Script de Actividades**: `10 Asignaturas/DM y ML/Clase 3 - Árboles de decisión-20260914/actividades_arboles.py`

---

## 🔍 Hallazgos y Conclusiones de las Actividades

### 1. Criterios de Partición (Gini vs Entropy) en `diabetes.csv`
- Tanto Entropy ($0.8893$) como Gini ($0.8828$) seleccionan a `Insulin` como atributo de partición raíz.
- Gini es computacionalmente más eficiente; Entropy genera particiones ligeramente más balanceadas en este dataset.

### 2. Data Leakage (Fuga de Datos)
- Al incluir `Outcome` como predictor, el árbol selecciona dicho atributo inmediatamente en la raíz con $100\%$ de accuracy.
- **Trampa crítica**: El modelo resulta inútil para predecir pacientes reales no etiquetados.

### 3. Sobreajuste y Poda (`max_depth`)
- Sin límite de profundidad (`default`), el modelo alcanza $100\%$ de accuracy en Train pero desciende a $83.1\%$ en Test (**Overfitting**).
- Con poda preventiva (`max_depth=4`), la exactitud en Train desciende a $89.2\%$ pero se mantiene o mejora la capacidad de generalización en Test.

### 4. Multiclase en `glass.csv`
- En problemas multiclase (6 categorías de vidrio), un árbol simple de profundidad 4 ronda entre $55\%$ y $67\%$ de exactitud. Revela la necesidad de ensambles (Random Forest / Boosting) que veremos en la Clase 4.

### 5. Preprocesamiento en `Campus.csv`
- Eliminación indispensable de `sl_no` (identificador sin valor predictivo) y `salary` (provocaría fuga de datos, ya que solo tienen salario quienes fueron contratados).
- Transformación One-Hot Encoding de variables nominales (`ssc_b`, `hsc_b`, `hsc_s`, `degree_t`, `specialisation`).
- **Factores determinantes para la contratación**: El rendimiento académico previo (`ssc_p` con 46.8% y `hsc_p` con 31.3%) domina la decisión.

---

## 🔁 Próximos Pasos de la Cursada
- [x] Completar y validar actividades 1 a 8 de Árboles de Decisión (Clase 3) #dm-y-ml 📅 2026-09-14
- [ ] Clase 4: Ensambles (Bagging, Random Forest y Boosting) 📅 2026-09-18 #dm-y-ml
- [ ] Definir propuesta de tema para el Trabajo Grupal #dm-y-ml
