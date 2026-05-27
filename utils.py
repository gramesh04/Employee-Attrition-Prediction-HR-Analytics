"""
Utility functions for the Employee Attrition Prediction application.
This module provides functions for data preprocessing and model training.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
from pathlib import Path


def load_and_prepare_data(csv_path):
    """
    Load the HR dataset and perform initial preprocessing.
    
    Parameters:
    -----------
    csv_path : str or Path
        Path to the HR_comma_sep.csv file
        
    Returns:
    --------
    df : pd.DataFrame
        Preprocessed dataframe
    """
    # Load data
    df = pd.read_csv(csv_path)
    
    print(f"Data shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    
    return df


def encode_categorical_variables(df):
    """
    Encode categorical variables in the dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with categorical variables
        
    Returns:
    --------
    df_encoded : pd.DataFrame
        Dataframe with encoded categorical variables
    encoders : dict
        Dictionary containing the encoders used for each column
    """
    df_encoded = df.copy()
    encoders = {}
    
    # Encode Department
    if 'Department' in df_encoded.columns:
        le_dept = LabelEncoder()
        df_encoded['Department'] = le_dept.fit_transform(df_encoded['Department'])
        encoders['Department'] = le_dept
        print(f"Department encoding: {dict(zip(le_dept.classes_, le_dept.transform(le_dept.classes_)))}")
    
    # Encode salary
    if 'salary' in df_encoded.columns:
        le_salary = LabelEncoder()
        df_encoded['salary'] = le_salary.fit_transform(df_encoded['salary'])
        encoders['salary'] = le_salary
        print(f"Salary encoding: {dict(zip(le_salary.classes_, le_salary.transform(le_salary.classes_)))}")
    
    return df_encoded, encoders


def prepare_features_and_target(df_encoded):
    """
    Separate features and target variable.
    
    Parameters:
    -----------
    df_encoded : pd.DataFrame
        Encoded dataframe
        
    Returns:
    --------
    X : pd.DataFrame
        Features
    y : pd.Series
        Target variable (left)
    """
    if 'left' not in df_encoded.columns:
        raise ValueError("Target variable 'left' not found in dataframe")
    
    y = df_encoded['left']
    X = df_encoded.drop('left', axis=1)
    
    return X, y


def save_model(model, save_path):
    """
    Save a trained model to a pickle file.
    
    Parameters:
    -----------
    model : object
        Trained model object
    save_path : str or Path
        Path where to save the model
    """
    with open(save_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {save_path}")


def load_model(model_path):
    """
    Load a trained model from a pickle file.
    
    Parameters:
    -----------
    model_path : str or Path
        Path to the model pickle file
        
    Returns:
    --------
    model : object
        Loaded model
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print(f"Model loaded from {model_path}")
    return model


def get_feature_importance(model, feature_names):
    """
    Extract and display feature importance from a trained model.
    
    Parameters:
    -----------
    model : object
        Trained model with feature_importances_ attribute
    feature_names : list
        Names of features
        
    Returns:
    --------
    importances : pd.DataFrame
        Feature importances sorted by importance
    """
    if hasattr(model, 'best_estimator_'):
        estimator = model.best_estimator_
    else:
        estimator = model
    
    if not hasattr(estimator, 'feature_importances_'):
        raise ValueError("Model does not have feature_importances_ attribute")
    
    importances = pd.DataFrame({
        'feature': feature_names,
        'importance': estimator.feature_importances_
    }).sort_values('importance', ascending=False)
    
    return importances


def print_model_summary(model, X_test, y_test, feature_names):
    """
    Print a summary of model performance and feature importance.
    
    Parameters:
    -----------
    model : object
        Trained model object
    X_test : pd.DataFrame
        Test features
    y_test : pd.Series
        Test target
    feature_names : list
        Names of features
    """
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
    
    # Get predictions
    if hasattr(model, 'best_estimator_'):
        y_pred = model.best_estimator_.predict(X_test)
        y_pred_proba = model.best_estimator_.predict_proba(X_test)[:, 1]
    else:
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)
    
    print("\n" + "="*50)
    print("MODEL PERFORMANCE SUMMARY")
    print("="*50)
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print(f"AUC-ROC:   {auc:.4f}")
    print("="*50 + "\n")
    
    # Feature importance
    try:
        importances = get_feature_importance(model, feature_names)
        print("\nTOP 10 IMPORTANT FEATURES:")
        print("-"*50)
        print(importances.head(10).to_string(index=False))
        print("-"*50 + "\n")
    except Exception as e:
        print(f"Could not extract feature importance: {e}\n")


if __name__ == "__main__":
    print("Utility functions for Employee Attrition Prediction")
    print("Import this module to use the provided functions")
