---
materia: Minería y ML
fecha: "2026-09-09"
tipo: Clase
estado: En Progreso
tags:
  - clase
  - apuntes
  - dm-y-ml
  - arboles-de-decision
---

# 🌳 Clase 3: Árboles de Decisión

## 📌 Objetivos de la Sesión
- [x] Comprender la partición recursiva del espacio de muestras.
- [x] Dominar las métricas de desorden: Entropía de Shannon vs Índice Gini.
- [x] Identificar sobreajuste (*overfitting*) y aplicar técnicas de poda preventiva (`max_depth`).
- [x] Detectar fuga de datos (*data leakage*).
- [ ] Resolver de forma autónoma las Actividades 1 a 8 en Python.

---

## 📝 Fundamentos Teóricos y Formulaciones

### 1. Construcción Recursiva y Criterios de Desorden
El árbol busca en cada nodo el atributo $A$ y el umbral $\theta$ que maximicen la reducción del desorden (máxima pureza).

#### A. Entropía de Shannon (Algoritmos ID3 / C4.5)
Mide la incertidumbre en bits:
$$H(S) = - \sum_{i=1}^{C} p_i \log_2(p_i)$$

La **Ganancia de Información** producida por particionar con el atributo $A$ es:
$$\text{Gain}(S, A) = H(S) - \sum_{v \in \text{Valores}(A)} \frac{|S_v|}{|S|} H(S_v)$$

#### B. Índice de Impureza de Gini (Algoritmo CART)
Mide la probabilidad de clasificar erróneamente un elemento elegido al azar:
$$\text{Gini}(S) = 1 - \sum_{i=1}^{C} p_i^2$$

Partición ponderada de Gini:
$$\text{Gini}_{\text{split}}(S, A) = \sum_{v \in \text{Valores}(A)} \frac{|S_v|}{|S|} \text{Gini}(S_v)$$

> [!TIP] Diferencia Práctica
> Gini es computacionalmente más ágil (no calcula logaritmos). En la mayoría de los problemas producen estructuras muy similares.

---

### 2. Control de Complejidad y Sobreajuste
- Si no se limita la profundidad (`max_depth=None`), el árbol continuará creciendo hasta que todas las hojas sean 100% puras ($\text{Gini} = 0$ o $H = 0$), provocando **overfitting**:
  $$\text{Accuracy}_{\text{train}} \to 1.0, \quad \text{Accuracy}_{\text{test}} \ll \text{Accuracy}_{\text{train}}$$
- **Poda Preventiva (*Pre-pruning*)**: Restringir hiperparámetros como `max_depth`, `min_samples_split`, `min_samples_leaf` para reducir la varianza del modelo.

---

### 3. Fuga de Datos (*Data Leakage*)
- Si se deja por error la etiqueta objetivo dentro de la matriz de entrenamiento ($X$), el árbol seleccionará esa variable en la raíz logrando $\text{Accuracy} = 1.0$ de manera trivial y será inservible ante nuevos datos sin clasificar.

---

## 💻 Actividades Prácticas de la Cátedra (1 a 8)
Archivo de trabajo autónomo para resolver:
👉 `10 Asignaturas/DM y ML/Clase 3 - Árboles de decisión-20260914/actividades_practica_alumno.py`

Comando de ejecución:
```bash
uv run --with scikit-learn,pandas,numpy python3 actividades_practica_alumno.py
```

### 📋 Checklist de Actividades:
- [ ] **Actividad 1**: Entrenar `diabetes.csv` con `entropy` y `gini` (`max_depth=4`).
- [ ] **Actividad 2**: Incluir `Outcome` en $X$ y verificar el árbol resultante.
- [ ] **Actividad 3**: Predecir el paciente `[0, 150, 210, 30, 115, 30, 0.2, 25]` con el modelo de entropía.
- [ ] **Actividad 4**: Split 90-10 con parámetros por defecto y comparar exactitud Train vs Test.
- [ ] **Actividad 5**: Comparar split 90-10 con `max_depth=4`.
- [ ] **Actividad 6**: Comparar particiones (80-20), (70-30), (60-40).
- [ ] **Actividad 7**: Clasificación multiclase en `glass.csv` eliminando el ID.
- [ ] **Actividad 8**: Preprocesamiento (One-Hot Encoding, eliminación de salario/ID) y clasificación en `Campus.csv`.
