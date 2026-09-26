#!/usr/bin/env python3
"""
🧪 Práctica & Autoevaluación — Lección 01: Fundamentos de IA & Machine Learning
Cátedra: Minería de Datos y Aprendizaje Automático — UNLP Informática (2026)

Este script contiene las implementaciones vectorizadas en NumPy y la clase de
evaluación para validar tus funciones directamente en la terminal.
Ejecución: python3 practica_clase1.py
"""

import sys
import numpy as np

# Colores ANSI para salida elegante en terminal
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


# =====================================================================
# DESAFÍO 1: MÉTRICAS DE DISTANCIA VECTORIZADAS CON NUMPY
# =====================================================================

def distancia_euclidiana(p, q):
    """
    Calcula la distancia Euclidiana (L2) entre dos vectores p y q.
    Fórmula: d2(p, q) = sqrt( sum( (p_i - q_i)^2 ) )
    """
    diff = np.asarray(p, dtype=float) - np.asarray(q, dtype=float)
    return float(np.sqrt(np.sum(diff ** 2)))


def distancia_manhattan(p, q):
    """
    Calcula la distancia Manhattan (L1) entre dos vectores p y q.
    Fórmula: d1(p, q) = sum( |p_i - q_i| )
    """
    diff = np.asarray(p, dtype=float) - np.asarray(q, dtype=float)
    return float(np.sum(np.abs(diff)))


def distancia_minkowski(p, q, p_order=3):
    """
    Calcula la distancia Minkowski generalizada de orden p_order.
    Fórmula: dp(p, q) = ( sum( |p_i - q_i|^p ) )^(1/p)
    """
    if p_order <= 0:
        raise ValueError("El orden p debe ser estrictamente positivo.")
    diff = np.asarray(p, dtype=float) - np.asarray(q, dtype=float)
    return float(np.sum(np.abs(diff) ** p_order) ** (1.0 / p_order))


# =====================================================================
# DESAFÍO 2: ESCALAMIENTO Y ESTANDARIZACIÓN MANUAL
# =====================================================================

def z_score_estandarizar(X):
    """
    Estandariza una matriz X (muestras x características) a media 0 y varianza 1.
    Fórmula: z = (x - mu) / sigma
    """
    X_arr = np.asarray(X, dtype=float)
    mu = np.mean(X_arr, axis=0)
    sigma = np.std(X_arr, axis=0)
    # Evitar división por cero si la desviación es nula (columna constante)
    sigma_safe = np.where(sigma == 0, 1.0, sigma)
    return (X_arr - mu) / sigma_safe, mu, sigma


def min_max_escalar(X, feature_range=(0, 1)):
    """
    Escala la matriz X al rango especificado [min, max], por defecto [0, 1].
    Fórmula: x_scaled = (x - x_min) / (x_max - x_min)
    """
    X_arr = np.asarray(X, dtype=float)
    x_min = np.min(X_arr, axis=0)
    x_max = np.max(X_arr, axis=0)
    denom = np.where(x_max == x_min, 1.0, x_max - x_min)
    X_std = (X_arr - x_min) / denom
    r_min, r_max = feature_range
    return X_std * (r_max - r_min) + r_min


# =====================================================================
# DESAFÍO 3: CLASIFICADOR KNN DESDE CERO (API COMPATIBLE)
# =====================================================================

class KNNClassifierScratch:
    """
    Clasificador K-Nearest Neighbors implementado en Python puro con NumPy.
    Soporta distancias Euclidiana y Manhattan, y votación uniforme o ponderada.
    """
    def __init__(self, k=3, metric='euclidean', weights='uniform'):
        self.k = k
        self.metric = metric
        self.weights = weights
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        Fase de entrenamiento (Lazy Learner): almacena las referencias en memoria.
        Complejidad temporal: O(1)
        """
        self.X_train = np.asarray(X, dtype=float)
        self.y_train = np.asarray(y)
        return self

    def predict(self, X):
        """
        Fase de inferencia: calcula distancias a todas las muestras para cada consulta.
        Complejidad temporal: O(N_test * N_train * d)
        """
        X = np.asarray(X, dtype=float)
        return np.array([self._predict_single(x) for x in X])

    def _predict_single(self, x):
        # 1. Distancias vectorizadas hacia todo el set de entrenamiento
        if self.metric == 'euclidean':
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
        elif self.metric == 'manhattan':
            distances = np.sum(np.abs(self.X_train - x), axis=1)
        else:
            raise ValueError(f"Métrica no soportada: {self.metric}")

        # 2. Encontrar los k vecinos más cercanos
        k_indices = np.argsort(distances)[:self.k]
        k_labels = self.y_train[k_indices]
        k_dists = distances[k_indices]

        # 3. Votación
        if self.weights == 'uniform':
            classes, counts = np.unique(k_labels, return_counts=True)
            return classes[np.argmax(counts)]
        elif self.weights == 'distance':
            eps = 1e-6
            w = 1.0 / (k_dists + eps)
            scores = {}
            for label, weight in zip(k_labels, w):
                scores[label] = scores.get(label, 0.0) + weight
            return max(scores, key=scores.get)
        else:
            raise ValueError(f"Ponderación desconocida: {self.weights}")


# =====================================================================
# SUITE DE PRUEBAS AUTOMATIZADA
# =====================================================================

def run_tests():
    print(f"\n{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}  🔬 VALIDACIÓN AUTOMATIZADA · CLASE 1: FUNDAMENTOS IA & ML (UNLP){RESET}")
    print(f"{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}\n")

    tests_passed = 0
    total_tests = 6

    # Test 1: Distancia Euclidiana
    try:
        p = [0, 0]
        q = [3, 4]
        res = distancia_euclidiana(p, q)
        assert np.isclose(res, 5.0), f"Esperado 5.0, obtenido {res}"
        print(f"  [{GREEN}✓{RESET}] Test 1: Distancia Euclidiana L2 correcta (Pitágoras 3-4-5 -> 5.0)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 1 Falló: {e}")

    # Test 2: Distancia Manhattan
    try:
        p = [1, 2, 5]
        q = [4, 6, 8]
        # |1-4| + |2-6| + |5-8| = 3 + 4 + 3 = 10
        res = distancia_manhattan(p, q)
        assert np.isclose(res, 10.0), f"Esperado 10.0, obtenido {res}"
        print(f"  [{GREEN}✓{RESET}] Test 2: Distancia Manhattan L1 correcta (|Δx| + |Δy| + |Δz| -> 10.0)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 2 Falló: {e}")

    # Test 3: Minkowski equivalencias
    try:
        p = [2, 3]
        q = [5, 7]
        mink_1 = distancia_minkowski(p, q, p_order=1)
        manh = distancia_manhattan(p, q)
        mink_2 = distancia_minkowski(p, q, p_order=2)
        eucl = distancia_euclidiana(p, q)
        assert np.isclose(mink_1, manh), "Minkowski(p=1) debe ser idéntico a Manhattan"
        assert np.isclose(mink_2, eucl), "Minkowski(p=2) debe ser idéntico a Euclidiana"
        print(f"  [{GREEN}✓{RESET}] Test 3: Minkowski satisface equivalencia formal para p=1 y p=2")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 3 Falló: {e}")

    # Test 4: Estandarización Z-score
    try:
        datos = np.array([[10.0, 1000.0], [20.0, 2000.0], [30.0, 3000.0]])
        z, mu, sigma = z_score_estandarizar(datos)
        assert np.allclose(np.mean(z, axis=0), [0.0, 0.0]), "La media de z debe ser 0"
        assert np.allclose(np.std(z, axis=0), [1.0, 1.0]), "La desviación de z debe ser 1"
        print(f"  [{GREEN}✓{RESET}] Test 4: Estandarización Z-score produce media=0.0 y desv=1.0 exactas")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 4 Falló: {e}")

    # Test 5: KNN Scratch - Votación Uniforme
    try:
        X_toy = np.array([
            [1.0, 1.0], [1.5, 1.2], [1.2, 1.8], # Clase 0 (Cluster inferior izquierdo)
            [8.0, 8.0], [8.5, 8.2], [8.2, 8.8]  # Clase 1 (Cluster superior derecho)
        ])
        y_toy = np.array([0, 0, 0, 1, 1, 1])

        clf = KNNClassifierScratch(k=3, metric='euclidean', weights='uniform')
        clf.fit(X_toy, y_toy)

        pred_close_0 = clf.predict([[1.1, 1.3]])[0]
        pred_close_1 = clf.predict([[8.1, 8.3]])[0]

        assert pred_close_0 == 0, f"Punto cerca de 0 predijo {pred_close_0}"
        assert pred_close_1 == 1, f"Punto cerca de 1 predijo {pred_close_1}"
        print(f"  [{GREEN}✓{RESET}] Test 5: KNNClassifierScratch clasifica con exactitud 100% en clusters")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 5 Falló: {e}")

    # Test 6: KNN Scratch - Votación Ponderada (Distance Weighting)
    try:
        # Escenario donde el voto uniforme y el ponderado discrepan:
        # Punto consulta en x = [0.0]
        # Vecino muy cercano en 0.1 de clase 1
        # Dos vecinos un poco más lejanos en 2.0 y 2.1 de clase 0
        X_skew = np.array([[0.1], [2.0], [2.1]])
        y_skew = np.array([1, 0, 0])

        clf_unif = KNNClassifierScratch(k=3, weights='uniform')
        clf_unif.fit(X_skew, y_skew)
        pred_unif = clf_unif.predict([[0.0]])[0] # Voto simple: 2 ceros vs 1 uno -> predice 0

        clf_dist = KNNClassifierScratch(k=3, weights='distance')
        clf_dist.fit(X_skew, y_skew)
        pred_dist = clf_dist.predict([[0.0]])[0] # Ponderado: 1/0.1 = 10 para clase 1 >> 1/2 + 1/2.1 para clase 0 -> predice 1

        assert pred_unif == 0, "Voto uniforme debe priorizar mayoría de clase 0"
        assert pred_dist == 1, "Voto ponderado debe priorizar proximidad del vecino clase 1"
        print(f"  [{GREEN}✓{RESET}] Test 6: Inverso de distancia altera correctamente la votación de frontera")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 6 Falló: {e}")

    print(f"\n{BOLD}{CYAN}──────────────────────────────────────────────────────────────────────{RESET}")
    if tests_passed == total_tests:
        print(f"  {BOLD}{GREEN}🎉 ¡TODAS LAS PRUEBAS APROBADAS EXITOSAMENTE ({tests_passed}/{total_tests})!{RESET}")
        print(f"  {YELLOW}Las bases matemáticas y computacionales de la Clase 1 están consolidadas.{RESET}\n")
    else:
        print(f"  {BOLD}{RED}⚠️  Resultado: {tests_passed}/{total_tests} pruebas aprobadas.{RESET}\n")

if __name__ == "__main__":
    run_tests()
