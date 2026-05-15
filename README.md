# 👥 Employee Attrition Prediction & HR Analytics

A comprehensive Machine Learning project with an interactive web application for predicting employee attrition risk and providing HR insights.

## 🎯 Project Overview

This project analyzes an HR dataset to build predictive models that help organizations understand and predict employee attrition. The analysis provides data-driven insights for the Human Resources department to improve employee retention strategies.

**Now featuring:** Interactive web applications built with **Streamlit** and **Flask** for real-time employee attrition predictions! 🚀

## Business Problem

**Research Question:** What factors are most likely to lead an employee to leave the company?

Salifort Motors sought to understand employee satisfaction and retention patterns in their organization. The ability to predict and address potential attrition provides significant value, as recruiting, interviewing, and training new employees is both time-consuming and costly.

## Dataset

- **Source:** [Kaggle HR Analytics Dataset](https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction)
- **Rows:** 14,999 employees (after removing duplicates: 11,991)
- **Features:** 10 variables

### Features Description

| Variable | Description |
|----------|-------------|
| `satisfaction_level` | Employee-reported job satisfaction level (0–1) |
| `last_evaluation` | Score of employee's last performance review (0–1) |
| `number_project` | Number of projects the employee contributes to |
| `average_monthly_hours` | Average number of hours worked per month |
| `tenure` | Employee tenure in years |
| `work_accident` | Whether employee experienced an accident at work (0/1) |
| `left` | **Target Variable** - Whether employee left company (0/1) |
| `promotion_last_5years` | Whether employee was promoted in last 5 years (0/1) |
| `department` | Employee's department |
| `salary` | Employee's salary tier (low, medium, high) |

## Key Findings

### Data Insights

1. **Workload & Attrition Correlation**
   - Employees working 240+ hours/month showed significantly higher attrition
   - All employees assigned to 7 projects left the company
   - Optimal project load: 3-4 projects (low attrition rate)

2. **Satisfaction & Retention**
   - Mean satisfaction for employees who left: 0.44
   - Mean satisfaction for employees who stayed: 0.67
   - Strong negative correlation between satisfaction and attrition

3. **Tenure Patterns**
   - Employees with 4+ years tenure who left showed unusually low satisfaction
   - Long-tenured employees (6+ years) rarely left
   - Relatively few long-tenure employees suggest higher-paying positions

4. **Evaluation & Promotion**
   - Overworked employees with high evaluations were more likely to leave (burnout)
   - Very few employees working extreme hours were promoted
   - Disconnect between hard work and career advancement

5. **Workload Reality**
   - Benchmark: ~167 hours/month (40-hour weeks, 2-week vacation)
   - Most employees work 200+ hours/month (well above benchmark)
   - Indicates systemic overwork across the organization

## Methodology

### Data Processing
- **Data Cleaning:** Removed 3,008 duplicate rows (20% of data)
- **Outlier Detection:** Identified tenure outliers using IQR method
- **Feature Encoding:**
  - Ordinal encoding for `salary` (preserves hierarchy)
  - One-hot encoding for `department`

### Exploratory Data Analysis (EDA)
- Univariate analysis: distributions of key variables
- Bivariate analysis: relationships with attrition
- Correlation analysis: feature relationships
- Visualizations: boxplots, histograms, scatterplots, heatmaps

### Modeling Approaches

#### 1. **Logistic Regression Model**
- **Assumptions Checked:**
  - Binary outcome variable ✓
  - Independent observations ✓
  - No severe multicollinearity ✓
  - Sufficiently large sample size ✓
  
- **Performance:**
  - Accuracy: 82%
  - Precision: 79%
  - Recall: 82%
  - F1-Score: 80%

#### 2. **Decision Tree Model**
- **Grid Search Parameters:**
  - `max_depth`: [4, 6, 8, None]
  - `min_samples_leaf`: [1, 2, 5]
  - `min_samples_split`: [2, 4, 6]
  
- **Best Parameters:** (Determined via cross-validation)
  - Strong cross-validation scores across all metrics

## 🤖 Machine Learning Models

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| **Random Forest** | **97.60%** | **97.40%** | **92.39%** | **0.9483** | **0.9846** |
| Decision Tree | ~95% | ~95% | ~90% | ~0.92 | ~0.96 |
| Logistic Regression | 82% | 79% | 82% | 0.80 | ~0.85 |

### ✅ Selected Model: Random Forest Classifier

**Why Random Forest?**
- Highest accuracy (97.6%)
- Excellent recall (92.39%) - catches most at-risk employees
- Better generalization (ensemble method reduces overfitting)
- Handles non-linear relationships
- Feature importance analysis available

**Model Specifications:**
- Algorithm: Random Forest Classifier
- Estimators: 500 trees
- Max Depth: 5
- Training Data: 11,249 records (75%)
- Test Data: 3,750 records (25%)
- Cross-Validation: 4-fold

### Training & Evaluation

```bash
# Quick Training (30-60 seconds)
python train_model_fast.py

# Advanced Training with GridSearch (5-10 minutes)
python train_and_save_model.py
```

The trained model is saved as **hr_rf1.pickle** (1.84 MB)

## Files in Repository

```
Employee Attrition Prediction & HR Analytics/
│
├── 🎯 WEB APPLICATIONS
│   ├── app.py                          # Streamlit web app (Recommended)
│   ├── app_flask.py                    # Flask alternative
│   ├── quickstart.py                   # Automated setup launcher
│   ├── utils.py                        # Helper functions
│   ├── templates/
│   │   └── index.html                  # Flask HTML template
│   └── requirements.txt                # Python dependencies
│
├── 📚 DOCUMENTATION
│   ├── README.md                       # This file (Updated!)
│   ├── START_HERE.md                   # Quick start guide
│   ├── SETUP_GUIDE.md                  # Detailed installation guide
│   ├── WEBAPP_README.md                # Web app user guide
│   ├── PROJECT_OVERVIEW.md             # Technical architecture
│   ├── QUICK_REFERENCE.md              # One-page reference
│   └── WEBAPP_README.md                # Web app documentation
│
├── 💾 DATA & MODEL
│   ├── HR_comma_sep.csv               # Employee dataset (14,999 records)
│   ├── hr_rf1.pickle                  # Trained Random Forest model (97.6% accuracy)
│   ├── train_and_save_model.py        # GridSearch training script
│   ├── train_model_fast.py            # Fast training script
│   └── Employee Attrition Prediction & HR Analytics.ipynb  # Jupyter notebook
│
└── 📊 ANALYSIS & RESULTS
    └── [Visualizations and analysis outputs]
```

## How to Use

### Quick Start (Recommended)

#### Option 1: Automated Setup
```bash
python quickstart.py
```
Automatically checks everything and launches the app!

#### Option 2: Streamlit Web App (Modern UI)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```
Then visit: **http://localhost:8501**

#### Option 3: Flask Web App (Full Control)
```bash
pip install -r requirements.txt
python app_flask.py
```
Then visit: **http://localhost:5000**

### Prerequisites
```
Python 3.8+
pip (Python package manager)
At least 2GB free disk space
```

### Full Installation Guide
See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed step-by-step instructions for all operating systems.

### Using the Web Application

1. **Enter Employee Data:**
   - Job Satisfaction Level (0-1)
   - Performance Evaluation Score (0-1)
   - Average Monthly Working Hours
   - Years at Company
   - Number of Projects
   - Work Accident History (Yes/No)
   - Promotion Status (Yes/No)
   - Department
   - Salary Level

2. **Click "Predict Employee Attrition"**

3. **Get Results:**
   - Risk Assessment (High/Low Risk)
   - Probability of Leaving (%)
   - HR Recommendations
   - Input Summary

### Running the Jupyter Notebook Analysis
```bash
jupyter notebook "Employee Attrition Prediction & HR Analytics.ipynb"
```

## 🚀 Quick Start Commands

```bash
# Clone the repository
git clone https://github.com/gramesh04/Employee-Attrition-Prediction-HR-Analytics.git
cd Employee-Attrition-Prediction-HR-Analytics

# Activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py           # Recommended
# OR
python app_flask.py            # Alternative
# OR
python quickstart.py           # Automated setup

# Access at http://localhost:8501 (Streamlit)
# Or http://localhost:5000 (Flask)
```

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [START_HERE.md](START_HERE.md) | Quick overview & getting started |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Complete installation guide |
| [WEBAPP_README.md](WEBAPP_README.md) | Web app features & usage |
| [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) | Technical architecture |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | One-page cheat sheet |

## 📚 Key Libraries

**Data Processing & Analysis:**
- pandas (2.0.3) - Data manipulation
- numpy (1.24.3) - Numerical computing

**Machine Learning:**
- scikit-learn (1.3.0) - ML algorithms & metrics
- xgboost (2.0.0) - Gradient boosting

**Web Frameworks:**
- Streamlit (1.28.1) - Interactive web apps
- Flask (2.3.0) - Web application framework

**Visualization:**
- matplotlib - Static plots
- seaborn - Statistical visualizations

**Utilities:**
- pickle - Model serialization
- pathlib - File path operations

## 💡 Model Insights

### Top Features Influencing Attrition
1. **Satisfaction Level** - Strong inverse correlation with attrition
2. **Average Monthly Hours** - Overwork significantly increases attrition
3. **Tenure** - Long-term employees less likely to leave
4. **Number of Projects** - Employees on too many projects leave
5. **Evaluation Score** - High performers under pressure leave more often

### Attrition Patterns
- **Overall Attrition Rate:** 23.81%
- **Critical Hours Threshold:** 240+ hours/month = high attrition
- **Optimal Project Load:** 3-4 projects (low attrition)
- **Satisfaction Threshold:** Below 0.5 = high attrition risk
- **Promotion Impact:** Lack of advancement increases risk

## Recommendations for HR

Based on the analysis, the following actions can improve employee retention:

1. **Workload Management**
   - Cap projects at 4 per employee
   - Maintain 160-200 hours/month as target
   - Identify and redistribute overloaded assignments

2. **Compensation & Promotion**
   - Link promotions more directly to performance and tenure
   - Review salary progression, especially for tenure-based roles
   - Ensure high performers receive career advancement

3. **Satisfaction Monitoring**
   - Regularly assess employee satisfaction levels
   - Investigate specific events around the 4-year mark
   - Implement interventions for declining satisfaction

4. **Department-Level Review**
   - While attrition varies by department, review individual roles
   - Identify burnout patterns within teams
   - Support managers in workload distribution

## 📊 Web Application Features

### Streamlit Version (app.py)
✅ Modern, interactive interface
✅ Real-time sliders for continuous inputs
✅ Color-coded risk indicators
✅ Mobile-responsive design
✅ HR recommendations engine
✅ Model information sidebar
✅ Professional styling

### Flask Version (app_flask.py)
✅ Full-featured web interface
✅ Beautiful HTML5 design
✅ REST API endpoints
✅ Custom CSS styling
✅ JavaScript interactions
✅ Production-ready architecture

### Key Features (Both Versions)
- 📈 Instant attrition predictions
- 🎯 Probability-based risk assessment
- 💡 Customized HR recommendations
- 📋 Input data summary
- 📊 Model performance metrics
- 🔒 Complete data privacy (local processing)
- ⚡ Sub-second predictions

## Ethical Considerations

- **Privacy:** All data is anonymized and aggregated
- **Fairness:** Models evaluated for potential bias across departments
- **Transparency:** Model predictions can be explained through feature importance
- **Application:** Predictions should support retention efforts, not punitive actions

## Limitations

1. Dataset appears to contain some synthetic/manipulated values (unusual distribution shapes)
2. Cross-sectional data; temporal patterns not captured
3. Missing context on major organizational events
4. Limited demographic variables for bias assessment

## Future Work

- Time-series analysis of employee satisfaction trends
- Deep learning models for improved predictions
- Explainability analysis (SHAP, LIME) for model interpretability
- Clustering analysis to identify employee personas
- Causal analysis to determine true drivers vs. correlations

## Resources & References

- [Kaggle HR Analytics Dataset](https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Employee Attrition Analysis Best Practices](https://en.wikipedia.org/wiki/Attrition_(employment))

## Author

**GANDEEDRAMESH**

## License

This project is open source and available under the MIT License.

## Contact & Support

For questions or feedback, please open an issue on the GitHub repository.

## 🌐 Deployment Options

### Local Deployment (Current)
```bash
streamlit run app.py
```
- Best for: Development, testing, local teams
- Access: http://localhost:8501
- Setup time: < 5 minutes

### Streamlit Cloud (Recommended for Demo)
```bash
# Push your repo to GitHub, then:
# Visit: https://streamlit.io/cloud
# Connect your GitHub account and select this repository
```
- Free tier available
- Auto-updates with git commits
- Shareable public URL

### Docker Containerization
```bash
docker build -t hr-attrition-app .
docker run -p 8501:8501 hr-attrition-app
```
- Consistent across environments
- Easy cloud deployment (AWS, Google Cloud, Azure)

### Cloud Platforms
- **Heroku** - https://www.heroku.com/ (Flask version)
- **AWS EC2** - https://aws.amazon.com/ (Full control)
- **Google Cloud Run** - https://cloud.google.com/run (Serverless)
- **Microsoft Azure** - https://azure.microsoft.com/ (Enterprise)

## 🔗 Repository Links

- **GitHub Repository:** [Employee-Attrition-Prediction-HR-Analytics](https://github.com/gramesh04/Employee-Attrition-Prediction-HR-Analytics)
- **Dataset Source:** [Kaggle HR Analytics](https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction)
- **Issues & Support:** GitHub Issues

## 📋 Troubleshooting

**Issue:** "Port already in use"
```bash
# Change port number
streamlit run app.py --server.port 8502
```

**Issue:** "Module not found"
```bash
# Reinstall requirements
pip install --upgrade -r requirements.txt
```

**Issue:** "Model file not found"
```bash
# Ensure hr_rf1.pickle exists in project root
# Or retrain: python train_model_fast.py
```

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for more troubleshooting.

---

**Last Updated:** December 2025

**Project Status:** ✅ **Complete - Web Applications Ready for Use**

**Version:** 2.0 (Web Application Edition)
