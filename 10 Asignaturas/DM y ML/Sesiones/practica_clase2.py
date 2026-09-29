#!/usr/bin/env python3
"""
🧪 Práctica & Autoevaluación — Lección 02: EDA, Preprocesamiento & KNN (Titanic)
Cátedra: Minería de Datos y Aprendizaje Automático — UNLP Informática (2026)

Este script contiene la batería de pruebas y ejercicios prácticos correspondientes
a la Clase 2 de la cátedra Ronchetti-Hasperué.
Ejecución directa: python3 practica_clase2.py
"""

import os
import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, ShuffleSplit, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Colores ANSI para terminal
GREEN = "\033[92m"
RED = "\033[91m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


# =====================================================================
# FUNCIONES DIDÁCTICAS A VALIDAR
# =====================================================================

def preprocesar_titanic_basico(df_raw):
    """
    Realiza la preparación de datos estándar enseñada por la cátedra:
    1. Elimina columnas irrelevantes/ruidosas: ['PassengerId', 'Name', 'Ticket', 'Cabin']
    2. Elimina filas con valores nulos residuales (dropna)
    3. Mapea 'Sex' de forma binaria: {'male': 0, 'female': 1}
    4. Aplica One-Hot Encoding sobre 'Embarked' con prefijo 'Embarked'
    Retorna el DataFrame limpio.
    """
    df = df_raw.copy()
    columns_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin']
    # Filtrar solo las columnas que existan
    cols_existentes = [c for c in columns_to_drop if c in df.columns]
    df = df.drop(columns=cols_existentes)
    df = df.dropna()

    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    if 'Embarked' in df.columns:
        df = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked', dtype=float)

    return df


def escalamiento_sin_leakage(X_train, X_test):
    """
    Aplica la Regla de Oro del escalamiento:
    Ajusta el StandardScaler EXCLUSIVAMENTE sobre X_train y transforma ambos conjuntos.
    Retorna (X_train_scaled, X_test_scaled, scaler_instancia)
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler


def ratio_clase_positiva(y):
    """Calcula la proporción de la clase 1 en un array o Serie."""
    arr = np.asarray(y)
    return float(np.sum(arr == 1) / len(arr))


# =====================================================================
# SUITE DE PRUEBAS AUTOMATIZADA
# =====================================================================

def run_tests():
    print(f"\n{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}  🔬 VALIDACIÓN AUTOMATIZADA · CLASE 2: PREPROCESAMIENTO & KNN (UNLP){RESET}")
    print(f"{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}\n")

    tests_passed = 0
    total_tests = 6

    # Cargar Dataset Titanic
    current_dir = os.path.dirname(os.path.abspath(__file__))
    titanic_path = os.path.join(current_dir, "titanic.csv")
    if not os.path.exists(titanic_path):
        # Fallback al directorio padre
        alt_path = os.path.join(os.path.dirname(current_dir), "Clase 2 - MD y AA", "titanic.csv")
        if os.path.exists(alt_path):
            titanic_path = alt_path

    # Test 1: Carga e integridad del dataset Titanic
    try:
        assert os.path.exists(titanic_path), f"No se encontró el dataset en {titanic_path}"
        df_raw = pd.read_csv(titanic_path)
        assert df_raw.shape[0] >= 800, f"Cantidad insuficiente de registros: {df_raw.shape[0]}"
        assert 'Survived' in df_raw.columns, "Falta la columna objetivo 'Survived'"
        print(f"  [{GREEN}✓{RESET}] Test 1: Dataset Titanic localizado y cargado con éxito ({df_raw.shape[0]} filas, {df_raw.shape[1]} columnas)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 1 Falló: {e}")
        return

    # Test 2: Preprocesamiento de columnas, nulos y One-Hot
    try:
        df_clean = preprocesar_titanic_basico(df_raw)
        assert 'PassengerId' not in df_clean.columns, "PassengerId no fue eliminada"
        assert 'Cabin' not in df_clean.columns, "Cabin no fue eliminada"
        assert df_clean.isnull().sum().sum() == 0, "Aún quedan valores nulos en el DataFrame"
        assert set(df_clean['Sex'].unique()).issubset({0, 1}), "La columna Sex no fue binarizada correctamente"
        assert any(c.startswith('Embarked_') for c in df_clean.columns), "No se generaron las columnas dummy de Embarked"
        print(f"  [{GREEN}✓{RESET}] Test 2: Limpieza y codificación categórica correctas (Vista minable: {df_clean.shape[0]} instancias, {df_clean.shape[1]} atributos)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 2 Falló: {e}")

    # Test 3: Prevención rigurosa de Data Leakage en Escalamiento
    try:
        # Generamos datos sintéticos donde Test tiene un outlier extremo
        X_tr = np.array([[10.0], [20.0], [30.0]])
        X_te = np.array([[1000.0]])

        X_tr_sc, X_te_sc, scaler = escalamiento_sin_leakage(X_tr, X_te)

        # La media debe ser exactamente 20.0 y desvío sqrt(200/3) ~ 8.16497
        expected_mean = 20.0
        expected_std = np.std(X_tr)

        assert np.isclose(scaler.mean_[0], expected_mean), f"La media calculada ({scaler.mean_[0]}) fue contaminada"
        assert np.isclose(scaler.scale_[0], expected_std), f"El desvío ({scaler.scale_[0]}) no coincide con train"
        # Comprobar que train escalado tiene media 0
        assert np.isclose(np.mean(X_tr_sc), 0.0), "La media de X_train_scaled debe ser 0.0"
        print(f"  [{GREEN}✓{RESET}] Test 3: Protocolo anti-leakage validado (Scaler fit ejecutado exclusivamente en Train)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 3 Falló: {e}")

    # Test 4: Preservación de proporciones con Partición Estratificada
    try:
        X = df_clean.drop('Survived', axis=1)
        y = df_clean['Survived']

        ratio_global = ratio_clase_positiva(y)

        # Split estratificado
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
        ratio_tr = ratio_clase_positiva(y_train)
        ratio_te = ratio_clase_positiva(y_test)

        diff_tr = abs(ratio_tr - ratio_global)
        diff_te = abs(ratio_te - ratio_global)

        assert diff_tr < 0.01 and diff_te < 0.01, f"Desbalanceo detectado en split: train={ratio_tr:.3f}, test={ratio_te:.3f}, global={ratio_global:.3f}"
        print(f"  [{GREEN}✓{RESET}] Test 4: Stratified Split preserva proporción de clases ({ratio_global*100:.1f}% ± 0.5%)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 4 Falló: {e}")

    # Test 5: Entrenamiento y convergencia de KNN con Scikit-Learn
    try:
        X_tr_sc, X_te_sc, _ = escalamiento_sin_leakage(X_train, X_test)
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_tr_sc, y_train)

        acc_train = accuracy_score(y_train, knn.predict(X_tr_sc))
        acc_test = accuracy_score(y_test, knn.predict(X_te_sc))

        assert acc_train >= 0.75, f"Accuracy en Train ({acc_train:.2f}) sospechosamente bajo"
        assert acc_test >= 0.70, f"Accuracy en Test ({acc_test:.2f}) sospechosamente bajo"
        print(f"  [{GREEN}✓{RESET}] Test 5: KNN (K=5) sobre Titanic alcanza Train Acc={acc_train*100:.1f}% y Test Acc={acc_test*100:.1f}%")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 5 Falló: {e}")

    # Test 6: Pipeline de Scikit-Learn con Cross-Validation ShuffleSplit
    try:
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('knn', KNeighborsClassifier(n_neighbors=5))
        ])

        ss = ShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
        cv_res = cross_validate(pipeline, X, y, cv=ss, scoring=['accuracy'], return_train_score=True)

        mean_tr = cv_res['train_accuracy'].mean()
        std_tr = cv_res['train_accuracy'].std()
        mean_te = cv_res['test_accuracy'].mean()
        std_te = cv_res['test_accuracy'].std()

        assert 0.75 <= mean_te <= 0.90, f"Media de Test CV fuera de rango razonable: {mean_te:.2f}"
        print(f"  [{GREEN}✓{RESET}] Test 6: Pipeline + ShuffleSplit (10 repeticiones) validado: Test Acc = {mean_te*100:.1f}% (±{std_te*100:.1f}%)")
        tests_passed += 1
    except Exception as e:
        print(f"  [{RED}✗{RESET}] Test 6 Falló: {e}")

    print(f"\n{BOLD}{CYAN}──────────────────────────────────────────────────────────────────────{RESET}")
    if tests_passed == total_tests:
        print(f"  {BOLD}{GREEN}🎉 ¡TODAS LAS PRUEBAS DE LA CLASE 2 APROBADAS EXITOSAMENTE ({tests_passed}/{total_tests})!{RESET}")
        print(f"  {YELLOW}Tu flujo de preprocesamiento, blindaje anti-leakage y validación cruzada está listo para producción.{RESET}\n")
    else:
        print(f"  {BOLD}{RED}⚠️  Resultado: {tests_passed}/{total_tests} pruebas aprobadas.{RESET}\n")


if __name__ == "__main__":
    run_tests()
