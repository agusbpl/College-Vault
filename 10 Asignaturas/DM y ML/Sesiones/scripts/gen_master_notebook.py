#!/usr/bin/env python3
"""
================================================================================
SCRIPT GENERADOR DEL NOTEBOOK MAESTRO: MINERÍA DE DATOS Y APRENDIZAJE AUTOMÁTICO
Cátedra: Ronchetti - Hasperué | Facultad de Informática, UNLP (2026)
Archivo destino: ../Master_DM_ML_Clases_1_a_5.ipynb
================================================================================
Genera de forma programática un Jupyter Notebook (.ipynb) validado bajo el
estándar nbformat 4.5. Incluye 5 módulos temáticos completos con desgloses
matemáticos exhaustivos en LaTeX, implementaciones vectorizadas en NumPy,
modelos de Scikit-Learn, visualizaciones en Matplotlib y comparativas empíricas.
"""

import json
import os
import sys


def make_cell(cell_type: str, source: str) -> dict:
    """
    Construye un diccionario que representa una celda en formato nbformat 4.5.
    Mantiene saltos de línea canónicos en cada renglón.
    """
    lines = source.splitlines(keepends=True)
    if not lines:
        lines = [""]
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": lines
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell


def build_master_notebook():
    cells = []

    # =========================================================================
    # ENCABEZADO GENERAL E ÍNDICE INTERACTIVO
    # =========================================================================
    header_md = r"""# 🎓 Master Notebook: Minería de Datos y Aprendizaje Automático
### Cátedra: Ronchetti — Hasperué | Facultad de Informática, Universidad Nacional de La Plata (UNLP)
**Ciclo Académico 2026** • *Guía Integral de Fundamentos Teóricos, Desgloses Matemáticos e Implementaciones Vectorizadas (Clases 1 a 5)*

---

## 📌 Presentación y Objetivos del Cuaderno
Este cuaderno interactivo constituye la referencia académica y práctica unificada para las primeras 5 clases de la cátedra de **Minería de Datos y Aprendizaje Automático**. Cada módulo combina:
1. **Rigor Teórico y Analítico**: Fórmulas matemáticas completas en $\LaTeX$ con desglose minucioso de cada variable y sumatoria.
2. **Implementación Artesanal (From Scratch)**: Código vectorizado en **NumPy** para comprender el funcionamiento interno de los algoritmos sin depender ciegamente de librerías.
3. **Validación en Entornos de Producción**: Contrastación directa contra implementaciones optimizadas de **Scikit-Learn** y **SciPy**.
4. **Buenas Prácticas Metodológicas**: Prevención de *Data Leakage*, diagnóstico de *Overfitting/Underfitting* y selección informada de métricas.

---

## 📑 Índice General Interactivo
* **[Clase 1: Fundamentos de IA, KDD vs. CRISP-DM & Métricas de Distancia](#clase-1)**
  * [1.1 Ciclo de Vida: Metodología KDD vs. Proceso CRISP-DM](#11-ciclo-de-vida-kdd-vs-crisp-dm)
  * [1.2 Fundamento Matemático de las Métricas de Distancia](#12-fundamento-matematico-de-distancias)
  * [1.3 Implementación Vectorizada Manual en NumPy](#13-implementacion-vectorizada-numpy)
  * [1.4 Validación Cruzada con SciPy y Scikit-Learn](#14-validacion-scipy-sklearn)
* **[Clase 2: EDA, Preprocesamiento, Escalamiento & KNN](#clase-2)**
  * [2.1 Estandarización Z-score vs. Normalización Min-Max](#21-estandarizacion-vs-normalizacion)
  * [2.2 El Peligro Crítico de Data Leakage (Fuga de Datos)](#22-data-leakage)
  * [2.3 Preprocesamiento Tabular y Limpieza de Datos (Estilo Titanic)](#23-preprocesamiento-tabular)
  * [2.4 Clasificación KNN y Análisis del Hiperparámetro K](#24-knn-hiperparametro-k)
* **[Clase 3: Árboles de Decisión (ID3, CART) y Métricas de Pureza](#clase-3)**
  * [3.1 Entropía de Shannon, Ganancia de Información y Gini](#31-metricas-pureza)
  * [3.2 Cálculo Manual Paso a Paso (Dataset Jugar Tenis)](#32-calculo-manual-arboles)
  * [3.3 Entrenamiento y Visualización de Árboles con Scikit-Learn](#33-entrenamiento-visualizacion-arboles)
  * [3.4 Comparación Empírica: Criterio Gini vs. Criterio Entropy](#34-comparativa-gini-entropy)
* **[Clase 4: Métricas de Evaluación, Curvas ROC/PR y Métodos de Ensamble](#clase-4)**
  * [4.1 La Matriz de Confusión y Fórmulas Derivadas Exhaustivas](#41-matriz-confusion-metricas)
  * [4.2 Umbrales de Decisión, Curva ROC y Métrica AUC](#42-umbral-roc-auc)
  * [4.3 Implementación Manual de Métricas y Validación](#43-implementacion-manual-metricas)
  * [4.4 Taxonomía de Ensambles: Bagging vs. Boosting vs. Stacking](#44-teoria-ensambles)
  * [4.5 Implementación y Comparativa de 4 Ensambles con Curvas ROC Superpuestas](#45-implementacion-comparativa-ensambles)
* **[Clase 5: Desbalance de Clases, Feature Selection y Sistemas de Recomendación](#clase-5)**
  * [5.1 Desbalance de Clases: Undersampling, SMOTE y Función de Pérdida Ponderada](#51-desbalance-clases)
  * [5.2 Implementación Práctica: Mini-SMOTE Manual y Ponderación de Clases](#52-mini-smote-cost-sensitive)
  * [5.3 Selección de Características: Filtro, Wrapper y Embebido (Lasso L1)](#53-feature-selection)
  * [5.4 Sistemas de Recomendación: Similitud Coseno y Filtrado Colaborativo Basado en Usuarios](#54-sistemas-recomendacion)
  * [5.5 Implementación 1: Recomendador Basado en Contenido](#55-recomendador-contenido)
  * [5.6 Implementación 2: Filtrado Colaborativo Manual Paso a Paso con Normalización por Media](#56-filtrado-colaborativo-paso-a-paso)
"""
    cells.append(make_cell("markdown", header_md))

    # Setup del entorno
    setup_code = """# =============================================================================
# CONFIGURACIÓN DEL ENTORNO DE TRABAJO Y LIBRERÍAS
# =============================================================================
import sys
import time
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Desactivar advertencias no críticas para mantener salidas limpias
warnings.filterwarnings('ignore')

# Configuración estética global de gráficos con Matplotlib
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['lines.linewidth'] = 2

# Fijar semilla aleatoria global para garantizar reproducibilidad exacta
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

print(f"✅ Entorno inicializado exitosamente.")
print(f"Python: {sys.version.split()[0]} | NumPy: {np.__version__} | Pandas: {pd.__version__}")
"""
    cells.append(make_cell("code", setup_code))

    # =========================================================================
    # CLASE 1: FUNDAMENTOS DE IA, KDD VS CRISP-DM & MÉTRICAS DE DISTANCIA
    # =========================================================================
    c1_md1 = r"""<a id="clase-1"></a>
# 1. Clase 1: Fundamentos de IA, KDD vs CRISP-DM & Métricas de Distancia

<a id="11-ciclo-de-vida-kdd-vs-crisp-dm"></a>
## 1.1 Ciclo de Vida: Metodología KDD vs. Proceso CRISP-DM

En minería de datos aplicada, los proyectos requieren metodologías estructuradas e iterativas para transformar datos brutos en conocimiento accionable. Las dos metodologías de referencia son:

### 1. KDD (Knowledge Discovery in Databases - Fayyad et al., 1996)
Enfoque eminentemente científico y centrado en los datos. Comprende 5 fases secuenciales e iterativas:
1. **Selección de Datos**: Creación del conjunto objetivo enfocado en un subconjunto de variables o muestras.
2. **Preprocesamiento (Limpieza)**: Tratamiento de ruido, eliminación de anomalías e imputación de valores faltantes.
3. **Transformación (Reducción/Proyección)**: Normalización, reducción de dimensionalidad y derivación de atributos.
4. **Minería de Datos (Data Mining)**: Aplicación de algoritmos para descubrir patrones, agrupamientos o reglas predictivas.
5. **Interpretación / Evaluación**: Validación de patrones descubiertos y traducción en conocimiento útil.

### 2. CRISP-DM (Cross-Industry Standard Process for Data Mining)
Estándar industrial adoptado globalmente, estructurado en 6 fases fuertemente iterativas con ciclos de retroalimentación:
1. **Business Understanding (Comprensión del Negocio)**: Definir objetivos del proyecto desde la perspectiva operativa/organizacional.
2. **Data Understanding (Comprensión de los Datos)**: Recolección inicial, exploración descriptiva y diagnóstico de calidad de datos.
3. **Data Preparation (Preparación de Datos)**: Selección, limpieza, construcción y formateo de tablas para el modelado.
4. **Modeling (Modelado)**: Selección y calibración de técnicas de aprendizaje automático.
5. **Evaluation (Evaluación)**: Validación técnica y de negocio del modelo frente a los objetivos iniciales.
6. **Deployment (Despliegue)**: Integración del modelo en sistemas productivos y monitorización continua.

| Dimensión | Metodología KDD | Metodología CRISP-DM |
| :--- | :--- | :--- |
| **Origen** | Ámbito Académico / Ciencias de la Computación | Consorcio Industrial (Daimler, SPSS, NCR) |
| **Foco Primario** | Transformación matemática y analítica de datos | Impacto de negocio y ciclo de vida de producto |
| **Punto de Partida** | Disponibilidad de un conjunto de datos | Problema u oportunidad estratégica de negocio |
| **Fase Final** | Extracción y validación de conocimiento | Puesta en producción (Deployment) y mantenimiento |

---

<a id="12-fundamento-matematico-de-distancias"></a>
## 1.2 Fundamento Matemático de las Métricas de Distancia

En el aprendizaje basado en instancias (ej. KNN, K-Means, DBSCAN), la noción de similitud entre dos observaciones $\mathbf{p}$ y $\mathbf{q}$ en un espacio $n$-dimensional $\mathbb{R}^n$ se formaliza mediante una función de métrica o distancia $d: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}^+$.

Para que una función sea una **métrica formal**, debe satisfacer cuatro axiomas fundamentales $\forall \mathbf{p}, \mathbf{q}, \mathbf{z} \in \mathbb{R}^n$:
1. **No-negatividad**: $d(\mathbf{p}, \mathbf{q}) \ge 0$
2. **Identidad de indiscernibles**: $d(\mathbf{p}, \mathbf{q}) = 0 \iff \mathbf{p} = \mathbf{q}$
3. **Simetría**: $d(\mathbf{p}, \mathbf{q}) = d(\mathbf{q}, \mathbf{p})$
4. **Desigualdad triangular**: $d(\mathbf{p}, \mathbf{z}) \le d(\mathbf{p}, \mathbf{q}) + d(\mathbf{q}, \mathbf{z})$

---

### Fórmulas Exhaustivas y Desglose de Términos

#### 1. Distancia Euclidiana (Norma $L_2$)
Es la longitud geométrica del segmento de recta que conecta dos puntos en el espacio euclidiano:
$$d_2(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_2 = \sqrt{\sum_{i=1}^n (p_i - q_i)^2}$$

* **Desglose de términos:**
  * $\mathbf{p} = (p_1, p_2, \dots, p_n)^T, \mathbf{q} = (q_1, q_2, \dots, q_n)^T$: Vectores de $n$ dimensiones.
  * $p_i, q_i$: Valores de la $i$-ésima característica para las observaciones $\mathbf{p}$ y $\mathbf{q}$.
  * $(p_i - q_i)^2$: Discrepancia unidimensional elevada al cuadrado. Penaliza drásticamente diferencias grandes (alta sensibilidad a outliers).
  * $\sum_{i=1}^n$: Acumulador que agrega las discrepancias cuadráticas a lo largo de las $n$ características.
  * $\sqrt{\cdot}$: Raíz cuadrada global que devuelve la magnitud a la escala lineal original de las variables.

#### 2. Distancia Manhattan (Norma $L_1$ o Geometría del Taxista)
Suma de las longitudes de las diferencias absolutas proyectadas sobre los ejes coordenados ortogonales:
$$d_1(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_1 = \sum_{i=1}^n |p_i - q_i|$$

* **Desglose de términos:**
  * $|p_i - q_i|$: Valor absoluto de la diferencia en la coordenada $i$. Representa el desplazamiento requerido en una cuadrícula ortogonal.
  * $\sum_{i=1}^n$: Suma lineal simple. No eleva al cuadrado, lo que otorga **mayor robustez frente a valores atípicos** en comparación con $L_2$.

#### 3. Distancia Minkowski (Norma $L_p$ Generalizada)
Generalización paramétrica que unifica a la familia de normas inducidas en espacios vectoriales:
$$d_p(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_p = \left( \sum_{i=1}^n |p_i - q_i|^p \right)^{1/p}, \quad p \ge 1$$

* **Desglose de términos:**
  * $p \in \mathbb{R}, p \ge 1$: Parámetro de orden de Minkowski.
  * Caso $p = 1$: Se reduce exactamente a la Distancia Manhattan ($L_1$).
  * Caso $p = 2$: Se reduce exactamente a la Distancia Euclidiana ($L_2$).
  * Caso $p \to \infty$: Converge a la Distancia de Chebyshev ($L_\infty$): $d_\infty(\mathbf{p}, \mathbf{q}) = \max_{1 \le i \le n} |p_i - q_i|$.

#### 4. Similitud y Distancia Coseno
Mide la orientación angular entre dos vectores en lugar de su separación espacial absoluta:
$$\text{Sim}_{\cos}(\mathbf{p}, \mathbf{q}) = \frac{\mathbf{p} \cdot \mathbf{q}}{\|\mathbf{p}\|_2 \|\mathbf{q}\|_2} = \frac{\sum_{i=1}^n p_i q_i}{\sqrt{\sum_{i=1}^n p_i^2} \sqrt{\sum_{i=1}^n q_i^2}}$$

$$d_{\cos}(\mathbf{p}, \mathbf{q}) = 1 - \text{Sim}_{\cos}(\mathbf{p}, \mathbf{q})$$

* **Desglose de términos:**
  * $\mathbf{p} \cdot \mathbf{q} = \sum_{i=1}^n p_i q_i$: Producto interno (escalar), proyecta un vector sobre el otro.
  * $\|\mathbf{p}\|_2 = \sqrt{\sum_{i=1}^n p_i^2}$: Norma euclidiana (longitud o magnitud física) del vector $\mathbf{p}$.
  * Rango de la similitud: $\text{Sim}_{\cos} \in [-1, 1]$ (para datos no negativos, $[0, 1]$).
  * Rango de la distancia: $d_{\cos} \in [0, 2]$. Es invariante a la escala de los vectores (escala-invariante), haciéndola idónea para minería de texto (TF-IDF) y sistemas de recomendación.
"""
    cells.append(make_cell("markdown", c1_md1))

    c1_md2 = r"""<a id="13-implementacion-vectorizada-numpy"></a>
### 1.3 Implementación Vectorizada Manual en NumPy (From Scratch)
A continuación implementamos cada métrica de distancia de forma manual y vectorizada con NumPy, incluyendo el cálculo matricial pairwise entre dos conjuntos de puntos mediante broadcasting.
"""
    cells.append(make_cell("markdown", c1_md2))

    c1_code1 = """# =============================================================================
# IMPLEMENTACIÓN VECTORIZADA MANUAL DE MÉTRICAS DE DISTANCIA
# =============================================================================

def dist_euclidiana_manual(p: np.ndarray, q: np.ndarray) -> float:
    \"\"\"Calcula la distancia Euclidiana (L2) entre dos vectores p y q.\"\"\"
    diff = np.asarray(p, dtype=float) - np.asarray(q, dtype=float)
    return float(np.sqrt(np.sum(diff ** 2)))


def dist_manhattan_manual(p: np.ndarray, q: np.ndarray) -> float:
    \"\"\"Calcula la distancia Manhattan (L1) entre dos vectores p y q.\"\"\"
    diff = np.asarray(p, dtype=float) - np.asarray(q, dtype=float)
    return float(np.sum(np.abs(diff)))


def dist_minkowski_manual(p: np.ndarray, q: np.ndarray, p_order: float = 3.0) -> float:
    \"\"\"Calcula la distancia Minkowski Lp generalizada entre dos vectores p y q.\"\"\"
    if p_order < 1.0:
        raise ValueError("El parámetro de orden p debe ser mayor o igual a 1.0.")
    diff = np.asarray(p, dtype=float) - np.asarray(q, dtype=float)
    return float(np.sum(np.abs(diff) ** p_order) ** (1.0 / p_order))


def dist_coseno_manual(p: np.ndarray, q: np.ndarray) -> float:
    \"\"\"Calcula la distancia Coseno (1 - cos_sim) entre dos vectores p y q.\"\"\"
    p_arr = np.asarray(p, dtype=float)
    q_arr = np.asarray(q, dtype=float)
    norm_p = np.linalg.norm(p_arr)
    norm_q = np.linalg.norm(q_arr)
    if norm_p == 0 or norm_q == 0:
        raise ZeroDivisionError("No es posible calcular similitud coseno con vectores de magnitud cero.")
    similitud = np.dot(p_arr, q_arr) / (norm_p * norm_q)
    # Acotar numéricamente al rango [-1.0, 1.0] para mitigar errores de redondeo float
    similitud_clipped = np.clip(similitud, -1.0, 1.0)
    return float(1.0 - similitud_clipped)


def matriz_distancias_pairwise_manual(X: np.ndarray, Y: np.ndarray = None, metric: str = 'euclidean', p_order: float = 2.0) -> np.ndarray:
    \"\"\"
    Calcula la matriz de distancias entre todas las filas de X e Y de forma vectorizada (broadcasting).
    Si Y es None, se calcula la matriz cuadrada de distancias entre las filas de X.
    \"\"\"
    X_arr = np.asarray(X, dtype=float)
    Y_arr = X_arr if Y is None else np.asarray(Y, dtype=float)
    
    # Broadcasting tridimensional: X[:, None, :] tiene forma (M, 1, D) y Y[None, :, :] tiene (1, N, D)
    diff = X_arr[:, np.newaxis, :] - Y_arr[np.newaxis, :, :]  # Forma resultante: (M, N, D)
    
    if metric == 'euclidean':
        return np.sqrt(np.sum(diff ** 2, axis=2))
    elif metric == 'manhattan':
        return np.sum(np.abs(diff), axis=2)
    elif metric == 'minkowski':
        return np.sum(np.abs(diff) ** p_order, axis=2) ** (1.0 / p_order)
    elif metric == 'cosine':
        dot_product = np.dot(X_arr, Y_arr.T)
        norms_X = np.linalg.norm(X_arr, axis=1, keepdims=True)
        norms_Y = np.linalg.norm(Y_arr, axis=1, keepdims=True)
        sim = dot_product / (norms_X * norms_Y.T)
        return 1.0 - np.clip(sim, -1.0, 1.0)
    else:
        raise ValueError(f"Métrica desconocida: {metric}")

print("✅ Funciones vectorizadas de distancias compiladas correctamente en memoria.")
"""
    cells.append(make_cell("code", c1_code1))

    c1_md3 = r"""<a id="14-validacion-scipy-sklearn"></a>
### 1.4 Test con Datos Sintéticos y Validación Cruzada (SciPy & Scikit-Learn)
Validamos la precisión de nuestras implementaciones manuales contra las funciones estándar de SciPy (`scipy.spatial.distance`) y Scikit-Learn (`pairwise_distances`), verificando discrepancias numéricas mediante aserciones con tolerancia estricta ($< 10^{-12}$).
"""
    cells.append(make_cell("markdown", c1_md3))

    c1_code2 = """# =============================================================================
# VALIDACIÓN CRUZADA CONTRA SCIPY Y SCIKIT-LEARN
# =============================================================================
from scipy.spatial.distance import (
    euclidean as scipy_euclidean,
    cityblock as scipy_cityblock,
    minkowski as scipy_minkowski,
    cosine as scipy_cosine
)
from sklearn.metrics.pairwise import pairwise_distances

# Generación de dos observaciones sintéticas en 5 dimensiones
p_sample = np.array([2.5, 0.0, 4.8, 1.2, 7.3])
q_sample = np.array([1.1, 3.2, 2.4, 1.8, 5.0])

# Cómputo con implementaciones manuales
d_euc_man = dist_euclidiana_manual(p_sample, q_sample)
d_man_man = dist_manhattan_manual(p_sample, q_sample)
d_min_man = dist_minkowski_manual(p_sample, q_sample, p_order=3.0)
d_cos_man = dist_coseno_manual(p_sample, q_sample)

# Cómputo con SciPy oficial
d_euc_sci = scipy_euclidean(p_sample, q_sample)
d_man_sci = scipy_cityblock(p_sample, q_sample)
d_min_sci = scipy_minkowski(p_sample, q_sample, p=3.0)
d_cos_sci = scipy_cosine(p_sample, q_sample)

# Validación de exactitud numérica con tolerancia ultra-estricta (1e-12)
assert np.isclose(d_euc_man, d_euc_sci, atol=1e-12), "Discrepancia en Distancia Euclidiana"
assert np.isclose(d_man_man, d_man_sci, atol=1e-12), "Discrepancia en Distancia Manhattan"
assert np.isclose(d_min_man, d_min_sci, atol=1e-12), "Discrepancia en Distancia Minkowski"
assert np.isclose(d_cos_man, d_cos_sci, atol=1e-12), "Discrepancia en Distancia Coseno"

# Tabla comparativa de resultados
df_dist_test = pd.DataFrame({
    'Métrica': ['Euclidiana (L2)', 'Manhattan (L1)', 'Minkowski (p=3)', 'Coseno (1 - cos)'],
    'Manual NumPy': [d_euc_man, d_man_man, d_min_man, d_cos_man],
    'SciPy Oficial': [d_euc_sci, d_man_sci, d_min_sci, d_cos_sci],
    'Diferencia Absoluta': [
        abs(d_euc_man - d_euc_sci),
        abs(d_man_man - d_man_sci),
        abs(d_min_man - d_min_sci),
        abs(d_cos_man - d_cos_sci)
    ]
})
print("📊 Tabla de Validación de Distancias Vector vs Vector:")
print(df_dist_test.to_string(index=False))

# Test matricial Pairwise: Matriz de 4 muestras x 3 dimensiones
X_test = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [1.5, 3.5, 5.5]
])

mat_manual = matriz_distancias_pairwise_manual(X_test, metric='euclidean')
mat_sklearn = pairwise_distances(X_test, metric='euclidean')

assert np.allclose(mat_manual, mat_sklearn, atol=1e-12), "Discrepancia en matriz pairwise de Scikit-Learn"
print("\\n✅ Validación Pairwise Exitosa: Error máximo frente a Scikit-Learn =", np.max(np.abs(mat_manual - mat_sklearn)))
"""
    cells.append(make_cell("code", c1_code2))

    # =========================================================================
    # CLASE 2: EDA, PREPROCESAMIENTO, ESCALAMIENTO & KNN
    # =========================================================================
    c2_md1 = r"""<a id="clase-2"></a>
# 2. Clase 2: EDA, Preprocesamiento, Escalamiento & KNN

<a id="21-estandarizacion-vs-normalizacion"></a>
## 2.1 Estandarización Z-score vs. Normalización Min-Max

Los algoritmos basados en distancias geométricas (KNN, SVM, K-Means, Redes Neuronales) son fuertemente dependientes de las escalas de las variables. Una característica con rango $[0, 100000]$ (ej. Ingreso Anual) dominaría numéricamente el cálculo de distancias por sobre una con rango $[0, 5]$ (ej. Número de hijos), aunque esta última posea mayor poder predictivo.

### 1. Estandarización Z-score
Proyecta los datos hacia una distribución con media centrada en cero y desviación estándar unitaria:
$$z = \frac{x - \mu}{\sigma}$$

* **Desglose de términos:**
  * $x$: Valor empírico original de la característica.
  * $\mu = \frac{1}{N} \sum_{i=1}^N x_i$: Media aritmética calculada sobre la muestra.
  * $\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2}$: Desviación estándar de la muestra.
  * Propiedades resultantes: $\mathbb{E}[Z] = 0$, $\text{Var}(Z) = 1$.
  * **Comportamiento ante Outliers**: No acota el rango a un intervalo cerrado. Conserva las distancias relativas de valores extremos en unidades de desviaciones estándar.

### 2. Normalización Min-Max
Realiza un reescalamiento lineal estricto de los datos a un intervalo acotado $[a, b]$, convencionalmente $[0, 1]$:
$$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}} (b - a) + a \xrightarrow{a=0, b=1} x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

* **Desglose de términos:**
  * $x_{\min} = \min(X), x_{\max} = \max(X)$: Valores extremos inferior y superior observados.
  * $x_{\max} - x_{\min}$: Rango muestral dinámico de la variable.
  * **Comportamiento ante Outliers**: **Extremadamente sensible**. Un único valor atípico desproporcionado comprimirá todo el resto de las observaciones en una franja diminuta (ej. $[0.0, 0.05]$), destruyendo la resolución de la señal.

---

<a id="22-data-leakage"></a>
## 2.2 El Peligro Crítico de Data Leakage (Fuga de Datos)

El **Data Leakage** ocurre cuando información del conjunto de prueba (o del futuro) se filtra inadvertidamente en el entrenamiento del modelo.

### 🚨 La Regla de Oro del Aprendizaje Automático
> **Todo parámetro de preprocesamiento (medias, desviaciones estándar, medianas de imputación, selectores de variables, codificadores) DEBE aprenderse estrictamente con el conjunto de entrenamiento (`X_train`) usando `.fit()` o `.fit_transform()`. El conjunto de prueba (`X_test`) debe tratarse como datos no vistos en producción y transformarse EXCLUSIVAMENTE con `.transform()`.**

Si ejecutamos `scaler.fit_transform(X)` sobre todo el dataset antes de `train_test_split()`, $\mu$ y $\sigma$ contendrán información de `X_test`. Esto producirá una estimación artificialmente optimista en validación y una caída estrepitosa del desempeño en producción real.
"""
    cells.append(make_cell("markdown", c2_md1))

    c2_md2 = r"""<a id="23-preprocesamiento-tabular"></a>
### 2.3 Preprocesamiento Tabular y Limpieza de Datos (Estilo Titanic)
Generamos un conjunto de datos sintético realista con valores numéricos y categóricos, incluyendo datos faltantes intencionales. Luego aplicamos la regla de oro: partición previa, imputación sin fuga de datos, One-Hot Encoding y estandarización Z-score con `StandardScaler`.
"""
    cells.append(make_cell("markdown", c2_md2))

    c2_code1 = """# =============================================================================
# PREPROCESAMIENTO TABULAR ESTILO TITANIC (SIN DATA LEAKAGE)
# =============================================================================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generación sintética representativa de un dataset de 600 pasajeros (estilo Titanic)
np.random.seed(RANDOM_STATE)
n_samples = 600

edades = np.random.normal(loc=30, scale=14, size=n_samples)
edades = np.clip(edades, 1, 80)
# Inyectar valores nulos intencionales (12% de registros faltantes en Age)
mask_nulos = np.random.rand(n_samples) < 0.12
edades[mask_nulos] = np.nan

tarifas = np.random.exponential(scale=35, size=n_samples) + 7.5
parientes = np.random.poisson(lam=0.8, size=n_samples)
genero = np.random.choice(['male', 'female'], size=n_samples, p=[0.65, 0.35])
pclass = np.random.choice([1, 2, 3], size=n_samples, p=[0.25, 0.25, 0.50])
puerto = np.random.choice(['S', 'C', 'Q', None], size=n_samples, p=[0.70, 0.20, 0.08, 0.02])

# Probabilidad de supervivencia condicionada (mujer, 1ra clase y alta tarifa favorecen supervivencia)
log_odds = (
    -1.2 
    + 1.8 * (genero == 'female') 
    + 1.0 * (pclass == 1) 
    - 0.8 * (pclass == 3) 
    + 0.015 * tarifas 
    - 0.02 * np.nan_to_num(edades, nan=30)
)
prob_supervivencia = 1.0 / (1.0 + np.exp(-log_odds))
sobrevivio = (np.random.rand(n_samples) < prob_supervivencia).astype(int)

df_titanic = pd.DataFrame({
    'Age': edades,
    'Fare': tarifas,
    'SibSp': parientes,
    'Sex': genero,
    'Pclass': pclass,
    'Embarked': puerto,
    'Survived': sobrevivio
})

print("📋 Primeros 5 registros del dataset sintético:")
print(df_titanic.head())
print("\\n🔍 Diagnóstico de valores nulos:")
print(df_titanic.isnull().sum())

# -----------------------------------------------------------------------------
# PARTICIÓN TRAIN/TEST ANTES DE CUALQUIER IMPUTACIÓN O TRANSFORMACIÓN
# -----------------------------------------------------------------------------
X = df_titanic.drop(columns=['Survived'])
y = df_titanic['Survived']

X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y
)

# Imputación CORRECTA sin Data Leakage:
# 1. Mediana de edad calculada ÚNICAMENTE en train
mediana_edad_train = X_train_raw['Age'].median()
X_train_clean = X_train_raw.copy()
X_test_clean = X_test_raw.copy()
X_train_clean['Age'] = X_train_clean['Age'].fillna(mediana_edad_train)
X_test_clean['Age'] = X_test_clean['Age'].fillna(mediana_edad_train)

# 2. Moda de embarque calculada ÚNICAMENTE en train
moda_puerto_train = X_train_raw['Embarked'].mode()[0]
X_train_clean['Embarked'] = X_train_clean['Embarked'].fillna(moda_puerto_train)
X_test_clean['Embarked'] = X_test_clean['Embarked'].fillna(moda_puerto_train)

# 3. One-Hot Encoding consistente con drop_first=True para evitar colinealidad
X_train_encoded = pd.get_dummies(X_train_clean, columns=['Sex', 'Embarked', 'Pclass'], drop_first=True)
X_test_encoded = pd.get_dummies(X_test_clean, columns=['Sex', 'Embarked', 'Pclass'], drop_first=True)
# Alinear columnas de test para asegurar idéntico espacio de características
X_train_encoded, X_test_encoded = X_train_encoded.align(X_test_encoded, join='left', axis=1, fill_value=0)

# 4. Estandarización Z-score respetando la regla fit en train y transform en test
num_cols = ['Age', 'Fare', 'SibSp']
scaler = StandardScaler()
X_train_scaled = X_train_encoded.copy()
X_test_scaled = X_test_encoded.copy()

X_train_scaled[num_cols] = scaler.fit_transform(X_train_encoded[num_cols])
X_test_scaled[num_cols] = scaler.transform(X_test_encoded[num_cols])

print(f"\\n✅ Preprocesamiento completado con éxito.")
print(f"Train Shape: {X_train_scaled.shape} | Test Shape: {X_test_scaled.shape}")
print(f"Media Age Train estandarizada = {X_train_scaled['Age'].mean():.4f} | Std = {X_train_scaled['Age'].std():.4f}")
print(f"Media Age Test estandarizada  = {X_test_scaled['Age'].mean():.4f} | Std = {X_test_scaled['Age'].std():.4f}")
"""
    cells.append(make_cell("code", c2_code1))

    c2_md3 = r"""<a id="24-knn-hiperparametro-k"></a>
### 2.4 Clasificación KNN y Análisis del Hiperparámetro K
Entrenamos un clasificador $K$-Nearest Neighbors variando $K \in [1, 30]$ para visualizar empíricamente el equilibrio de **Sesgo-Varianza**:
* Para $K=1$, la frontera es hipersensible a cada muestra individual de Train (**Sobreajuste / Alta Varianza**).
* Para $K$ grande, la frontera suaviza en exceso e ignora patrones locales (**Subajuste / Alto Sesgo**).
"""
    cells.append(make_cell("markdown", c2_md3))

    c2_code2 = """# =============================================================================
# CLASIFICACIÓN CON KNN Y BARRIDO DEL HIPERPARÁMETRO K
# =============================================================================
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

k_values = list(range(1, 31))
train_accuracies = []
test_accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn.fit(X_train_scaled, y_train)
    
    y_pred_train = knn.predict(X_train_scaled)
    y_pred_test = knn.predict(X_test_scaled)
    
    train_accuracies.append(accuracy_score(y_train, y_pred_train))
    test_accuracies.append(accuracy_score(y_test, y_pred_test))

best_k = k_values[int(np.argmax(test_accuracies))]
best_test_acc = max(test_accuracies)

# Gráfico del impacto del hiperparámetro K
plt.figure(figsize=(11, 5))
plt.plot(k_values, train_accuracies, marker='o', label='Exactitud Train (Ajuste)', color='#1f77b4', linestyle='--')
plt.plot(k_values, test_accuracies, marker='s', label='Exactitud Test (Generalización)', color='#d62728', linewidth=2.5)

# Señalización del K óptimo
plt.axvline(x=best_k, color='green', linestyle=':', label=f'K* Óptimo = {best_k} (Test Acc: {best_test_acc:.3f})')
plt.scatter([best_k], [best_test_acc], color='green', s=120, zorder=5)

# Zonas de sesgo y varianza
plt.axvspan(1, 3, alpha=0.15, color='orange', label='Zona de Sobreajuste (K muy bajo: Alta Varianza)')
plt.axvspan(20, 30, alpha=0.15, color='purple', label='Zona de Subajuste (K muy alto: Alto Sesgo)')

plt.title('Impacto del Hiperparámetro K en KNeighborsClassifier (Detección de Sesgo vs. Varianza)')
plt.xlabel('Número de Vecinos Más Cercanos (K)')
plt.ylabel('Exactitud (Accuracy)')
plt.xticks(k_values)
plt.legend(loc='lower right', frameon=True)
plt.tight_layout()
plt.show()

print(f"🎯 Conclusión del Experimento KNN:")
print(f"Para K=1, la exactitud en Train es {train_accuracies[0]:.4f} (memorización total), pero en Test cae a {test_accuracies[0]:.4f}.")
print(f"El K óptimo es K={best_k} alcanzando una exactitud de generalización del {best_test_acc * 100:.2f}%.")
"""
    cells.append(make_cell("code", c2_code2))

    # =========================================================================
    # CLASE 3: ÁRBOLES DE DECISIÓN (ID3, CART) Y MÉTRICAS DE PUREZA
    # =========================================================================
    c3_md1 = r"""<a id="clase-3"></a>
# 3. Clase 3: Árboles de Decisión (ID3, CART) y Métricas de Pureza

<a id="31-metricas-pureza"></a>
## 3.1 Entropía de Shannon, Ganancia de Información y Gini

Los árboles de decisión son modelos no paramétricos que dividen recursivamente el espacio de características en hiper-rectángulos ortogonales disjuntos. La calidad de una partición se mide mediante criterios matemáticos de **impureza**.

---

### 1. Entropía de Shannon (Algoritmo ID3 / C4.5)
Cuantifica la incertidumbre o nivel de desorden probabilístico de una partición de datos $S$:
$$H(S) = - \sum_{c=1}^C p_c \log_2(p_c)$$

* **Desglose de términos:**
  * $S$: Subconjunto o nodo de datos evaluado.
  * $C$: Número total de clases objetivo ($c \in \{1, 2, \dots, C\}$).
  * $p_c = \frac{|S_c|}{|S|}$: Proporción empírica de muestras en $S$ que pertenecen a la clase $c$.
  * $\log_2(p_c)$: Logaritmo en base 2 (unidades medidas en *bits* de información).
  * Convención matemática: Si $p_c = 0$, se define $\lim_{p \to 0^+} p \log_2(p) = 0$.
  * Rango: $H(S) = 0$ cuando el nodo es **puro** (todas las muestras pertenecen a una sola clase). Máximo $H(S) = \log_2(C)$ cuando la distribución de clases es perfectamente uniforme.

---

### 2. Ganancia de Información (Information Gain - ID3)
Mide la reducción esperada en la entropía al particionar el conjunto $S$ según los valores de un atributo candidato $A$:
$$IG(S, A) = H(S) - \sum_{v \in \text{Valores}(A)} \frac{|S_v|}{|S|} H(S_v)$$

* **Desglose de términos:**
  * $H(S)$: Entropía original del nodo padre antes de la partición.
  * $\text{Valores}(A)$: Conjunto exhaustivo de valores discretos posibles del atributo $A$.
  * $S_v = \{x \in S \mid A(x) = v\}$: Subconjunto de muestras donde el atributo $A$ toma el valor específico $v$.
  * $\frac{|S_v|}{|S|}$: Ponderación probabilística del nodo hijo $v$ (fracción de muestras asignadas a esa rama).
  * $H(S_v)$: Entropía interna del subnodo resultante $S_v$.
  * Criterio de selección ID3: Elegir el atributo $A^*$ que maximice la Ganancia de Información: $A^* = \arg\max_A IG(S, A)$.

---

### 3. Índice de Impureza de Gini (Algoritmo CART)
Representa la probabilidad de clasificar erróneamente un elemento elegido al azar de $S$ si se le asignara aleatoriamente una clase según la distribución observada:
$$Gini(S) = 1 - \sum_{c=1}^C p_c^2$$

* **Desglose de términos:**
  * $p_c^2$: Probabilidad de que dos elementos independientes elegidos de $S$ pertenezcan a la misma clase $c$.
  * $\sum_{c=1}^C p_c^2$: Probabilidad acumulada de concordancia de clases.
  * Para clasificación binaria ($p$ y $1-p$): $Gini(S) = 1 - (p^2 + (1-p)^2) = 2p(1-p)$.
  * Rango binario: Mínimo $0.0$ (nodo perfectamente puro), Máximo $0.5$ (máxima incertidumbre, clases balanceadas $50\% - 50\%$).

---

### 4. Gini Ponderado para Split Binario (CART)
En el algoritmo CART, cada partición es estrictamente binaria ($A \le \theta$ vs $A > \theta$):
$$Gini_{\text{split}}(S, A) = \frac{|S_L|}{|S|} Gini(S_L) + \frac{|S_R|}{|S|} Gini(S_R)$$

* **Desglose de términos:**
  * $S_L, S_R$: Subconjuntos hijos izquierdo y derecho resultantes del corte binario.
  * $\frac{|S_L|}{|S|}, \frac{|S_R|}{|S|}$: Proporciones muestrales enviadas al nodo izquierdo y derecho.
  * Criterio de selección CART: Minimizar $Gini_{\text{split}}(S, A)$ o equivalentemente maximizar $\Delta Gini = Gini(S) - Gini_{\text{split}}(S, A)$.
"""
    cells.append(make_cell("markdown", c3_md1))

    c3_md2 = r"""<a id="32-calculo-manual-arboles"></a>
### 3.2 Cálculo Manual Paso a Paso (Dataset Jugar Tenis)
A continuación implementamos el cálculo de Entropía, Gini y Ganancia de Información desde cero en NumPy y lo aplicamos al dataset clásico de 14 observaciones "Play Tennis" para seleccionar matemáticamente el atributo de partición en la raíz.
"""
    cells.append(make_cell("markdown", c3_md2))

    c3_code1 = """# =============================================================================
# CÁLCULO MANUAL PASO A PASO DE ENTROPÍA Y GINI (DATASET JUGAR TENIS)
# =============================================================================

def entropia_shannon_manual(y: np.ndarray) -> float:
    \"\"\"Calcula la entropía de Shannon H(S) para un vector de etiquetas categóricas.\"\"\"
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probabilidades = counts / len(y)
    probabilidades = probabilidades[probabilidades > 0]
    return float(-np.sum(probabilidades * np.log2(probabilidades)))


def gini_impureza_manual(y: np.ndarray) -> float:
    \"\"\"Calcula el índice de impureza de Gini para un vector de etiquetas categóricas.\"\"\"
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probabilidades = counts / len(y)
    return float(1.0 - np.sum(probabilidades ** 2))


def ganancia_informacion_manual(df: pd.DataFrame, feature_col: str, target_col: str) -> float:
    \"\"\"Calcula la ganancia de información IG(S, feature) para un atributo discreto.\"\"\"
    n_total = len(df)
    h_padre = entropia_shannon_manual(df[target_col].values)
    
    h_hijos_ponderada = 0.0
    for valor, subconjunto in df.groupby(feature_col):
        peso = len(subconjunto) / n_total
        h_hijo = entropia_shannon_manual(subconjunto[target_col].values)
        h_hijos_ponderada += peso * h_hijo
        
    return float(h_padre - h_hijos_ponderada)


def gini_split_manual(df: pd.DataFrame, feature_col: str, target_col: str) -> float:
    \"\"\"Calcula el Gini ponderado resultante de dividir según un atributo discreto.\"\"\"
    n_total = len(df)
    gini_ponderado = 0.0
    for valor, subconjunto in df.groupby(feature_col):
        peso = len(subconjunto) / n_total
        gini_hijo = gini_impureza_manual(subconjunto[target_col].values)
        gini_ponderado += peso * gini_hijo
    return float(gini_ponderado)

# Dataset clásico Play Tennis (14 observaciones canónicas)
df_tennis = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast',
                'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
             'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
                   'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

h_raiz = entropia_shannon_manual(df_tennis['PlayTennis'].values)
gini_raiz = gini_impureza_manual(df_tennis['PlayTennis'].values)

print(f"🎾 Dataset Jugar Tenis (Total N = {len(df_tennis)} muestras):")
print(f"Distribución objetivo: {dict(df_tennis['PlayTennis'].value_counts())}")
print(f"Entropía Inicial del Nodo Raíz H(S)    = {h_raiz:.4f} bits")
print(f"Impureza de Gini Inicial del Raíz Gini = {gini_raiz:.4f}")

# Evaluación de cada atributo candidato para la partición raíz
atributos = ['Outlook', 'Temperature', 'Humidity', 'Wind']
eval_list = []
for attr in atributos:
    ig = ganancia_informacion_manual(df_tennis, attr, 'PlayTennis')
    gini_sp = gini_split_manual(df_tennis, attr, 'PlayTennis')
    eval_list.append({
        'Atributo Candidato': attr,
        'Ganancia de Información (ID3)': ig,
        'Gini Ponderado Split (CART)': gini_sp
    })

df_eval_tree = pd.DataFrame(eval_list).sort_values(by='Ganancia de Información (ID3)', ascending=False)
print("\\n📊 Evaluación de Partición en Nodo Raíz:")
print(df_eval_tree.to_string(index=False))

mejor_id3 = df_eval_tree.iloc[0]['Atributo Candidato']
mejor_cart = df_eval_tree.sort_values(by='Gini Ponderado Split (CART)').iloc[0]['Atributo Candidato']
print(f"\\n🏆 Atributo óptimo seleccionado por ID3 (Mayor IG)    : {mejor_id3}")
print(f"🏆 Atributo óptimo seleccionado por CART (Menor Gini) : {mejor_cart}")
"""
    cells.append(make_cell("code", c3_code1))

    c3_md3 = r"""<a id="33-entrenamiento-visualizacion-arboles"></a>
### 3.3 Entrenamiento y Visualización de Árboles con Scikit-Learn
Entrenamos un `DecisionTreeClassifier` con Scikit-Learn sobre el dataset real `load_breast_cancer` aplicando poda preventiva (`max_depth=3`). Visualizamos las reglas de decisión en formato textual estructurado (`export_text`) y mediante un diagrama gráfico de alta fidelidad (`plot_tree`).
"""
    cells.append(make_cell("markdown", c3_md3))

    c3_code2 = """# =============================================================================
# ENTRENAMIENTO Y VISUALIZACIÓN DE ÁRBOLES CON SCIKIT-LEARN
# =============================================================================
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

cancer_data = load_breast_cancer()
X_cancer = cancer_data.data
y_cancer = cancer_data.target
feature_names = cancer_data.feature_names
class_names = cancer_data.target_names

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X_cancer, y_cancer, test_size=0.30, random_state=RANDOM_STATE, stratify=y_cancer
)

# Ajuste con poda preventiva max_depth=3 para asegurar interpretabilidad
arbol_cart = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=RANDOM_STATE)
arbol_cart.fit(X_train_c, y_train_c)

print(f"🌲 Desempeño del Árbol (max_depth=3):")
print(f"Exactitud en Train : {arbol_cart.score(X_train_c, y_train_c):.4f}")
print(f"Exactitud en Test  : {arbol_cart.score(X_test_c, y_test_c):.4f}")

# 1. Visualización Textual de las Reglas Lógicas
print("\\n📜 Representación en Reglas Lógicas (export_text):")
reglas_texto = export_text(arbol_cart, feature_names=list(feature_names))
print(reglas_texto[:700] + "\\n... [Reglas truncadas para brevedad] ...")

# 2. Visualización Gráfica con plot_tree
plt.figure(figsize=(18, 8), dpi=100)
plot_tree(
    arbol_cart,
    feature_names=feature_names,
    class_names=class_names,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Estructura del Árbol de Decisión CART (Dataset Breast Cancer, max_depth=3)", fontsize=14)
plt.tight_layout()
plt.show()
"""
    cells.append(make_cell("code", c3_code2))

    c3_md4 = r"""<a id="34-comparativa-gini-entropy"></a>
### 3.4 Comparativa Empírica: Criterio Gini vs. Criterio Entropy
Analizamos el comportamiento de ambos criterios de pureza sobre el dataset completo sin poda artificial, evaluando tiempo de cómputo en milisegundos, profundidad alcanzada, número de hojas y capacidad de generalización en test.
"""
    cells.append(make_cell("markdown", c3_md4))

    c3_code3 = """# =============================================================================
# COMPARATIVA EMPÍRICA RIGUROSA: CRITERIO GINI VS. CRITERIO ENTROPY
# =============================================================================

t0_gini = time.perf_counter()
arbol_gini_full = DecisionTreeClassifier(criterion='gini', random_state=RANDOM_STATE)
arbol_gini_full.fit(X_train_c, y_train_c)
t_gini = (time.perf_counter() - t0_gini) * 1000

t0_ent = time.perf_counter()
arbol_ent_full = DecisionTreeClassifier(criterion='entropy', random_state=RANDOM_STATE)
arbol_ent_full.fit(X_train_c, y_train_c)
t_ent = (time.perf_counter() - t0_ent) * 1000

acc_gini_train = arbol_gini_full.score(X_train_c, y_train_c)
acc_gini_test = arbol_gini_full.score(X_test_c, y_test_c)

acc_ent_train = arbol_ent_full.score(X_train_c, y_train_c)
acc_ent_test = arbol_ent_full.score(X_test_c, y_test_c)

df_comp_criterios = pd.DataFrame({
    'Criterio': ['Gini (CART)', 'Entropy (ID3 / C4.5)'],
    'Tiempo Ajuste (ms)': [t_gini, t_ent],
    'Profundidad Máxima': [arbol_gini_full.get_depth(), arbol_ent_full.get_depth()],
    'Nodos Hoja': [arbol_gini_full.get_n_leaves(), arbol_ent_full.get_n_leaves()],
    'Accuracy Train': [acc_gini_train, acc_ent_train],
    'Accuracy Test': [acc_gini_test, acc_ent_test]
})

print("⚖️ Comparativa Empírica entre Gini y Entropy:")
print(df_comp_criterios.to_string(index=False))

print("\\n💡 Análisis Teórico y Práctico:")
print("1. En eficiencia computacional, Gini evita calcular logaritmos base 2, siendo más rápido en datasets grandes.")
print("2. En precisión predictiva, ambos criterios generan particiones con exactitud prácticamente idéntica en más del 95% de los problemas reales.")
"""
    cells.append(make_cell("code", c3_code3))

    # =========================================================================
    # CLASE 4: MÉTRICAS DE EVALUACIÓN, CURVAS ROC/PR Y ENSAMBLES
    # =========================================================================
    c4_md1 = r"""<a id="clase-4"></a>
# 4. Clase 4: Métricas de Evaluación, Curvas ROC/PR y Ensambles

<a id="41-matriz-confusion-metricas"></a>
## 4.1 La Matriz de Confusión y Fórmulas Derivadas Exhaustivas

En problemas de clasificación supervisada, la evaluación mediante exactitud global (*Accuracy*) resulta insuficiente y engañosa ante distribuciones desbalanceadas. La base de toda evaluación rigurosa es la **Matriz de Confusión**:

| Realidad \ Predicción | Predicho Positivo ($\hat{Y}=1$) | Predicho Negativo ($\hat{Y}=0$) | Total Real |
| :--- | :---: | :---: | :---: |
| **Real Positivo ($Y=1$)** | $\mathbf{TP}$ (Verdadero Positivo) | $\mathbf{FN}$ (Falso Negativo - Error Tipo II) | $P = TP + FN$ |
| **Real Negativo ($Y=0$)** | $\mathbf{FP}$ (Falso Positivo - Error Tipo I) | $\mathbf{TN}$ (Verdadero Negativo) | $N = FP + TN$ |
| **Total Predicho** | $TP + FP$ | $FN + TN$ | $N_{\text{total}}$ |

---

### Fórmulas Exhaustivas y Desglose Conceptual

#### 1. Exactitud Global (Accuracy)
Proporción de instancias correctamente clasificadas sobre el total:
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
*Desglose:* Mide la corrección general. Inútil si hay fuerte asimetría de clases (ej. un clasificador que siempre predice negativo en un dataset con 99% de ceros obtendrá 99% de Accuracy siendo incapaz de detectar positivos).

#### 2. Precisión (Positive Predictive Value - PPV)
De todas las predicciones positivas realizadas, ¿qué fracción es verdaderamente positiva?
$$\text{Precision} = \frac{TP}{TP + FP}$$
*Desglose:* Penaliza los **Falsos Positivos**. Crítica en escenarios donde una falsa alarma es costosa (ej. clasificador de spam, bloqueo preventivo de transacciones legítimas).

#### 3. Recall / Sensibilidad (True Positive Rate - TPR)
De todas las instancias verdaderamente positivas existentes, ¿qué fracción logró identificar el modelo?
$$\text{Recall} = \frac{TP}{TP + FN}$$
*Desglose:* Penaliza los **Falsos Negativos**. Esencial en medicina, detección de fraude o alertas de seguridad, donde omitir un caso positivo puede resultar catastrófico.

#### 4. Puntuación $F_1$ (Media Armónica)
Balance o compromiso entre Precisión y Recall:
$$F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 TP}{2 TP + FP + FN}$$
*Desglose:* La media armónica penaliza fuertemente a un modelo si una de las dos métricas fundamentales se aproxima a cero.

#### 5. Especificidad (True Negative Rate - TNR)
De todas las instancias negativas reales, ¿qué fracción fue reconocida correctamente?
$$\text{Specificity} = \frac{TN}{TN + FP}$$

#### 6. Tasa de Falsos Positivos (False Positive Rate - FPR)
Fracción de negativos reales que fueron erróneamente clasificados como positivos:
$$\text{FPR} = \frac{FP}{TN + FP} = 1 - \text{Specificity}$$

#### 7. Tasa de Falsos Negativos (False Negative Rate - FNR)
Fracción de positivos reales omitidos por el clasificador:
$$\text{FNR} = \frac{FN}{TP + FN} = 1 - \text{Recall}$$

---

<a id="42-umbral-roc-auc"></a>
## 4.2 Umbrales de Decisión, Curva ROC y Métrica AUC

Un clasificador probabilístico asigna a una instancia $x$ una probabilidad estimada $\hat{p} = P(Y=1 \mid X=x)$.
La decisión binaria requiere un **umbral de corte** $\tau \in [0, 1]$:
$$\hat{y} = \begin{cases} 1 & \text{si } \hat{p} \ge \tau \\ 0 & \text{si } \hat{p} < \tau \end{cases}$$

Por defecto se emplea $\tau = 0.5$. Sin embargo:
* Si disminuimos $\tau$ (ej. $\tau = 0.2$), el modelo clasifica más muestras como positivas: **Aumenta el Recall pero empeora la Precisión (aumenta el FPR)**.
* Si aumentamos $\tau$ (ej. $\tau = 0.8$), el modelo es más conservador: **Aumenta la Precisión pero cae el Recall**.

### La Curva ROC (Receiver Operating Characteristic)
Gráfica paramétrica bidimensional que traza el $TPR$ (Eje Y) frente al $FPR$ (Eje X) para todos los posibles umbrales de decisión $\tau \in [0, 1]$.

### El Área Bajo la Curva (AUC - Area Under the Curve)
Cuantifica la capacidad global del modelo de separar las dos clases sin depender de un umbral arbitrario:
$$\text{AUC} = \int_0^1 \text{TPR}(\tau) \, d(\text{FPR}(\tau)) = P(\hat{p}(x^+) > \hat{p}(x^-))$$
* **Interpretación probabilística**: El AUC representa la probabilidad exacta de que una muestra positiva elegida al azar reciba un score de probabilidad predicho mayor que una muestra negativa elegida al azar.
* $\text{AUC} = 0.5$: Desempeño equivalente a lanzar una moneda (clasificador aleatorio, línea diagonal).
* $\text{AUC} = 1.0$: Separador perfecto (curva pasa por el vértice superior izquierdo $(0, 1)$).
"""
    cells.append(make_cell("markdown", c4_md1))

    c4_md2 = r"""<a id="43-implementacion-manual-metricas"></a>
### 4.3 Implementación Manual de Métricas y Validación con Scikit-Learn
Implementamos vectorialmente en NumPy el cálculo de $TP, TN, FP, FN$ y las 7 métricas derivadas para contrastarlas numéricamente contra las funciones de `sklearn.metrics`.
"""
    cells.append(make_cell("markdown", c4_md2))

    c4_code1 = """# =============================================================================
# IMPLEMENTACIÓN MANUAL DE MÉTRICAS Y VALIDACIÓN CON SCIKIT-LEARN
# =============================================================================
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_curve,
    auc,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

def calcular_metricas_clasificacion_manual(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    \"\"\"Calcula manualmente la matriz de confusión y todas las métricas de rendimiento.\"\"\"
    y_t = np.asarray(y_true, dtype=int)
    y_p = np.asarray(y_pred, dtype=int)
    
    tp = int(np.sum((y_t == 1) & (y_p == 1)))
    tn = int(np.sum((y_t == 0) & (y_p == 0)))
    fp = int(np.sum((y_t == 0) & (y_p == 1)))
    fn = int(np.sum((y_t == 1) & (y_p == 0)))
    
    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    fpr = fp / (tn + fp) if (tn + fp) > 0 else 0.0
    fnr = fn / (tp + fn) if (tp + fn) > 0 else 0.0
    
    return {
        'TP': tp, 'TN': tn, 'FP': fp, 'FN': fn,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1_score': f1,
        'Specificity': specificity,
        'FPR': fpr,
        'FNR': fnr
    }

# Prueba sintética con vectores conocidos
y_true_demo = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0])
y_pred_demo = np.array([1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0])

res_man = calcular_metricas_clasificacion_manual(y_true_demo, y_pred_demo)

# Validación cruzada contra Scikit-Learn
cm_sklearn = confusion_matrix(y_true_demo, y_pred_demo)
acc_sk = accuracy_score(y_true_demo, y_pred_demo)
prec_sk = precision_score(y_true_demo, y_pred_demo)
rec_sk = recall_score(y_true_demo, y_pred_demo)
f1_sk = f1_score(y_true_demo, y_pred_demo)

assert res_man['TP'] == cm_sklearn[1, 1] and res_man['TN'] == cm_sklearn[0, 0]
assert res_man['FP'] == cm_sklearn[0, 1] and res_man['FN'] == cm_sklearn[1, 0]
assert np.isclose(res_man['Accuracy'], acc_sk)
assert np.isclose(res_man['Precision'], prec_sk)
assert np.isclose(res_man['Recall'], rec_sk)
assert np.isclose(res_man['F1_score'], f1_sk)

print("✅ Validación de Métricas Manuales Exitosa:")
print(f"Matriz de Confusión -> TP: {res_man['TP']}, TN: {res_man['TN']}, FP: {res_man['FP']}, FN: {res_man['FN']}")
print(f"Accuracy:    {res_man['Accuracy']:.4f} (SciPy/Sklearn: {acc_sk:.4f})")
print(f"Precision:   {res_man['Precision']:.4f} (SciPy/Sklearn: {prec_sk:.4f})")
print(f"Recall:      {res_man['Recall']:.4f} (SciPy/Sklearn: {rec_sk:.4f})")
print(f"F1-score:    {res_man['F1_score']:.4f} (SciPy/Sklearn: {f1_sk:.4f})")
print(f"Specificity: {res_man['Specificity']:.4f} | FPR: {res_man['FPR']:.4f} | FNR: {res_man['FNR']:.4f}")
"""
    cells.append(make_cell("code", c4_code1))

    c4_md3 = r"""<a id="44-teoria-ensambles"></a>
## 4.4 Taxonomía de Ensambles: Bagging vs. Boosting vs. Stacking

Los métodos de ensamble combinan múltiples modelos base (estimadores individuales) para generar un predictor unificado que supera a cualquiera de sus componentes individuales. Teóricamente se fundamentan en el **Teorema del Jurado de Condorcet** y en la descomposición de **Sesgo-Varianza**:

### 1. Bagging (Bootstrap Aggregating - ej. Random Forest)
* **Mecanismo**: Genera $B$ subconjuntos de datos entrenables mediante muestreo aleatorio con reemplazo (**Bootstrap**). Entrena $B$ estimadores en paralelo de forma completamente independiente y promedia sus predicciones (o votación por mayoría).
* **Impacto**: Reduce drásticamente la **Varianza** del modelo sin incrementar el Sesgo.
* **Random Forest**: Incorpora adicionalmente aleatoriedad en el espacio de características (*Random Subspace*), seleccionando un subconjunto aleatorio de $\sqrt{p}$ variables en cada split para descorrelacionar los árboles.

### 2. Boosting (ej. AdaBoost, Gradient Boosting)
* **Mecanismo**: Entrenamiento **secuencial** iterativo. Cada nuevo modelo se especializa en corregir los errores cometidos por los modelos predecesores:
  * **AdaBoost**: Incrementa las ponderaciones de las muestras mal clasificadas en la siguiente iteración.
  * **Gradient Boosting**: Ajusta cada nuevo árbol a los **pseudo-residuos** (el gradiente negativo de la función de pérdida) del ensamble acumulado.
* **Impacto**: Reduce primordialmente el **Sesgo**, logrando fronteras de decisión complejas a partir de estimadores débiles (*weak learners*).

### 3. Stacking (Stacked Generalization)
* **Mecanismo**: Ensamble heterogéneo estructurado en dos niveles. Múltiples modelos base (ej. Random Forest, SVM, KNN) generan predicciones fuera de muestra (*out-of-fold*). Estas predicciones se convierten en las características de entrada para un **meta-modelo** superior (ej. Regresión Logística), el cual aprende a ponderar óptimamente a cada clasificador base.
"""
    cells.append(make_cell("markdown", c4_md3))

    c4_md4 = r"""<a id="45-implementacion-comparativa-ensambles"></a>
### 4.5 Implementación y Comparativa de 4 Ensambles con Curvas ROC Superpuestas
Entrenamos sobre el dataset de cáncer de mama 4 familias de ensambles:
1. `RandomForestClassifier` (Bagging)
2. `AdaBoostClassifier` (Boosting Adaptativo)
3. `GradientBoostingClassifier` (Boosting por Gradiente)
4. `StackingClassifier` (Meta-Aprendizaje)

Graficamos sus curvas ROC superpuestas en un único lienzo y tabulamos todas sus métricas en Test.
"""
    cells.append(make_cell("markdown", c4_md4))

    c4_code2 = """# =============================================================================
# IMPLEMENTACIÓN Y COMPARATIVA DE 4 ENSAMBLES CON CURVAS ROC SUPERPUESTAS
# =============================================================================
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
    StackingClassifier
)
from sklearn.linear_model import LogisticRegression

# Definición de los 4 clasificadores ensamble
modelos_ensamble = {
    'Random Forest (Bagging)': RandomForestClassifier(
        n_estimators=100, max_depth=5, random_state=RANDOM_STATE
    ),
    'AdaBoost (Boosting Adaptativo)': AdaBoostClassifier(
        n_estimators=100, learning_rate=0.8, random_state=RANDOM_STATE
    ),
    'Gradient Boosting (Boosting Gradiente)': GradientBoostingClassifier(
        n_estimators=100, max_depth=3, learning_rate=0.1, random_state=RANDOM_STATE
    ),
    'Stacking (Meta-Ensamble)': StackingClassifier(
        estimators=[
            ('rf', RandomForestClassifier(n_estimators=50, max_depth=4, random_state=RANDOM_STATE)),
            ('gb', GradientBoostingClassifier(n_estimators=50, max_depth=3, random_state=RANDOM_STATE)),
            ('lr', LogisticRegression(max_iter=1000, random_state=RANDOM_STATE))
        ],
        final_estimator=LogisticRegression(random_state=RANDOM_STATE),
        cv=5
    )
}

# Entrenamiento, recolección de métricas y cálculo de curvas ROC
tabla_resultados = []
curvas_roc = {}

plt.figure(figsize=(10, 7), dpi=100)
colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for (nombre, modelo), color in zip(modelos_ensamble.items(), colores):
    modelo.fit(X_train_c, y_train_c)
    
    y_pred = modelo.predict(X_test_c)
    y_proba = modelo.predict_proba(X_test_c)[:, 1]
    
    acc = accuracy_score(y_test_c, y_pred)
    prec = precision_score(y_test_c, y_pred)
    rec = recall_score(y_test_c, y_pred)
    f1 = f1_score(y_test_c, y_pred)
    
    fpr_vals, tpr_vals, _ = roc_curve(y_test_c, y_proba)
    roc_auc_val = auc(fpr_vals, tpr_vals)
    
    tabla_resultados.append({
        'Ensamble': nombre,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1-score': f1,
        'ROC-AUC': roc_auc_val
    })
    
    plt.plot(fpr_vals, tpr_vals, color=color, lw=2.2, label=f'{nombre} (AUC = {roc_auc_val:.4f})')

# Trazar diagonal de azar de referencia
plt.plot([0, 1], [0, 1], color='navy', lw=1.5, linestyle='--', label='Clasificador Aleatorio (AUC = 0.5000)')

plt.xlim([-0.01, 1.0])
plt.ylim([0.0, 1.02])
plt.xlabel('Tasa de Falsos Positivos (FPR = 1 - Specificity)')
plt.ylabel('Tasa de Verdaderos Positivos (TPR = Recall)')
plt.title('Comparativa de Curvas ROC Superpuestas de los 4 Ensambles (Dataset Breast Cancer)')
plt.legend(loc='lower right', frameon=True)
plt.tight_layout()
plt.show()

# Mostrar tabla comparativa de métricas formateada
df_metricas_ensambles = pd.DataFrame(tabla_resultados).sort_values(by='ROC-AUC', ascending=False)
print("📊 Resumen Comparativo de Desempeño en Test:")
print(df_metricas_ensambles.to_string(index=False))
"""
    cells.append(make_cell("code", c4_code2))

    # =========================================================================
    # CLASE 5: DESBALANCE DE CLASES, FEATURE SELECTION Y SISTEMAS DE RECOMENDACIÓN
    # =========================================================================
    c5_md1 = r"""<a id="clase-5"></a>
# 5. Clase 5: Desbalance de Clases, Feature Selection y Sistemas de Recomendación

<a id="51-desbalance-clases"></a>
## 5.1 Desbalance de Clases: Problema y Soluciones Metodológicas

En problemas reales (detección de fraudes financieros, fallas mecánicas, enfermedades raras), una clase mayoritaria comprende entre el $95\%$ y el $99.9\%$ de los datos. Si un modelo clasifica todo como clase mayoritaria, alcanzará $99\%$ de Accuracy pero será enteramente inútil (**Paradoja de la Exactitud**).

Para abordar este fenómeno existen tres familias principales de técnicas:

---

### 1. Técnicas de Undersampling (Submuestreo)
Reducen el tamaño de la clase mayoritaria para igualar a la minoritaria.
* **Random Undersampling**: Elimina aleatoriamente muestras de la clase mayoritaria. Desventaja: Descarte de información potencialmente crítica.
* **Tomek Links**: Identifica pares de observaciones de clases opuestas que son los vecinos más cercanos mutuos. Su remoción despeja y limpia la frontera de decisión en zonas de solapamiento.
* **NearMiss (v1, v2, v3)**: Algoritmo heurístico que conserva muestras mayoritarias basándose en su distancia media a los $k$ vecinos más cercanos de la clase minoritaria.

---

### 2. Técnicas de Oversampling (Sobremuestreo)
Incrementan el volumen de la clase minoritaria.
* **Random Oversampling**: Duplica copias idénticas de la minoría. Desventaja: Riesgo severo de sobreajuste por memorización de puntos discretos.
* **SMOTE (Synthetic Minority Over-sampling Technique - Chawla et al., 2002)**: Genera muestras sintéticas plausibles mediante interpolación vectorial en el espacio de características:
$$x_{\text{new}} = x_i + \lambda \cdot (x_{zi} - x_i), \quad \lambda \sim U(0, 1)$$

* **Desglose de términos:**
  * $x_i$: Una observación arbitraria perteneciente a la clase minoritaria.
  * $x_{zi}$: Uno de los $k$ vecinos más cercanos de $x_i$ que pertenece a su misma clase minoritaria.
  * $(x_{zi} - x_i)$: Vector de dirección geométrica que une a ambos puntos en $\mathbb{R}^n$.
  * $\lambda \in [0, 1]$: Escalar aleatorio obtenido de una distribución uniforme continua.
  * $x_{\text{new}}$: Nuevo punto sintético generado a lo largo del segmento que une ambas muestras reales, preservando la continuidad del espacio.

---

### 3. Ponderación de Función de Pérdida (Cost-Sensitive Learning)
Modifica la función objetivo del algoritmo penalizando los errores sobre la clase minoritaria proporcionalmente a su escasez:
$$w_c = \frac{N}{C \cdot N_c}$$

* **Desglose de términos:**
  * $N$: Número total de muestras en el conjunto de entrenamiento.
  * $C$: Número de clases ($C = 2$ en binario).
  * $N_c$: Número de muestras pertenecientes a la clase $c$.
  * En Scikit-Learn se implementa nativamente con el hiperparámetro `class_weight='balanced'`.
"""
    cells.append(make_cell("markdown", c5_md1))

    c5_md2 = r"""<a id="52-mini-smote-cost-sensitive"></a>
### 5.2 Implementación Práctica: Mini-SMOTE Manual y Ponderación de Clases
Generamos un dataset sintético con desbalance severo ($95\% - 5\%$). Implementamos artesanalmente el algoritmo SMOTE vectorial en NumPy utilizando `NearestNeighbors` y contrastamos el desempeño frente al modelo base y al enfoque de costo ponderado (`class_weight='balanced'`).
"""
    cells.append(make_cell("markdown", c5_md2))

    c5_code1 = """# =============================================================================
# IMPLEMENTACIÓN PRÁCTICA: MINI-SMOTE MANUAL Y PONDERACIÓN DE CLASES
# =============================================================================
from sklearn.datasets import make_classification
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LogisticRegression

# 1. Creación de Dataset Sintético Fuertemente Desbalanceado (95% Clase 0, 5% Clase 1)
X_imb, y_imb = make_classification(
    n_samples=1200,
    n_features=6,
    n_informative=4,
    n_redundant=1,
    weights=[0.95, 0.05],
    random_state=RANDOM_STATE
)

X_train_imb, X_test_imb, y_train_imb, y_test_imb = train_test_split(
    X_imb, y_imb, test_size=0.30, random_state=RANDOM_STATE, stratify=y_imb
)

print(f"📊 Distribución en Train: Clase 0 = {np.sum(y_train_imb == 0)} | Clase 1 = {np.sum(y_train_imb == 1)} ({np.mean(y_train_imb == 1)*100:.1f}%)")

# 2. Implementación Manual Didáctica de Mini-SMOTE
def mini_smote_manual(X_minoria: np.ndarray, n_sinteticos: int, k_vecinos: int = 5, seed: int = 42) -> np.ndarray:
    \"\"\"Genera n_sinteticos puntos interpolados a partir de los k vecinos más cercanos de la minoría.\"\"\"
    rng = np.random.RandomState(seed)
    n_muestras = len(X_minoria)
    if n_muestras <= k_vecinos:
        k_vecinos = max(1, n_muestras - 1)
        
    nn = NearestNeighbors(n_neighbors=k_vecinos + 1, metric='euclidean').fit(X_minoria)
    _, indices = nn.kneighbors(X_minoria)
    
    sinteticos = []
    for _ in range(n_sinteticos):
        idx_base = rng.randint(0, n_muestras)
        x_i = X_minoria[idx_base]
        
        idx_vecino = rng.choice(indices[idx_base, 1:])
        x_zi = X_minoria[idx_vecino]
        
        lam = rng.uniform(0.0, 1.0)
        x_new = x_i + lam * (x_zi - x_i)
        sinteticos.append(x_new)
        
    return np.array(sinteticos)

# Generar muestras sintéticas para balancear la minoría en Train
X_minority_train = X_train_imb[y_train_imb == 1]
n_a_generar = np.sum(y_train_imb == 0) - np.sum(y_train_imb == 1)
X_synth = mini_smote_manual(X_minority_train, n_sinteticos=n_a_generar, k_vecinos=4, seed=RANDOM_STATE)
y_synth = np.ones(len(X_synth), dtype=int)

X_train_resampled = np.vstack([X_train_imb, X_synth])
y_train_resampled = np.concatenate([y_train_imb, y_synth])

# 3. Entrenamiento Comparativo con Regresión Logística
clf_base = LogisticRegression(random_state=RANDOM_STATE).fit(X_train_imb, y_train_imb)
clf_smote = LogisticRegression(random_state=RANDOM_STATE).fit(X_train_resampled, y_train_resampled)
clf_weighted = LogisticRegression(class_weight='balanced', random_state=RANDOM_STATE).fit(X_train_imb, y_train_imb)

# Evaluación sobre el conjunto de test original
rec_base = recall_score(y_test_imb, clf_base.predict(X_test_imb))
rec_smote = recall_score(y_test_imb, clf_smote.predict(X_test_imb))
rec_weight = recall_score(y_test_imb, clf_weighted.predict(X_test_imb))

f1_base = f1_score(y_test_imb, clf_base.predict(X_test_imb))
f1_smote = f1_score(y_test_imb, clf_smote.predict(X_test_imb))
f1_weight = f1_score(y_test_imb, clf_weighted.predict(X_test_imb))

df_res_desbalance = pd.DataFrame({
    'Estrategia': ['1. Base (Sin Balancear)', '2. Mini-SMOTE Manual', '3. class_weight="balanced"'],
    'Recall Clase Minoritaria': [rec_base, rec_smote, rec_weight],
    'F1-score Clase Minoritaria': [f1_base, f1_smote, f1_weight]
})
print("\\n⚖️ Comparativa de Tratamiento de Desbalance en Test:")
print(df_res_desbalance.to_string(index=False))
"""
    cells.append(make_cell("code", c5_code1))

    c5_md3 = r"""<a id="53-feature-selection"></a>
## 5.3 Selección de Características: Filtro, Wrapper y Embebido (Lasso L1)

La selección de características reduce la complejidad computacional, mitiga la maldición de la dimensionalidad (*Curse of Dimensionality*) y previene el sobreajuste al eliminar variables irrelevantes o redundantes.

Se clasifican en tres familias metodológicas:

### 1. Métodos de Filtro (Filter)
Evalúan propiedades estadísticas de los datos con independencia del modelo predictivo:
* **Umbral de Varianza (Variance Threshold)**: Remueve variables cuasi-constantes cuya varianza muestral $\text{Var}(X) < \tau$.
* **ANOVA F-test (`f_classif`)**: Evalúa si la media de una característica numérica difiere significativamente entre las categorías de la variable objetivo calculando el estadístico $F$:
$$F = \frac{\text{Varianza Entre Grupos (Between-group Variance)}}{\text{Varianza Intra-Grupo (Within-group Variance)}} = \frac{\text{MSB}}{\text{MSW}}$$
* **Chi-cuadrado ($\chi^2$)**: Prueba de independencia estadística para atributos categóricos.
* **Correlación de Pearson**: Identifica colinealidad entre pares de variables numéricas.

### 2. Métodos Wrapper (Envolventes)
Utilizan un estimador de aprendizaje automático como juez para evaluar combinaciones de subconjuntos de atributos:
* **RFE (Recursive Feature Elimination)**: Ajusta el modelo iterativamente con todas las variables, cuantifica la importancia de cada una (pesos o coeficientes) y descarta recursivamente el atributo menos relevante hasta alcanzar el número objetivo.

### 3. Métodos Embebidos (Embedded)
La selección se produce intrínsecamente como parte del proceso de optimización del algoritmo:
* **Regularización Lasso ($L_1$)**: Agrega a la función de pérdida una penalización proporcional a la norma $L_1$ de los coeficientes:
$$\min_{\mathbf{w}} \left\{ \frac{1}{2N} \|\mathbf{y} - \mathbf{X}\mathbf{w}\|_2^2 + \alpha \sum_{j=1}^p |w_j| \right\}$$
* **Propiedad de Esparcidad**: Debido a la geometría poliédrica con vértices angulares de la bola unitaria $L_1$, el gradiente fuerza a los coeficientes de variables irrelevantes a anularse **exactamente a cero**, realizando selección automática de variables.
"""
    cells.append(make_cell("markdown", c5_md3))

    c5_code2 = """# =============================================================================
# IMPLEMENTACIÓN DE SELECCIÓN DE CARACTERÍSTICAS (FILTRO, WRAPPER Y LASSO)
# =============================================================================
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif, RFE
from sklearn.linear_model import Lasso

# Generación de dataset con 15 variables: 5 informativas, 2 redundantes, 8 ruido aleatorio
np.random.seed(RANDOM_STATE)
X_fs, y_fs = make_classification(
    n_samples=400,
    n_features=15,
    n_informative=5,
    n_redundant=2,
    n_repeated=0,
    random_state=RANDOM_STATE
)
nombres_vars = [f"Feature_{i+1:02d}" for i in range(15)]

# 1. Filtro: Variance Threshold (eliminación de variables con varianza insignificante)
selector_var = VarianceThreshold(threshold=0.2)
selector_var.fit(X_fs)
vars_retenidas_var = [nombres_vars[i] for i in selector_var.get_support(indices=True)]

# 2. Filtro: SelectKBest con ANOVA F-test (las mejores 5 variables)
selector_kbest = SelectKBest(score_func=f_classif, k=5)
selector_kbest.fit(X_fs, y_fs)
vars_retenidas_kbest = [nombres_vars[i] for i in selector_kbest.get_support(indices=True)]

# 3. Wrapper: Recursive Feature Elimination (RFE) con Regresión Logística
selector_rfe = RFE(estimator=LogisticRegression(random_state=RANDOM_STATE), n_features_to_select=5)
selector_rfe.fit(X_fs, y_fs)
vars_retenidas_rfe = [nombres_vars[i] for i in selector_rfe.get_support(indices=True)]

# 4. Embebido: Regularización Lasso (L1) observando coeficientes anulados
lasso = Lasso(alpha=0.08, random_state=RANDOM_STATE)
lasso.fit(X_fs, y_fs)
vars_retenidas_lasso = [nombres_vars[i] for i, coef in enumerate(lasso.coef_) if abs(coef) > 1e-4]

print("🔬 Resultados de Selección de Características:")
print(f"1. Filtro Varianza (>0.2) : {len(vars_retenidas_var)} variables retenidas -> {vars_retenidas_var}")
print(f"2. Filtro ANOVA F-test    : Top-5 variables -> {vars_retenidas_kbest}")
print(f"3. Wrapper RFE            : Top-5 variables -> {vars_retenidas_rfe}")
print(f"4. Embebido Lasso (L1)    : {len(vars_retenidas_lasso)} variables con coef != 0 -> {vars_retenidas_lasso}")

# Gráfico de coeficientes Lasso que muestra esparcidad
plt.figure(figsize=(10, 4))
plt.stem(range(15), lasso.coef_, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xticks(range(15), nombres_vars, rotation=45)
plt.title('Esparcidad de Coeficientes mediante Regularización Lasso (L1)')
plt.ylabel('Valor del Coeficiente w_j')
plt.axhline(0, color='red', linestyle='--')
plt.tight_layout()
plt.show()
"""
    cells.append(make_cell("code", c5_code2))

    c5_md4 = r"""<a id="54-sistemas-recomendacion"></a>
## 5.4 Sistemas de Recomendación: Similitud Coseno y Filtrado Colaborativo

Los sistemas de recomendación asisten a usuarios en la toma de decisiones dentro de catálogos masivos. Se dividen en dos paradigmas fundamentales:

### 1. Recomendación Basada en Contenido (Content-Based)
Recomienda ítems similares a los que un usuario consumió y calificó positivamente en el pasado. Se modela cada ítem como un vector de atributos y se evalúa la **Similitud Coseno**:
$$\text{Sim}_{\cos}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2}$$

---

### 2. Filtrado Colaborativo Basado en Usuarios (User-Based Collaborative Filtering)
Aprovecha el comportamiento colectivo histórico sin requerir atributos descriptivos de los ítems. Asume que usuarios con preferencias similares en el pasado tenderán a concordar en el futuro.

Para predecir la calificación desconocida del usuario activo $u$ sobre el ítem $i$, se utiliza la **Fórmula con Normalización por la Media (Mean-Centering)**:
$$\hat{r}_{u, i} = \bar{r}_u + \frac{\sum_{v \in U_i} \text{Sim}(u, v) \cdot (r_{v, i} - \bar{r}_v)}{\sum_{v \in U_i} |\text{Sim}(u, v)|}$$

---

### Desglose Minucioso de Cada Término de la Fórmula
* $\hat{r}_{u, i}$: Calificación predicha que el usuario activo $u$ otorgaría al ítem aún no visto $i$.
* $\bar{r}_u = \frac{1}{|I_u|} \sum_{j \in I_u} r_{u, j}$: Calificación promedio histórica otorgada por el usuario $u$ a todos los ítems que ha puntuado. Representa su **sesgo de calificación basal** (un usuario optimista asigna en promedio 4.5; uno crítico asigna 2.5).
* $U_i$: Conjunto de usuarios similares a $u$ que **efectivamente han calificado** el ítem de interés $i$.
* $\text{Sim}(u, v)$: Coeficiente de similitud (Coseno centrado o Correlación de Pearson) entre los usuarios $u$ y $v$, calculado estrictamente sobre los ítems co-calificados por ambos.
* $r_{v, i}$: Calificación real que el vecino similar $v$ otorgó al ítem $i$.
* $\bar{r}_v$: Calificación promedio histórica del vecino $v$.
* $(r_{v, i} - \bar{r}_v)$: **Desviación respecto a la media del vecino**. Indica si al vecino le agradó el ítem por encima o por debajo de su estándar habitual.
* $\sum_{v \in U_i} |\text{Sim}(u, v)|$: Factor de normalización ponderado que garantiza que la predicción combinada permanezca dentro de la escala numérica natural de calificaciones (ej. $[1, 5]$).
"""
    cells.append(make_cell("markdown", c5_md4))

    c5_md5 = r"""<a id="55-recomendador-contenido"></a>
### 5.5 Implementación 1: Recomendador Basado en Contenido
Construimos un catálogo de películas caracterizado por géneros binarios y evaluamos la afinidad de un usuario mediante similitud coseno con su vector de preferencias.
"""
    cells.append(make_cell("markdown", c5_md5))

    c5_code3 = """# =============================================================================
# IMPLEMENTACIÓN 1: RECOMENDADOR BASADO EN CONTENIDO
# =============================================================================
from sklearn.metrics.pairwise import cosine_similarity

# Matriz de 7 películas y 6 géneros binarios
peliculas = ['Inception', 'The Dark Knight', 'Interstellar', 'Toy Story', 'Finding Nemo', 'Coco', 'The Notebook']
generos = ['Accion', 'Aventura', 'Sci-Fi', 'Animacion', 'Drama', 'Romance']

matriz_items = np.array([
    [1, 1, 1, 0, 0, 0],  # Inception (Acción, Aventura, Sci-Fi)
    [1, 0, 0, 0, 1, 0],  # The Dark Knight (Acción, Drama)
    [0, 1, 1, 0, 1, 0],  # Interstellar (Aventura, Sci-Fi, Drama)
    [0, 1, 0, 1, 0, 0],  # Toy Story (Aventura, Animación)
    [0, 1, 0, 1, 0, 0],  # Finding Nemo (Aventura, Animación)
    [0, 0, 0, 1, 1, 0],  # Coco (Animación, Drama)
    [0, 0, 0, 0, 1, 1]   # The Notebook (Drama, Romance)
])
df_catalogo = pd.DataFrame(matriz_items, index=peliculas, columns=generos)

# Perfil del usuario activo (preferencia por Sci-Fi y Aventura)
perfil_usuario = np.array([[0.2, 0.8, 1.0, 0.0, 0.4, 0.0]])

# Cómputo de similitud coseno entre el perfil del usuario y el catálogo
similitudes = cosine_similarity(perfil_usuario, df_catalogo.values).flatten()

df_ranking_contenido = pd.DataFrame({
    'Película': peliculas,
    'Afinidad Predicha (Coseno)': similitudes
}).sort_values(by='Afinidad Predicha (Coseno)', ascending=False)

print("🎬 Recomendaciones Basadas en Contenido:")
print(df_ranking_contenido.to_string(index=False))
"""
    cells.append(make_cell("code", c5_code3))

    c5_md6 = r"""<a id="56-filtrado-colaborativo-paso-a-paso"></a>
### 5.6 Implementación 2: Filtrado Colaborativo Manual Paso a Paso con Normalización por Media
Modelamos una matriz de interacción Usuario-Ítem con valores faltantes (`NaN`). Calculamos las medias históricas por usuario, las similitudes de Pearson sobre ítems en común y computamos analíticamente cada término de la sumatoria para predecir la calificación de ítems no vistos y ordenar el ranking final de recomendación.
"""
    cells.append(make_cell("markdown", c5_md6))

    c5_code4 = """# =============================================================================
# IMPLEMENTACIÓN 2: FILTRADO COLABORATIVO PASO A PASO (USER-BASED CON MEDIA)
# =============================================================================

# Matriz de Calificaciones Usuario - Ítem (con valores NaN en ítems no evaluados)
usuarios = ['Alicia', 'Bernardo', 'Carlos', 'Diana', 'Esteban']
items = ['Inception', 'Interstellar', 'The Dark Knight', 'Toy Story', 'Finding Nemo', 'Coco']

matriz_ratings = np.array([
    [5.0, 5.0, 4.0, np.nan, 1.0, np.nan],  # Alicia (Fan de Nolan/Sci-Fi)
    [4.0, 5.0, np.nan, 2.0, np.nan, 1.0],  # Bernardo (Fan de Nolan/Sci-Fi)
    [np.nan, 2.0, 3.0, 5.0, 4.0, np.nan],  # Carlos (Gusto infantil/animación)
    [1.0, np.nan, 2.0, 5.0, 4.0, 5.0],     # Diana (Fan de animación)
    [2.0, 1.0, 1.0, 4.0, 5.0, 5.0]         # Esteban (Fan de animación)
])

df_ratings = pd.DataFrame(matriz_ratings, index=usuarios, columns=items)
print("📊 Matriz de Interacción Usuario - Ítem Original (Ratings de 1 a 5):")
print(df_ratings)

# Predicción paso a paso para Alicia sobre 'Toy Story'
usuario_activo = 'Alicia'
item_objetivo = 'Toy Story'

# 1. Medias históricas por usuario (r_bar)
medias_usuarios = df_ratings.mean(axis=1)
print(f"\\n📈 Calificaciones Promedio Históricas:")
for u, m in medias_usuarios.items():
    print(f"  {u}: {m:.3f}")

# 2. Función para calcular similitud centrada (Pearson Correlation) entre dos usuarios
def calcular_similitud_usuarios(df: pd.DataFrame, u1: str, u2: str) -> float:
    mascara_comun = df.loc[u1].notnull() & df.loc[u2].notnull()
    if np.sum(mascara_comun) < 2:
        return 0.0
    
    r1 = df.loc[u1, mascara_comun].values
    r2 = df.loc[u2, mascara_comun].values
    
    m1 = medias_usuarios[u1]
    m2 = medias_usuarios[u2]
    
    centrado1 = r1 - m1
    centrado2 = r2 - m2
    
    norm1 = np.linalg.norm(centrado1)
    norm2 = np.linalg.norm(centrado2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(np.dot(centrado1, centrado2) / (norm1 * norm2))

# 3. Aplicar la fórmula exacta para predecir la calificación de Toy Story para Alicia
media_u = medias_usuarios[usuario_activo]
numerador = 0.0
denominador = 0.0

print(f"\\n🧮 Desglose analítico de la sumatoria para '{usuario_activo}' en '{item_objetivo}':")

for vecino in usuarios:
    if vecino == usuario_activo:
        continue
    if pd.notnull(df_ratings.loc[vecino, item_objetivo]):
        sim = calcular_similitud_usuarios(df_ratings, usuario_activo, vecino)
        r_vi = df_ratings.loc[vecino, item_objetivo]
        media_v = medias_usuarios[vecino]
        desviacion = r_vi - media_v
        
        if sim > 0:
            numerador += sim * desviacion
            denominador += abs(sim)
            print(f"  • Vecino {vecino:8s} | Sim={sim:+.4f} | r_vi={r_vi} | Media_v={media_v:.3f} | Desviación={desviacion:+.3f}")
        else:
            print(f"  • Vecino {vecino:8s} | Sim={sim:+.4f} (Descartado por similitud <= 0)")

prediccion_alicia = media_u + (numerador / denominador) if denominador > 0 else media_u
print(f"\\n🎯 Resultado Numérico:")
print(f"Predicción r_hat({usuario_activo}, {item_objetivo}) = {media_u:.3f} + ({numerador:.4f} / {denominador:.4f}) = {prediccion_alicia:.2f}")

# 4. Predicción para todos los ítems no calificados de Alicia para generar su Ranking
items_no_vistos = df_ratings.columns[df_ratings.loc[usuario_activo].isnull()]
ranking_alicia = []

for item in items_no_vistos:
    num, den = 0.0, 0.0
    for v in usuarios:
        if v != usuario_activo and pd.notnull(df_ratings.loc[v, item]):
            sim = calcular_similitud_usuarios(df_ratings, usuario_activo, v)
            if sim > 0:
                num += sim * (df_ratings.loc[v, item] - medias_usuarios[v])
                den += abs(sim)
    pred = media_u + (num / den) if den > 0 else media_u
    ranking_alicia.append({'Ítem Recomendable': item, 'Rating Predicho': pred})

df_final_rec = pd.DataFrame(ranking_alicia).sort_values(by='Rating Predicho', ascending=False)
print(f"\\n🏆 Ranking Final de Recomendaciones para {usuario_activo}:")
print(df_final_rec.to_string(index=False))
"""
    cells.append(make_cell("code", c5_code4))

    # =========================================================================
    # SÍNTESIS Y CONCLUSIÓN PEDAGÓGICA FINAL
    # =========================================================================
    conclusion_md = r"""---

## 🏁 Síntesis Integral y Conclusiones Generales (Clases 1 a 5)

A lo largo de este Cuaderno Maestro hemos recorrido el núcleo matemático y algorítmico del aprendizaje automático supervisado y la preparación de datos:

1. **Clase 1 (Métricas de Distancia)**: Comprendimos que toda noción de proximidad geométrica en Machine Learning ($L_1$, $L_2$, $L_p$, Coseno) induce sesgos inductivos específicos sobre el espacio de estados. La distancia Coseno es fundamental para datos no acotados e invariantes a magnitud, mientras que Manhattan ofrece robustez ante outliers.
2. **Clase 2 (EDA y Preprocesamiento)**: La rigurosidad metodológica exige blindar el conjunto de prueba para evitar **Data Leakage**. La estandarización Z-score y la normalización Min-Max preparan a los datos para que algoritmos sensibles a distancias como KNN operen de manera equilibrada.
3. **Clase 3 (Árboles de Decisión)**: Las métricas de impureza (Entropía y Gini) guían la partición óptima del espacio. Gini provee eficiencia computacional equivalente a Entropía sin evaluar funciones trascendentales, siendo el estándar de CART.
4. **Clase 4 (Métricas y Ensambles)**: Diagnosticar modelos requiere trascender el Accuracy mediante matrices de confusión, curvas ROC y AUC. Los ensambles explotan el principio de complementariedad: **Bagging** mitiga la varianza promediando modelos independientes; **Boosting** reduce el sesgo iterando sobre los errores residuales; **Stacking** optimiza la combinación de predictores heterogéneos.
5. **Clase 5 (Desbalance, Selección y Recomendación)**: SMOTE sintetiza muestras interpolando sobre vectores directores en la minoría y la ponderación de costos compensa la disparidad en la función de pérdida. La regularización Lasso ($L_1$) elimina coeficientes espurios por esparcidad geométrica. Finalmente, el filtrado colaborativo con normalización por la media desacopla los sesgos intrínsecos de los usuarios para estimar valoraciones con alta fidelidad.

---
**Cátedra de Minería de Datos y Aprendizaje Automático — Facultad de Informática, UNLP (2026)**
"""
    cells.append(make_cell("markdown", conclusion_md))

    # Construcción final del objeto Notebook
    notebook_dict = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    return notebook_dict


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sesiones_dir = os.path.dirname(script_dir)
    output_path = os.path.join(sesiones_dir, "Master_DM_ML_Clases_1_a_5.ipynb")

    print("🚀 Iniciando generación del Notebook Maestro...")
    nb_dict = build_master_notebook()

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(nb_dict, f, indent=1, ensure_ascii=False)

    total_cells = len(nb_dict["cells"])
    code_cells = sum(1 for c in nb_dict["cells"] if c["cell_type"] == "code")
    md_cells = sum(1 for c in nb_dict["cells"] if c["cell_type"] == "markdown")

    print(f"✨ ¡Notebook generado exitosamente en:")
    print(f"   {output_path}")
    print(f"📊 Estadísticas del archivo:")
    print(f"   • Total de Celdas: {total_cells}")
    print(f"   • Celdas de Código: {code_cells}")
    print(f"   • Celdas de Markdown: {md_cells}")
    print(f"   • Versión de Formato: nbformat {nb_dict['nbformat']}.{nb_dict['nbformat_minor']}")


if __name__ == "__main__":
    main()
