# Employee Attrition Prediction Web Application

A machine learning-powered web application built with Streamlit that predicts employee attrition risk using a trained Random Forest model.

## 📋 Overview

This application provides HR departments with a data-driven tool to identify employees at risk of leaving the company. By inputting employee metrics, the model predicts the likelihood of attrition and provides actionable insights for retention strategies.

## 🎯 Features

- **Interactive User Interface**: Easy-to-use form for entering employee data
- **Real-time Predictions**: Instant attrition risk assessment
- **Probability Scores**: Detailed probability percentages for both outcomes
- **Visual Feedback**: Color-coded results (red for risk, green for secure)
- **HR Recommendations**: Contextual suggestions based on prediction outcome
- **Input Summary**: Review of all entered data before making decisions
- **Model Info**: Transparency about model performance and accuracy

## 📊 Model Details

- **Algorithm**: Random Forest Classifier
- **Training Data**: 14,999 employee records
- **Features**: 9 key employee metrics
- **Accuracy**: ~98%
- **AUC Score**: ~0.97

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project directory**
   ```bash
   cd "Employee Attrition Prediction & HR Analytics"
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Navigate to the project directory**
   ```bash
   cd "Employee Attrition Prediction & HR Analytics"
   ```

2. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

3. **Access the application**
   - The app will open in your default browser at `http://localhost:8501`
   - If it doesn't open automatically, manually visit the URL shown in the terminal

## 📝 How to Use

1. **Enter Employee Information**: Fill in the form with the employee's details:
   - Job Satisfaction Level (0-1)
   - Last Evaluation Score (0-1)
   - Average Monthly Hours Worked
   - Years at Company
   - Number of Projects
   - Work Accident History (Yes/No)
   - Promotion in Last 5 Years (Yes/No)
   - Department
   - Salary Level

2. **Click "Predict Employee Attrition"**: The model will analyze the data

3. **Review Results**:
   - High Risk (Probability > 50%): Employee may be at risk of leaving
   - Low Risk (Probability < 50%): Employee is likely to stay
   - Probability percentages for both outcomes
   - Customized HR recommendations

## 🔄 Input Parameters

### Numeric Inputs (0-1 Scale)
- **Job Satisfaction Level**: Employee's self-reported satisfaction (0 = low, 1 = high)
- **Last Evaluation Score**: Performance review rating (0 = poor, 1 = excellent)

### Integer Inputs
- **Average Monthly Hours**: Hours worked per month (typical range: 100-300)
- **Years at Company**: Employee tenure (0-50 years)
- **Number of Projects**: Active project assignments (0-20)

### Binary Inputs (Yes/No)
- **Work Accident**: Whether employee experienced workplace accident
- **Promotion in Last 5 Years**: Recent promotion history

### Categorical Inputs
- **Department**: Sales, Accounting, HR, IT, Management, Marketing, Product Management, R&D, Support, Technical
- **Salary Level**: Low, Medium, or High

## 📁 Project Structure

```
Employee Attrition Prediction & HR Analytics/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── hr_rf1.pickle                   # Trained Random Forest model
├── HR_comma_sep.csv               # Training dataset
├── Employee Attrition Prediction & HR Analytics.ipynb  # Model training notebook
└── README.md                       # Original project README
```

## 🛠️ Technical Stack

- **Streamlit**: Web framework for ML apps
- **scikit-learn**: Machine learning algorithms
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **XGBoost**: Gradient boosting (used in model training)

## 📈 Model Training

The Random Forest model was trained using:
- 14,999 employee records
- 9-feature input space
- Grid search cross-validation for hyperparameter optimization
- Stratified train-test split (75% training, 25% testing)

For detailed model training code, see: `Employee Attrition Prediction & HR Analytics.ipynb`

## 💡 HR Use Cases

### Retention Strategy
- Identify at-risk employees proactively
- Schedule intervention meetings before employees leave
- Address dissatisfaction or overwork issues

### Compensation Review
- Identify if salary level is a factor in attrition predictions
- Benchmark compensation against industry standards

### Workload Management
- Monitor average working hours
- Redistribute projects to prevent burnout
- Balance team capacity

### Career Development
- Identify employees without recent promotions
- Create advancement pathways
- Plan succession planning

## ⚠️ Important Notes

1. **Data Privacy**: This application operates locally with no external data transmission
2. **Model Limitations**: Predictions are based on historical data patterns and should complement, not replace, human judgment
3. **Feature Encoding**: Categorical variables (Department, Salary) are automatically encoded to match training data
4. **Assumption**: The model assumes input features are independent and follow training data distributions

## 🔐 Data Security

- No employee data is stored or transmitted to external servers
- All processing happens locally on your machine
- The model file is loaded from local storage only

## 🐛 Troubleshooting

### "Model file not found" error
- Ensure `hr_rf1.pickle` is in the same directory as `app.py`
- Check the file hasn't been moved or deleted

### Slow predictions
- This is typically normal; model prediction is very fast
- If persistent, restart the Streamlit app

### Encoding errors
- Ensure all categorical inputs match the available options
- Check that numeric inputs are within valid ranges

## 📞 Support

For issues or questions about:
- **Model training**: See the Jupyter notebook `Employee Attrition Prediction & HR Analytics.ipynb`
- **Streamlit features**: Visit https://docs.streamlit.io/
- **scikit-learn**: Visit https://scikit-learn.org/

## 📚 References

- Original Dataset: HR Analytics and Job Prediction (Kaggle)
- Streamlit Documentation: https://docs.streamlit.io/
- scikit-learn Documentation: https://scikit-learn.org/

## 📝 License

This project is provided as-is for educational and business intelligence purposes.

---

**Created**: 2024
**Framework**: Streamlit
**Model**: Random Forest Classifier
**Status**: Production Ready
