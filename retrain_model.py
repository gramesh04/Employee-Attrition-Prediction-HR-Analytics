#!/usr/bin/env python
"""
Retrain model with compatible numpy version for deployment
"""
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

print("🚀 Retraining Employee Attrition Model")
print("=" * 60)

try:
    # Load data
    print("📊 Loading HR data...")
    df = pd.read_csv('HR_comma_sep.csv')
    print(f"   ✓ Loaded {len(df)} records")
    
    # Encode
    print("🔄 Encoding variables...")
    df_enc = df.copy()
    df_enc['Department'] = LabelEncoder().fit_transform(df_enc['Department'])
    df_enc['salary'] = LabelEncoder().fit_transform(df_enc['salary'])
    
    # Prepare
    print("📈 Preparing features...")
    y = df_enc['left']
    X = df_enc.drop('left', axis=1)
    
    # Split
    print("✂️  Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=0
    )
    
    # Train
    print("🤖 Training Random Forest...")
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=5,
        min_samples_split=3,
        min_samples_leaf=2,
        random_state=0,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    from sklearn.metrics import accuracy_score
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Accuracy: {acc*100:.2f}%")
    
    # Save
    print("💾 Saving model...")
    with open('hr_rf1.pickle', 'wb') as f:
        pickle.dump(model, f)
    
    print("\n✅ SUCCESS! Model retrained and saved.")
    print("   File: hr_rf1.pickle")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
