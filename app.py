import os
import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pathlib import Path
from gemini_service import generate_hr_recommendation

# Hugging Face Spaces may run without a writable HOME directory; keep the app resilient.
os.environ.setdefault("STREAMLIT_SERVER_HEADLESS", "true")
os.environ.setdefault("STREAMLIT_SERVER_PORT", "8501")
os.environ.setdefault("STREAMLIT_BROWSER_GATHER_USAGE_STATS", "false")
os.environ.setdefault("STREAMLIT_SERVER_ENABLE_CORS", "false")
os.environ.setdefault("STREAMLIT_SERVER_ENABLE_STATIC_SERVING", "true")

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Workforce Intelligence Platform",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* GLOBAL */

.stApp {
    background: #081028;
    color: #f8fafc;
}

/* MAIN LAYOUT */

.block-container {
    max-width: 1150px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* TYPOGRAPHY */

h1, h2, h3, h4 {
    color: white !important;
    font-weight: 700 !important;
}

p, li {
    color: #cbd5e1;
    line-height: 1.8;
}

/* HEADER */

.main-title {
    font-size: 3.5rem;
    font-weight: 800;
    text-align: center;
    color: white;
    margin-bottom: 0.5rem;
}

.sub-title {
    text-align: center;
    font-size: 1.05rem;
    color: #94a3b8;
    margin-bottom: 1.8rem;
}

/* SECTION CARD */

.section-card {
    background: #111c44;
    border: 1px solid #1e2b5c;
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0px 6px 24px rgba(0,0,0,0.20);
}

/* SECTION TITLES */

.section-heading {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: white;
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stTextArea textarea {
    background-color: #0f172a !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #334155 !important;
}

/* SLIDER */

.stSlider {
    padding-top: 0.5rem;
    padding-bottom: 0.8rem;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 18px;
    border: none;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    font-size: 18px;
    font-weight: 700;
    transition: 0.3s ease;
    margin-top: 10px;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 8px 24px rgba(59,130,246,0.35);
}

/* PREDICTION CARD */

.prediction-box {
    padding: 36px;
    border-radius: 24px;
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}

.will-stay {
    background: linear-gradient(135deg, #065f46, #047857);
    border: 1px solid #10b981;
}

.will-leave {
    background: linear-gradient(135deg, #991b1b, #b91c1c);
    border: 1px solid #ef4444;
}

/* AI RESPONSE */

.ai-response {
    background: #111827;
    border-radius: 24px;
    padding: 28px;
    border: 1px solid #1e293b;
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.25);
}

/* AI TEXT */

.ai-response p,
.ai-response li {
    font-size: 16px;
    line-height: 1.9;
    color: #e2e8f0;
}

/* AI HEADINGS */

.ai-response h1,
.ai-response h2,
.ai-response h3 {
    margin-top: 1rem;
    margin-bottom: 0.8rem;
    color: white;
}

.ai-response strong {
    color: white !important;
}

/* METRICS */

[data-testid="metric-container"] {
    background: #111c44;
    border: 1px solid #1e2b5c;
    border-radius: 22px;
    padding: 24px;
    text-align: center;
}

[data-testid="metric-container"] label {
    color: #94a3b8 !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid #1e293b;
}

/* TABLE */

thead tr th {
    background-color: #111827 !important;
    color: white !important;
    font-size: 15px !important;
}

tbody tr {
    background-color: #0f172a !important;
    color: #f8fafc !important;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #0b122b;
}

[data-testid="stSidebar"] * {
    color: white;
}

/* HIDE FOOTER */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

@st.cache_resource
def load_model():

    model_path = Path(__file__).parent / 'hr_rf1.pickle'

    if model_path.exists():
        with open(model_path, 'rb') as f:
            return pickle.load(f)

    # Fallback for Hugging Face Spaces: if the model artifact is not present in the repo,
    # keep the UI available and explain the missing file instead of crashing.
    st.warning(
        "The trained model artifact was not found in the repository. "
        "Upload hr_rf1.pickle or train the model in the deployment environment to enable predictions."
    )
    st.stop()

# ---------------------------------------------------
# ENCODING
# ---------------------------------------------------

def encode_categorical_features(dept, salary_level):

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

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <div class="main-title">
        AI Workforce Intelligence Platform
    </div>

    <div class="sub-title">
        Predict employee attrition using machine learning and AI-powered workforce analytics
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = load_model()

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

st.markdown(
    """
    <div class="section-card" style="max-width:1100px; margin:auto;">
        <div class="section-heading" style="text-align:center;">
            Employee Information
        </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Work Performance")

    satisfaction = st.slider(
        "Job Satisfaction Level",
        0.0,
        1.0,
        0.5,
        0.1
    )

    evaluation = st.slider(
        "Last Evaluation Score",
        0.0,
        1.0,
        0.5,
        0.1
    )

    avg_hours = st.number_input(
        "Average Monthly Hours Worked",
        0,
        500,
        160
    )

with col2:

    st.markdown("### Employment Details")

    tenure = st.number_input(
        "Years at Company",
        0,
        50,
        3
    )

    num_projects = st.number_input(
        "Number of Projects",
        0,
        20,
        3
    )

    work_accident = st.radio(
        "Experienced Work Accident",
        ['No', 'Yes']
    )

col3, col4 = st.columns(2)

with col3:

    promotion = st.radio(
        "Promoted in Last 5 Years",
        ['No', 'Yes']
    )

with col4:

    department = st.selectbox(
        "Department",
        [
            'Sales',
            'Accounting',
            'HR',
            'IT',
            'Management',
            'Marketing',
            'Product management',
            'RandD',
            'Support',
            'Technical'
        ]
    )

    salary_level = st.selectbox(
        "Salary Level",
        ['Low', 'Medium', 'High']
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------

if st.button("Analyze Workforce Risk", use_container_width=True):

    try:

        dept_encoded, salary_encoded = encode_categorical_features(
            department,
            salary_level
        )

        work_accident_encoded = 1 if work_accident == 'Yes' else 0
        promotion_encoded = 1 if promotion == 'Yes' else 0

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

        if hasattr(model, 'best_estimator_'):

            prediction = model.best_estimator_.predict(features)[0]
            prediction_proba = model.best_estimator_.predict_proba(features)[0]

        else:

            prediction = model.predict(features)[0]
            prediction_proba = model.predict_proba(features)[0]

        # ---------------------------------------------------
        # RESULTS TITLE
        # ---------------------------------------------------

        st.markdown(
            '<div class="section-heading">Prediction Results</div>',
            unsafe_allow_html=True
        )

        employee_data = {
            "satisfaction": satisfaction,
            "evaluation": evaluation,
            "projects": num_projects,
            "hours": avg_hours,
            "tenure": tenure,
            "department": department,
            "salary": salary_level,
            "promotion": promotion,
            "work_accident": work_accident
        }

        # ---------------------------------------------------
        # PREDICTION BOX
        # ---------------------------------------------------

        if prediction == 0:

            risk = "Low Risk"

            st.markdown(
                f"""
                <div class="prediction-box will-stay">
                    <h1>Low Attrition Risk</h1>
                    <h2>{prediction_proba[1]*100:.1f}% Probability of Leaving</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            risk = "High Risk"

            st.markdown(
                f"""
                <div class="prediction-box will-leave">
                    <h1>High Attrition Risk</h1>
                    <h2>{prediction_proba[1]*100:.1f}% Probability of Leaving</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------------------------------------------------
        # AI RESPONSE
        # ---------------------------------------------------

        ai_response = generate_hr_recommendation(
            employee_data,
            risk,
            prediction_proba[1] * 100
        )

        st.markdown(
            f"""
            <div style="
                max-width:1000px;
                margin:25px auto 10px auto;
            ">

                <div class="section-heading"
                    style="
                        text-align:center;
                        margin-bottom:18px;
                    ">
                    AI HR Insights
                </div>

                <div class="ai-response">
                    {ai_response}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ---------------------------------------------------
        # METRICS
        # ---------------------------------------------------

        st.markdown(
            '<div class="section-heading">Workforce Metrics</div>',
            unsafe_allow_html=True
        )

        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:

            st.metric(
                "Retention Probability",
                f"{prediction_proba[0]*100:.1f}%"
            )

        with metric_col2:

            st.metric(
                "Attrition Probability",
                f"{prediction_proba[1]*100:.1f}%"
            )

        # ---------------------------------------------------
        # SUMMARY TABLE
        # ---------------------------------------------------

        st.markdown(
            '<div class="section-heading">Employee Summary</div>',
            unsafe_allow_html=True
        )

        summary_data = {
            'Metric': [
                'Satisfaction',
                'Evaluation',
                'Projects',
                'Monthly Hours',
                'Tenure',
                'Department',
                'Salary'
            ],
            'Value': [
                satisfaction,
                evaluation,
                num_projects,
                avg_hours,
                tenure,
                department,
                salary_level
            ]
        }

        summary_df = pd.DataFrame(summary_data)

        summary_df["Value"] = summary_df["Value"].astype(str)

        st.dataframe(
            summary_df,
            width='stretch',
            hide_index=True
        )

    except Exception as e:

        st.error(f"Prediction Error: {str(e)}")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.markdown("## Workforce Intelligence")

st.sidebar.markdown("""
### Model Overview

- Random Forest Classifier
- 15K+ Employee Records
- Accuracy: 97.6%
- AUC-ROC: 0.98

### AI Features

- Attrition Prediction
- AI HR Recommendations
- Workforce Risk Analysis
- Retention Strategy Generation

### Technology Stack

- Python
- Streamlit
- Scikit-learn
- Groq API
- Llama 3.1
- Pandas
- NumPy
""")

st.sidebar.markdown("""
**Satisfaction Level:** Job satisfaction (0-1 scale)
- **Evaluation:** Performance review score (0-1 scale)
- **Projects:** Number of projects assigned
- **Avg Hours:** Monthly working hours
- **Tenure:** Years employed
- **Accident:** Work accident history
- **Promotion:** Promotion in last 5 years
- **Department:** Work department
- **Salary:** Compensation level
""")
