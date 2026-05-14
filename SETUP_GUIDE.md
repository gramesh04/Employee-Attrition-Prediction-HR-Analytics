# 🚀 Setup Guide: Employee Attrition Prediction Web Application

This guide covers setting up and running both the **Streamlit** and **Flask** versions of the application.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Troubleshooting](#troubleshooting)
5. [Features Comparison](#features-comparison)

---

## Prerequisites

### System Requirements
- **Windows**, **macOS**, or **Linux**
- **Python 3.8 or higher**
- **pip** (Python package manager)
- At least 2GB of free disk space

### Verify Python Installation
Open Command Prompt (Windows) or Terminal (macOS/Linux) and run:

```bash
python --version
```

Should output: `Python 3.8.0` or higher

---

## Installation

### Step 1: Navigate to Project Directory

**Windows:**
```powershell
cd "C:\Users\YourUsername\OneDrive\Desktop\Employee Attrition Prediction & HR Analytics"
```

**macOS/Linux:**
```bash
cd ~/Desktop/"Employee Attrition Prediction & HR Analytics"
```

### Step 2: Create Virtual Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated.

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

For Flask version (alternative dependencies):
```bash
pip install flask==2.3.0 scikit-learn==1.3.0 pandas==2.0.3 numpy==1.24.3
```

### Step 4: Verify Model File

Ensure `hr_rf1.pickle` exists in the project directory:

**Windows:**
```powershell
Test-Path "hr_rf1.pickle"
```

**macOS/Linux:**
```bash
ls -la hr_rf1.pickle
```

If the file is missing, regenerate it from the Jupyter notebook.

---

## Running the Application

### Option 1: Streamlit Version (Recommended for Beginners)

Streamlit is easier to use and provides a modern, interactive interface.

#### Start the Application

```bash
streamlit run app.py
```

#### Access the Application

- The app will automatically open in your default browser
- If not, visit: **http://localhost:8501**

#### Stop the Application

Press **Ctrl+C** in the terminal

#### Features
- ✅ Interactive sliders and input fields
- ✅ Real-time predictions
- ✅ Color-coded results
- ✅ Beautiful, responsive design
- ✅ Automatic caching for performance

---

### Option 2: Flask Version (More Control)

Flask provides more customization and control over the web application.

#### Start the Application

```bash
python app_flask.py
```

#### Access the Application

- Visit: **http://127.0.0.1:5000** in your browser

#### Stop the Application

Press **Ctrl+C** in the terminal

#### Features
- ✅ Full control over routing and responses
- ✅ RESTful API endpoints
- ✅ Custom HTML/CSS styling
- ✅ JSON-based predictions
- ✅ Extensible architecture

---

## Troubleshooting

### Issue: "Python command not found"

**Solution:**
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation
- Restart your terminal after installation

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
# Ensure virtual environment is activated
# Then reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Model file not found"

**Solution:**
1. Verify `hr_rf1.pickle` exists in the project directory
2. Check the file path is correct
3. If missing, regenerate from the Jupyter notebook:
   ```python
   # In the notebook, run:
   write_pickle(path, rf1, 'hr_rf1')
   ```

### Issue: Port already in use

**For Streamlit:**
```bash
streamlit run app.py --server.port 8502
```

**For Flask:**
```python
# Edit app_flask.py, change:
app.run(port=5001)  # Use different port
```

### Issue: Application runs but predictions fail

**Solution:**
1. Ensure all dependencies are installed: `pip list`
2. Check that the model file is not corrupted
3. Verify input values are within valid ranges
4. Check browser console (F12) for error messages

### Issue: Slow loading on first run

**Normal behavior.** The application:
- Loads the machine learning model (~5-10 seconds)
- Initializes libraries
- Subsequent loads are faster

---

## Features Comparison

| Feature | Streamlit | Flask |
|---------|-----------|-------|
| **Setup Difficulty** | Very Easy | Moderate |
| **User Interface** | Modern, Built-in | Custom HTML/CSS |
| **Performance** | Fast | Very Fast |
| **Customization** | Limited | Extensive |
| **Real-time Updates** | Yes | Yes |
| **Documentation** | Excellent | Comprehensive |
| **Learning Curve** | Shallow | Moderate |
| **Best For** | Data Scientists | Full-stack Developers |

---

## Additional Tips

### 1. **Running Both Versions Simultaneously**

Keep two terminal windows open:

**Terminal 1 (Streamlit):**
```bash
streamlit run app.py
```

**Terminal 2 (Flask):**
```bash
python app_flask.py
```

Access:
- Streamlit: http://localhost:8501
- Flask: http://localhost:5000

### 2. **Deactivate Virtual Environment**

When done, deactivate the virtual environment:

**Windows:**
```powershell
deactivate
```

**macOS/Linux:**
```bash
deactivate
```

### 3. **Update Dependencies**

To update all packages to their latest versions:

```bash
pip install --upgrade -r requirements.txt
```

### 4. **Export Requirements**

If you add new packages, update requirements.txt:

```bash
pip freeze > requirements.txt
```

### 5. **Run in Production**

For production deployment (not local testing):

**Streamlit Cloud:**
```bash
streamlit run app.py --logger.level=warning
```

**Flask with Gunicorn:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app_flask:app
```

---

## Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Model file (`hr_rf1.pickle`) exists in project directory
- [ ] HR CSV data file exists
- [ ] Successfully started the application
- [ ] Application loads in browser
- [ ] Successfully made a prediction

---

## Next Steps

After successful installation:

1. **Explore the Interface**: Try different employee profiles
2. **Review Predictions**: Understand the model's decision-making
3. **Read Documentation**: Check `WEBAPP_README.md` for detailed feature info
4. **Experiment**: Test edge cases and unusual scenarios
5. **Customize**: Modify styling or features as needed

---

## Performance Optimization

### For Slow Computers
- Close other applications
- Use Flask instead of Streamlit (lighter)
- Reduce browser tabs/extensions

### For Better Performance
- Use SSD storage
- Increase RAM allocation
- Update Python and pip
- Run on a faster internet connection (if remote)

---

## Security Notes

- **Local Only**: By default, apps run on `localhost` (only accessible locally)
- **No Data Storage**: No employee data is stored permanently
- **No External Calls**: All processing is local
- **Model Security**: The pickle file is a binary - keep it secure

---

## Getting Help

### Common Resources
1. **Streamlit Documentation**: https://docs.streamlit.io/
2. **Flask Documentation**: https://flask.palletsprojects.com/
3. **scikit-learn Documentation**: https://scikit-learn.org/
4. **Python Official Docs**: https://docs.python.org/3/

### Debugging
1. Check terminal output for error messages
2. Enable debug mode in Flask (`debug=True`)
3. Check browser console (F12) for JavaScript errors
4. Verify all files are in the correct directory

---

## Support

If you encounter issues:

1. **Read the error message carefully** - it usually tells you the problem
2. **Check this guide's Troubleshooting section**
3. **Verify all prerequisites are met**
4. **Try reinstalling dependencies**: `pip install -r requirements.txt --force-reinstall`
5. **Restart your computer** - sometimes this solves unexpected issues

---

**Happy Predicting! 🎯**
