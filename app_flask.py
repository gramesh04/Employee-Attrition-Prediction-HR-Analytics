"""
Flask-based Employee Attrition Prediction Web Application
Alternative to the Streamlit version
"""

from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
from pathlib import Path
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Load the model
model = None
model_loaded = False

def load_model_flask():
    """Load the trained Random Forest model."""
    global model, model_loaded
    try:
        model_path = Path(__file__).parent / 'hr_rf1.pickle'
        if model_path.exists():
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            model_loaded = True
            print("Model loaded successfully")
            return True
        else:
            print(f"Model file not found at {model_path}")
            return False
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

def encode_categorical_features(dept, salary_level):
    """Encode categorical features."""
    departments = {
        'Sales': 1,
        'Accounting': 2,
        'HR': 3,
        'IT': 4,
        'Management': 5,
        'Marketing': 6,
        'Product management': 7,
        'RandD': 8,
        'Support': 9,
        'Technical': 10
    }
    
    salary_map = {
        'Low': 0,
        'Medium': 1,
        'High': 2
    }
    
    dept_encoded = departments.get(dept, 1)
    salary_encoded = salary_map.get(salary_level, 0)
    
    return dept_encoded, salary_encoded

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    if not model_loaded:
        return jsonify({'error': 'Model not loaded'}), 500
    
    try:
        data = request.get_json()
        
        # Extract and validate inputs
        satisfaction = float(data.get('satisfaction', 0.5))
        evaluation = float(data.get('evaluation', 0.5))
        num_projects = int(data.get('num_projects', 3))
        avg_hours = int(data.get('avg_hours', 160))
        tenure = int(data.get('tenure', 3))
        work_accident = int(data.get('work_accident', 0))
        promotion = int(data.get('promotion', 0))
        department = data.get('department', 'Sales')
        salary_level = data.get('salary_level', 'Low')
        
        # Encode categorical features
        dept_encoded, salary_encoded = encode_categorical_features(department, salary_level)
        
        # Create feature array
        features = np.array([[
            satisfaction,
            evaluation,
            num_projects,
            avg_hours,
            tenure,
            work_accident,
            promotion,
            dept_encoded,
            salary_encoded
        ]])
        
        # Make prediction
        # Handle both GridSearchCV and plain model objects
        if hasattr(model, 'best_estimator_'):
            # GridSearchCV object
            prediction = model.best_estimator_.predict(features)[0]
            prediction_proba = model.best_estimator_.predict_proba(features)[0]
        else:
            # Plain trained model
            prediction = model.predict(features)[0]
            prediction_proba = model.predict_proba(features)[0]
        
        # Prepare response
        result = {
            'prediction': int(prediction),
            'probability_stay': float(prediction_proba[0]),
            'probability_leave': float(prediction_proba[1]),
            'risk_level': 'High' if prediction == 1 else 'Low',
            'input_summary': {
                'satisfaction': satisfaction,
                'evaluation': evaluation,
                'num_projects': num_projects,
                'avg_hours': avg_hours,
                'tenure': tenure,
                'work_accident': 'Yes' if work_accident else 'No',
                'promotion': 'Yes' if promotion else 'No',
                'department': department,
                'salary_level': salary_level
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/model-info')
def model_info():
    """Return model information."""
    return jsonify({
        'model_type': 'Random Forest Classifier',
        'features': 9,
        'training_samples': 14999,
        'accuracy': 0.98,
        'auc_score': 0.97,
        'departments': ['Sales', 'Accounting', 'HR', 'IT', 'Management', 
                       'Marketing', 'Product management', 'RandD', 'Support', 'Technical'],
        'salary_levels': ['Low', 'Medium', 'High']
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Load model before starting the app
    if load_model_flask():
        # Run the app
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True
        )
    else:
        print("Failed to load model. Application cannot start.")
