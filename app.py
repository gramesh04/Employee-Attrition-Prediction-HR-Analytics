import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .will-leave {
        background-color: #ffcccc;
        border-left: 5px solid #cc0000;
    }
    .will-stay {
        background-color: #ccffcc;
        border-left: 5px solid #00cc00;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    """Load the trained Random Forest model from pickle file."""
    model_path = Path(__file__).parent / 'hr_rf1.pickle'
    if not model_path.exists():
        st.error(f"Model file not found at {model_path}")
        st.stop()
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

# Load the data to get encoding information
@st.cache_data
def load_sample_data():
    """Load sample data to understand encodings."""
    data_path = Path(__file__).parent / 'HR_comma_sep.csv'
    if data_path.exists():
        return pd.read_csv(data_path)
    return None

def encode_categorical_features(dept, salary_level):
    """
    Encode categorical features to match the training data encoding.
    This replicates the encoding used in the notebook.
    """
    # Department encoding
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
    
    # Salary encoding
    salary_map = {
        'Low': 0,
        'Medium': 1,
        'High': 2
    }
    
    dept_encoded = departments.get(dept, 1)
    salary_encoded = salary_map.get(salary_level, 0)
    
    return dept_encoded, salary_encoded

st.markdown("<h1 class='main-header'>👥 Employee Attrition Prediction System</h1>", unsafe_allow_html=True)

st.markdown("""
This application uses a trained Machine Learning model to predict whether an employee 
is likely to leave the company based on their profile and work metrics.
""")

# Load the model
model = load_model()
sample_data = load_sample_data()

# Create the input form
st.markdown("---")
st.markdown("### 📋 Enter Employee Information")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Work Performance & Evaluation**")
    satisfaction = st.slider(
        "Job Satisfaction Level (0 to 1)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1,
        help="Employee-reported job satisfaction level"
    )
    
    evaluation = st.slider(
        "Last Evaluation Score (0 to 1)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1,
        help="Score from the employee's last performance review"
    )
    
    avg_hours = st.number_input(
        "Average Monthly Hours Worked",
        min_value=0,
        max_value=500,
        value=160,
        step=1,
        help="Average number of hours worked per month"
    )

with col2:
    st.markdown("**Employment Details**")
    tenure = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=50,
        value=3,
        step=1,
        help="Employee tenure in years"
    )
    
    num_projects = st.number_input(
        "Number of Projects",
        min_value=0,
        max_value=20,
        value=3,
        step=1,
        help="Number of projects the employee contributes to"
    )
    
    work_accident = st.radio(
        "Experienced Work Accident",
        options=['No', 'Yes'],
        help="Whether the employee experienced an accident at work"
    )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.markdown("**Company Benefits & Position**")
    promotion = st.radio(
        "Promoted in Last 5 Years",
        options=['No', 'Yes'],
        help="Whether the employee was promoted in the last 5 years"
    )

with col4:
    st.markdown("**Department & Salary**")
    department = st.selectbox(
        "Department",
        options=['Sales', 'Accounting', 'HR', 'IT', 'Management', 
                'Marketing', 'Product management', 'RandD', 'Support', 'Technical']
    )
    
    salary_level = st.selectbox(
        "Salary Level",
        options=['Low', 'Medium', 'High']
    )

st.markdown("---")

# Make prediction
if st.button("🔮 Predict Employee Attrition", use_container_width=True, key="predict_btn"):
    try:
        # Encode categorical features
        dept_encoded, salary_encoded = encode_categorical_features(department, salary_level)
        
        # Convert binary inputs
        work_accident_encoded = 1 if work_accident == 'Yes' else 0
        promotion_encoded = 1 if promotion == 'Yes' else 0
        
        # Create feature array matching the order used in the model
        # Based on the notebook: satisfaction_level, last_evaluation, number_project, 
        # average_monthly_hours, time_spend_company, Work_accident, promotion_last_5years, 
        # Department, salary
        features = np.array([[
            satisfaction,
            evaluation,
            num_projects,
            avg_hours,
            tenure,
            work_accident_encoded,
            promotion_encoded,
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
        
        st.markdown("---")
        st.markdown("### 📊 Prediction Results")
        
        if prediction == 1:
            st.markdown(
                f"""
                <div class="prediction-box will-leave">
                    <h3>⚠️ High Risk - Employee May Leave</h3>
                    <p>Based on the provided information, this employee has a <strong>{prediction_proba[1]*100:.1f}%</strong> 
                    probability of leaving the company.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            st.info("""
            **Recommendations for HR:**
            - Schedule a meeting with the employee to discuss satisfaction and concerns
            - Review compensation and benefits
            - Discuss career development opportunities and growth paths
            - Consider workload and hours being worked
            - Identify what motivates this employee and align with company goals
            """)
        else:
            st.markdown(
                f"""
                <div class="prediction-box will-stay">
                    <h3>✅ Low Risk - Employee Likely to Stay</h3>
                    <p>Based on the provided information, this employee has only a <strong>{prediction_proba[1]*100:.1f}%</strong> 
                    probability of leaving the company.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            st.success("""
            **Recommendations for HR:**
            - Continue supporting this employee's growth and development
            - Maintain regular check-ins to ensure continued satisfaction
            - Consider leveraging this employee's stability for mentoring roles
            - Ensure competitive compensation remains in place
            """)
        
        # Display confidence metrics
        st.markdown("---")
        col_metrics1, col_metrics2 = st.columns(2)
        
        with col_metrics1:
            st.metric(
                "Probability of Staying",
                f"{prediction_proba[0]*100:.1f}%"
            )
        
        with col_metrics2:
            st.metric(
                "Probability of Leaving",
                f"{prediction_proba[1]*100:.1f}%"
            )
        
        # Display input summary
        st.markdown("---")
        st.markdown("### 📝 Input Summary")
        
        summary_data = {
            'Metric': [
                'Satisfaction Level',
                'Last Evaluation',
                'Number of Projects',
                'Avg Monthly Hours',
                'Years at Company',
                'Work Accident',
                'Promoted (5 yrs)',
                'Department',
                'Salary Level'
            ],
            'Value': [
                f"{satisfaction:.2f}",
                f"{evaluation:.2f}",
                num_projects,
                avg_hours,
                tenure,
                work_accident,
                promotion,
                department,
                salary_level
            ]
        }
        
        st.dataframe(pd.DataFrame(summary_data), use_container_width=True, hide_index=True)
        
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        st.info("Please ensure all inputs are valid and try again.")

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("### ℹ️ About This Model")
st.sidebar.markdown("""
**Model Type:** Random Forest Classifier

**Features:** 9 employee metrics

**Training Data:** 14,999 employee records

**Model Performance:**
- Accuracy: ~98%
- AUC Score: ~0.97

**Purpose:** Predict employee attrition risk to help HR improve retention strategies.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Feature Descriptions")
st.sidebar.markdown("""
- **Satisfaction Level:** Job satisfaction (0-1 scale)
- **Evaluation:** Performance review score (0-1 scale)
- **Projects:** Number of projects assigned
- **Avg Hours:** Monthly working hours
- **Tenure:** Years employed
- **Accident:** Work accident history
- **Promotion:** Promotion in last 5 years
- **Department:** Work department
- **Salary:** Compensation level
""")
