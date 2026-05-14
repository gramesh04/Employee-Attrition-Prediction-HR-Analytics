# 🚀 Quick Reference Card

## Start the App (Choose One)

```bash
# Option 1: Automated setup (Recommended)
python quickstart.py

# Option 2: Streamlit (Modern UI)
streamlit run app.py

# Option 3: Flask (Full control)
python app_flask.py
```

## Access Points
- **Streamlit**: http://localhost:8501
- **Flask**: http://localhost:5000

---

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or install manually
pip install streamlit pandas numpy scikit-learn xgboost
```

---

## File Map

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app |
| `app_flask.py` | Flask alternative |
| `quickstart.py` | Auto setup |
| `utils.py` | Helper functions |
| `requirements.txt` | Dependencies |
| `hr_rf1.pickle` | Trained model |
| `HR_comma_sep.csv` | Training data |

---

## Input Features

1. **Satisfaction Level** (0-1): Job satisfaction
2. **Evaluation Score** (0-1): Performance review
3. **Projects**: Number of active projects
4. **Avg Hours**: Monthly working hours
5. **Tenure**: Years at company
6. **Accident**: Work accident (Yes/No)
7. **Promotion**: Promoted (Yes/No)
8. **Department**: Work department
9. **Salary**: Low / Medium / High

---

## Prediction Output

✅ **Low Risk** (Green)
- Employee likely to stay
- Probability: Usually <30%

⚠️ **High Risk** (Red)
- Employee may leave
- Probability: Usually >50%

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Model not found | Train from Jupyter notebook |
| Imports fail | `pip install -r requirements.txt` |
| Port in use | `streamlit run app.py --server.port 8502` |
| Slow startup | Normal; model loads first time |

---

## Documentation

- **Setup**: See `SETUP_GUIDE.md`
- **Usage**: See `WEBAPP_README.md`
- **Overview**: See `PROJECT_OVERVIEW.md`
- **Original**: See `README.md`

---

## Model Stats

- **Accuracy**: 98%
- **AUC**: 0.97
- **Training Data**: 14,999 records
- **Features**: 9
- **Algorithm**: Random Forest

---

## Key Shortcuts

```bash
# Stop app
Ctrl + C

# Switch browser
Cmd + Tab (Mac) / Alt + Tab (Windows)

# Open dev tools
F12

# Reload page
Ctrl + R

# Open terminal
Ctrl + ` (VS Code)
```

---

## Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Deactivate later
deactivate
```

---

## Performance Tips

- Close other apps
- Use Flask (lighter than Streamlit)
- Run on SSD (faster)
- Chrome/Edge browser (fastest)

---

## Default Values

- Satisfaction: 0.5
- Evaluation: 0.5
- Projects: 3
- Hours: 160
- Tenure: 3
- Accident: No
- Promotion: No
- Department: Sales
- Salary: Low

---

**Need help? See SETUP_GUIDE.md or PROJECT_OVERVIEW.md**
