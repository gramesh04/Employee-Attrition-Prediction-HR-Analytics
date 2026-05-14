#!/usr/bin/env python3
"""
Quick Start Script for Employee Attrition Prediction Web Application
This script automates the setup and launch process
"""

import subprocess
import sys
import os
from pathlib import Path


def print_header():
    """Print application header."""
    print("\n" + "="*70)
    print(" "*15 + "🚀 Employee Attrition Prediction App")
    print(" "*20 + "Quick Start Guide")
    print("="*70 + "\n")


def check_python_version():
    """Check if Python version meets requirements."""
    print("✓ Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  ✅ Python {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"  ❌ Python {version.major}.{version.minor} (requires 3.8+)")
        return False


def check_model_file():
    """Check if model file exists."""
    print("\n✓ Checking for trained model...")
    model_path = Path('hr_rf1.pickle')
    if model_path.exists():
        print(f"  ✅ Model found: {model_path.absolute()}")
        return True
    else:
        print(f"  ❌ Model not found at {model_path.absolute()}")
        print("  ⚠️  You need to train and save the model from the Jupyter notebook first")
        return False


def check_data_file():
    """Check if data file exists."""
    print("\n✓ Checking for data file...")
    data_path = Path('HR_comma_sep.csv')
    if data_path.exists():
        print(f"  ✅ Data found: {data_path.absolute()}")
        return True
    else:
        print(f"  ⚠️  Data file not found at {data_path.absolute()}")
        return False


def check_requirements_installed():
    """Check if all required packages are installed."""
    print("\n✓ Checking installed packages...")
    required_packages = ['streamlit', 'pandas', 'numpy', 'sklearn', 'xgboost']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing.append(package)
    
    return len(missing) == 0, missing


def install_requirements():
    """Install required packages."""
    print("\n✓ Installing requirements...")
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("  ✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("  ❌ Failed to install requirements")
        return False


def choose_application():
    """Let user choose which application to run."""
    print("\n" + "="*70)
    print("Choose your application:\n")
    print("  1️⃣  Streamlit Version (Recommended for beginners)")
    print("  2️⃣  Flask Version (More customizable)")
    print("  3️⃣  Exit")
    print("="*70 + "\n")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    return choice


def run_streamlit():
    """Launch Streamlit application."""
    print("\n" + "="*70)
    print("🚀 Launching Streamlit Application...")
    print("="*70)
    print("\n📌 The app will open in your browser at http://localhost:8501")
    print("📌 Press Ctrl+C in this terminal to stop the application\n")
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\n\n✅ Application stopped")
    except Exception as e:
        print(f"\n❌ Error running Streamlit: {e}")
        return False
    
    return True


def run_flask():
    """Launch Flask application."""
    print("\n" + "="*70)
    print("🚀 Launching Flask Application...")
    print("="*70)
    print("\n📌 The app will be available at http://127.0.0.1:5000")
    print("📌 Press Ctrl+C in this terminal to stop the application\n")
    
    try:
        subprocess.run([sys.executable, 'app_flask.py'])
    except KeyboardInterrupt:
        print("\n\n✅ Application stopped")
    except Exception as e:
        print(f"\n❌ Error running Flask: {e}")
        return False
    
    return True


def show_troubleshooting():
    """Show troubleshooting tips."""
    print("\n" + "="*70)
    print("📚 TROUBLESHOOTING TIPS")
    print("="*70)
    print("""
Common issues and solutions:

1. "Model file not found"
   → Train and save the model from the Jupyter notebook
   → Ensure hr_rf1.pickle is in the project directory

2. "ModuleNotFoundError: No module named 'streamlit'"
   → Run: pip install -r requirements.txt
   → Or: pip install streamlit pandas numpy scikit-learn

3. "Port already in use"
   → For Streamlit: streamlit run app.py --server.port 8502
   → For Flask: Edit app_flask.py and change the port number

4. Application runs slowly
   → This is normal on first run (model loading)
   → Close other applications using system resources

For more help, see SETUP_GUIDE.md

""")
    print("="*70 + "\n")


def main():
    """Main function."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    
    # Check Python version
    if not check_python_version():
        print("\n❌ Python 3.8 or higher is required")
        print("   Visit: https://www.python.org/downloads/")
        return
    
    # Check model file
    if not check_model_file():
        print("\n" + "="*70)
        print("⚠️  IMPORTANT: Model file missing!")
        print("="*70)
        print("\nYou need to:")
        print("1. Open 'Employee Attrition Prediction & HR Analytics.ipynb'")
        print("2. Run all cells to train the Random Forest model")
        print("3. The notebook will save the model as 'hr_rf1.pickle'")
        print("\nOnce saved, run this script again.\n")
        return
    
    # Check data file
    check_data_file()
    
    # Check requirements
    all_installed, missing = check_requirements_installed()
    
    if not all_installed:
        print("\n" + "="*70)
        print("📦 Missing packages detected!")
        print("="*70)
        response = input("\nInstall missing packages now? (y/n): ").strip().lower()
        
        if response == 'y':
            if not install_requirements():
                print("\n❌ Failed to install requirements")
                print("Try manually: pip install -r requirements.txt")
                return
        else:
            print("\nManual installation:")
            print("  pip install -r requirements.txt")
            return
    
    # Choose and run application
    while True:
        choice = choose_application()
        
        if choice == '1':
            run_streamlit()
        elif choice == '2':
            run_flask()
        elif choice == '3':
            print("\n👋 Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.\n")
    
    # Show troubleshooting
    response = input("\nWould you like to see troubleshooting tips? (y/n): ").strip().lower()
    if response == 'y':
        show_troubleshooting()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("For help, see SETUP_GUIDE.md\n")
