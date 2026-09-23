"""
Plantilla de Práctica Guiada: Actividades 1 a 8 - Árboles de Decisión
Cátedra: Minería de Datos y Aprendizaje Automático (UNLP)

Completa las secciones marcadas con TODO para resolver los ejercicios.
Para ejecutar: uv run --with scikit-learn,pandas,numpy python3 actividades_practica_alumno.py
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("="*70)
print("📘 PRÁCTICA DE ÁRBOLES DE DECISIÓN (ACTIVIDADES 1 A 8)")
print("="*70)

# =========================================================================
# ACTIVIDAD 1 & 2: Dataset Diabetes (Entropy vs Gini y Fuga de Datos)
# =========================================================================
print("\n--- ACTIVIDAD 1 & 2: diabetes.csv ---")
# 1. Cargar el dataset 'diabetes.csv'
df_diabetes = pd.read_csv("diabetes.csv")
X_diab = df_diabetes.drop(columns=['Outcome'])
y_diab = df_diabetes['Outcome']

# TODO 1: Entrenar dos árboles con max_depth=4, uno con criterion='entropy' y otro con criterion='gini'
# clf_entropy = ...
# clf_gini = ...

# TODO 2: Entrenar un árbol incluyendo 'Outcome' dentro de las variables de entrada X (Fuga de Datos).
# Observar la raíz y el accuracy obtenido.


# =========================================================================
# ACTIVIDADES 3 A 6: Predicciones y Variación de Splits Train/Test
# =========================================================================
print("\n--- ACTIVIDADES 3 A 6: Predicción y Splits Train/Test ---")
# TODO 3: Con el árbol entrenado con entropy, predecir la clase de un nuevo paciente:
# new_patient = [[0, 150, 210, 30, 115, 30, 0.2, 25]]

# TODO 4: Separar diabetes en 90-10 (train_test_split con test_size=0.10, random_state=13).
# Entrenar dos árboles con entropy y gini con parámetros por defecto. Comparar Accuracy Train vs Test.

# TODO 5: Repetir con max_depth=4. ¿Mejora la generalización en Test?

# TODO 6: Comparar accuracy en Test variando las particiones a (80-20), (70-30), (60-40).


# =========================================================================
# ACTIVIDAD 7: Dataset Glass (Clasificación Multiclase)
# =========================================================================
print("\n--- ACTIVIDAD 7: glass.csv (Multiclase) ---")
# El dataset no tiene encabezados en la primera fila. Usar estos nombres de columna:
glass_cols = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
df_glass = pd.read_csv("glass.csv", names=glass_cols)

# TODO 7: Eliminar la columna 'Id' y separar 'Type' como target (y).
# Entrenar árboles variando splits (80-20, 70-30, 60-40) con max_depth=4. Evaluar accuracy.


# =========================================================================
# ACTIVIDAD 8: Dataset Campus (Preprocesamiento Categórico)
# =========================================================================
print("\n--- ACTIVIDAD 8: Campus.csv (Preprocesamiento y Clasificación) ---")
df_campus = pd.read_csv("Campus.csv")

# TODO 8:
# a) Descartar 'sl_no' y 'salary' (evitar data leakage: salary solo existe si fue contratado).
# b) Convertir 'status' ('Placed'/'Not Placed') a 1 y 0.
# c) Codificar variables binarias ('gender', 'workex') y aplicar pd.get_dummies() a las nominales:
#    ['ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'specialisation']
# d) Entrenar árboles con splits (80-20, 70-30, 60-40) y analizar feature_importances_.
