"""
Fast Model Training Script (without GridSearch)
This trains a Random Forest model with good default parameters
Much faster than the GridSearch version
"""

import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

print("=" * 70)
print("Training Employee Attrition Prediction Model (Fast Version)")
print("=" * 70)

# Step 1: Load the data
print("\n1. Loading HR data...")
df = pd.read_csv('HR_comma_sep.csv')
print(f"   ✓ Loaded {len(df)} records with {len(df.columns)} features")

# Step 2: Encode categorical variables
print("\n2. Encoding categorical variables...")
df_enc = df.copy()

# Encode Department
le_dept = LabelEncoder()
df_enc['Department'] = le_dept.fit_transform(df_enc['Department'])

# Encode salary
le_salary = LabelEncoder()
df_enc['salary'] = le_salary.fit_transform(df_enc['salary'])

# Step 3: Prepare features and target
print("\n3. Preparing features and target...")
y = df_enc['left']
X = df_enc.drop('left', axis=1)
print(f"   ✓ Features shape: {X.shape}")
print(f"   ✓ Attrition rate: {y.mean()*100:.2f}%")

# Step 4: Train/test split
print("\n4. Splitting data (75% train, 25% test)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=0
)
print(f"   ✓ Train set: {len(X_train)} records")
print(f"   ✓ Test set: {len(X_test)} records")

# Step 5: Train Random Forest (without GridSearch - faster!)
print("\n5. Training Random Forest model with optimized parameters...")
print("   This takes about 30-60 seconds...")

# Use good default parameters (similar to what GridSearch would find)
rf_model = RandomForestClassifier(
    n_estimators=500,
    max_depth=5,
    min_samples_split=3,
    min_samples_leaf=2,
    max_features=1.0,
    random_state=0,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)
print(f"   ✓ Model training complete!")

# Step 6: Evaluate on test set
print("\n6. Evaluating model on test set...")
y_pred = rf_model.predict(X_test)
y_pred_proba = rf_model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)

print(f"   ✓ Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"   ✓ Precision: {precision:.4f} ({precision*100:.2f}%)")
print(f"   ✓ Recall:    {recall:.4f} ({recall*100:.2f}%)")
print(f"   ✓ F1-Score:  {f1:.4f}")
print(f"   ✓ AUC-ROC:   {auc:.4f}")

# Step 7: Save the model
print("\n7. Saving model as 'hr_rf1.pickle'...")
model_path = Path('hr_rf1.pickle')
with open(model_path, 'wb') as f:
    pickle.dump(rf_model, f)
print(f"   ✓ Model saved successfully!")
print(f"   ✓ File location: {model_path.absolute()}")
print(f"   ✓ File size: {model_path.stat().st_size / 1024 / 1024:.2f} MB")

# Step 8: Verify the model can be loaded
print("\n8. Verifying model can be loaded...")
with open(model_path, 'rb') as f:
    rf_loaded = pickle.load(f)
print(f"   ✓ Model verified successfully!")

# Step 9: Test prediction
print("\n9. Testing prediction with sample data...")
sample = X_test.iloc[0:1]
pred = rf_loaded.predict(sample)[0]
pred_proba = rf_loaded.predict_proba(sample)[0]
print(f"   ✓ Sample prediction: {'Will Leave' if pred == 1 else 'Will Stay'}")
print(f"   ✓ Probability: Stay={pred_proba[0]:.2%}, Leave={pred_proba[1]:.2%}")

print("\n" + "=" * 70)
print("✅ Model training and saving completed successfully!")
print("=" * 70)
print(f"\nModel is ready at: {model_path.absolute()}")
print("\nNext steps:")
print("1. Refresh your browser at http://localhost:8501")
print("2. The application will load the model automatically")
print("3. Start making predictions!")
print("\n" + "=" * 70)
