"""
Resolución y Análisis Práctico de Actividades 1 a 8 - Árboles de Decisión
Cátedra: Minería de Datos y Aprendizaje Automático (UNLP)
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("🚀 EJECUTANDO ACTIVIDADES 1 A 8 - ÁRBOLES DE DECISIÓN")
print("="*70)

# -------------------------------------------------------------------------
# ACTIVIDAD 1 & 2: Dataset Diabetes (Entropy vs Gini, max_depth=4, Data Leakage)
# -------------------------------------------------------------------------
print("\n📌 [ACTIVIDAD 1 & 2] Dataset: diabetes.csv")
df_diabetes = pd.read_csv("diabetes.csv")
print(f"Shape: {df_diabetes.shape}")

X_diab = df_diabetes.drop(columns=['Outcome'])
y_diab = df_diabetes['Outcome']

# 1. Comparación Entropy vs Gini (max_depth=4)
clf_entropy = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=42)
clf_entropy.fit(X_diab, y_diab)
acc_entropy = accuracy_score(y_diab, clf_entropy.predict(X_diab))

clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)
clf_gini.fit(X_diab, y_diab)
acc_gini = accuracy_score(y_diab, clf_gini.predict(X_diab))

print(f"1. Accuracy en todo el dataset (max_depth=4):")
print(f"   - Criterio Entropy: {acc_entropy:.4f}")
print(f"   - Criterio Gini   : {acc_gini:.4f}")

# Atributo raíz elegido por cada criterio
feature_names_diab = list(X_diab.columns)
root_entropy = feature_names_diab[clf_entropy.tree_.feature[0]]
root_gini = feature_names_diab[clf_gini.tree_.feature[0]]
print(f"   - Nodo Raíz (Entropy): {root_entropy} (umbral <= {clf_entropy.tree_.threshold[0]:.2f})")
print(f"   - Nodo Raíz (Gini)   : {root_gini} (umbral <= {clf_gini.tree_.threshold[0]:.2f})")

# 2. Trampa de Data Leakage (incluyendo 'Outcome' en X)
X_leak = df_diabetes.copy()
clf_leak = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=42)
clf_leak.fit(X_leak, y_diab)
root_leak = list(X_leak.columns)[clf_leak.tree_.feature[0]]
acc_leak = accuracy_score(y_diab, clf_leak.predict(X_leak))
print(f"\n2. Impacto de Data Leakage (incluyendo Outcome como predictor):")
print(f"   - Atributo seleccionado en la Raíz: {root_leak}")
print(f"   - Accuracy resultante: {acc_leak:.4f} (100% trivial)")
print(f"   - Conclusión: El árbol divide directamente por el target, volviéndose inútil para datos no etiquetados.")

# -------------------------------------------------------------------------
# ACTIVIDADES 3 A 6: Predicción de nuevo paciente y variaciones Train/Test
# -------------------------------------------------------------------------
print("\n" + "-"*70)
print("📌 [ACTIVIDADES 3 A 6] Diabetes: Train/Test Splits y Predicción")

# Predicción para nuevo paciente
new_patient = [[0, 150, 210, 30, 115, 30, 0.2, 25]]
pred_patient = clf_entropy.predict(new_patient)[0]
prob_patient = clf_entropy.predict_proba(new_patient)[0]
print(f"\nPredicción nuevo paciente {new_patient[0]}:")
print(f"   - Clase predicha: {'Diabético (1)' if pred_patient == 1 else 'No diabético (0)'}")
print(f"   - Probabilidades: [Clase 0: {prob_patient[0]:.2f}, Clase 1: {prob_patient[1]:.2f}]")

# Actividades 3 y 4: Split 90-10, default vs max_depth=4
X_tr90, X_te90, y_tr90, y_te90 = train_test_split(X_diab, y_diab, test_size=0.10, random_state=13)

clf_ent_def = DecisionTreeClassifier(criterion='entropy', random_state=13).fit(X_tr90, y_tr90)
clf_gin_def = DecisionTreeClassifier(criterion='gini', random_state=13).fit(X_tr90, y_tr90)
print(f"\n3 y 4. Split 90/10 (Valores por defecto, sin límite de profundidad - Overfitting):")
print(f"   - Entropy Test Acc: {accuracy_score(y_te90, clf_ent_def.predict(X_te90)):.4f} (Train Acc: {accuracy_score(y_tr90, clf_ent_def.predict(X_tr90)):.4f})")
print(f"   - Gini Test Acc   : {accuracy_score(y_te90, clf_gin_def.predict(X_te90)):.4f} (Train Acc: {accuracy_score(y_tr90, clf_gin_def.predict(X_tr90)):.4f})")

clf_ent_d4 = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=13).fit(X_tr90, y_tr90)
clf_gin_d4 = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=13).fit(X_tr90, y_tr90)
print(f"\n5. Split 90/10 con Poda preventiva (max_depth=4):")
print(f"   - Entropy Test Acc: {accuracy_score(y_te90, clf_ent_d4.predict(X_te90)):.4f} (Train Acc: {accuracy_score(y_tr90, clf_ent_d4.predict(X_tr90)):.4f})")
print(f"   - Gini Test Acc   : {accuracy_score(y_te90, clf_gin_d4.predict(X_te90)):.4f} (Train Acc: {accuracy_score(y_tr90, clf_gin_d4.predict(X_tr90)):.4f})")
print("   -> Explicación: Al limitar la profundidad evitamos que memorice outliers, reduciendo la varianza del modelo.")

# 6. Variación de Train-Test Splits
print(f"\n6. Comparación de proporciones Train/Test (max_depth=4):")
splits = [(0.20, "80/20"), (0.30, "70/30"), (0.40, "60/40")]
for test_ratio, label in splits:
    X_tr, X_te, y_tr, y_te = train_test_split(X_diab, y_diab, test_size=test_ratio, random_state=13)
    c_ent = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=13).fit(X_tr, y_tr)
    c_gin = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=13).fit(X_tr, y_tr)
    acc_e = accuracy_score(y_te, c_ent.predict(X_te))
    acc_g = accuracy_score(y_te, c_gin.predict(X_te))
    print(f"   - Split {label}: Entropy Test Acc = {acc_e:.4f} | Gini Test Acc = {acc_g:.4f}")

# -------------------------------------------------------------------------
# ACTIVIDAD 7: Dataset Glass (Clasificación Multiclase)
# -------------------------------------------------------------------------
print("\n" + "-"*70)
print("📌 [ACTIVIDAD 7] Dataset: glass.csv (Multiclase)")
glass_cols = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
df_glass = pd.read_csv("glass.csv", names=glass_cols)
X_glass = df_glass.drop(columns=['Id', 'Type'])
y_glass = df_glass['Type']
print(f"Shape: {df_glass.shape} | Clases únicas en target: {sorted(y_glass.unique())}")

for test_ratio, label in splits:
    X_tr, X_te, y_tr, y_te = train_test_split(X_glass, y_glass, test_size=test_ratio, random_state=13)
    c_ent = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=13).fit(X_tr, y_tr)
    c_gin = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=13).fit(X_tr, y_tr)
    acc_e = accuracy_score(y_te, c_ent.predict(X_te))
    acc_g = accuracy_score(y_te, c_gin.predict(X_te))
    print(f"   - Glass Split {label}: Entropy Acc = {acc_e:.4f} | Gini Acc = {acc_g:.4f}")

# -------------------------------------------------------------------------
# ACTIVIDAD 8: Dataset Campus (Codificación Categórica y Clasificación)
# -------------------------------------------------------------------------
print("\n" + "-"*70)
print("📌 [ACTIVIDAD 8] Dataset: Campus.csv (Preprocesamiento y Clasificación)")
df_campus = pd.read_csv("Campus.csv")
print(f"Shape inicial: {df_campus.shape}")

# Preprocesamiento:
# 1. Descartar 'sl_no' (identificador irrelevante) y 'salary' (target secundario que genera data leakage para status)
df_camp_clean = df_campus.drop(columns=['sl_no', 'salary'], errors='ignore')

# 2. Variable objetivo: status ('Placed' -> 1, 'Not Placed' -> 0)
y_campus = df_camp_clean['status'].map({'Placed': 1, 'Not Placed': 0})
X_campus = df_camp_clean.drop(columns=['status'])

# 3. Tratamiento de variables categóricas:
# Binarias ordinales/nominales: gender, workex
X_campus['gender'] = X_campus['gender'].map({'M': 1, 'F': 0})
X_campus['workex'] = X_campus['workex'].map({'Yes': 1, 'No': 0})
# Nominales con One-Hot Encoding: ssc_b, hsc_b, hsc_s, degree_t, specialisation
categorical_cols = ['ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'specialisation']
X_campus_encoded = pd.get_dummies(X_campus, columns=categorical_cols, drop_first=True)

print(f"Variables tras One-Hot Encoding: {X_campus_encoded.shape[1]} columnas")

for test_ratio, label in splits:
    X_tr, X_te, y_tr, y_te = train_test_split(X_campus_encoded, y_campus, test_size=test_ratio, random_state=13)
    c_ent = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=13).fit(X_tr, y_tr)
    c_gin = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=13).fit(X_tr, y_tr)
    acc_e = accuracy_score(y_te, c_ent.predict(X_te))
    acc_g = accuracy_score(y_te, c_gin.predict(X_te))
    print(f"   - Campus Split {label}: Entropy Acc = {acc_e:.4f} | Gini Acc = {acc_g:.4f}")

# Features más importantes para conseguir empleo
best_tree = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=13).fit(X_campus_encoded, y_campus)
importances = pd.Series(best_tree.feature_importances_, index=X_campus_encoded.columns).sort_values(ascending=False)
print("\nTop 3 atributos más determinantes para conseguir empleo (Feature Importance):")
for feat, imp in importances.head(3).items():
    print(f"   - {feat}: {imp*100:.1f}%")

print("\n" + "="*70)
print("✅ TODAS LAS ACTIVIDADES COMPLETADAS EXITOSAMENTE")
print("="*70)
