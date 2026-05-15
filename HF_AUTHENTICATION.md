# 🔐 Hugging Face Authentication & Final Push

## Your Space is Almost LIVE! ✅

**Status:** ✅ All files ready (16.46 MB total)
- ✅ app.py (Streamlit application)  
- ✅ hr_rf1.pickle (Trained model - 16.45 MB)
- ✅ requirements.txt (Dependencies)
- ✅ README.md (Documentation)

**What's Next:** Authenticate and push (2 minutes)

---

## 🔑 Step-by-Step Authentication

### Method 1: Using Git Credentials (Easiest)

1. **Go to Hugging Face Settings:**
   - Visit: https://huggingface.co/settings/tokens
   - Click "Create new token"
   - Name: "Employee Attrition Predictor"
   - Type: "write"
   - **Copy the token**

2. **Authenticate with Git:**
   ```powershell
   git config --global credential.helper store
   ```

3. **Push to HF:**
   ```powershell
   cd "c:\Users\gande\OneDrive\Desktop\Employee Attrition Prediction & HR Analytics\Employee-Attrition-Predictor"
   git push origin main
   ```

4. **When prompted for username/password:**
   - **Username:** `gramesh0404`
   - **Password:** Paste your Hugging Face token

---

### Method 2: Configure Git Credentials (Permanent)

```powershell
git config --global user.email "your-email@example.com"
git config --global user.name "gramesh0404"
git config --global credential.helper wincred
```

Then push:
```powershell
cd "c:\Users\gande\OneDrive\Desktop\Employee Attrition Prediction & HR Analytics\Employee-Attrition-Predictor"
git push origin main
```

---

### Method 3: Using HTTPS Token URL

```powershell
# Set remote with token embedded
git remote set-url origin https://gramesh0404:YOUR_HF_TOKEN@huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor.git

# Then push
git push origin main
```

⚠️ **Warning:** Don't commit this URL to public repositories!

---

## ✅ Verification

After pushing, check if deployment started:

1. **Go to your Space:**
   ```
   https://huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor
   ```

2. **Look for:**
   - ✅ Status changes to "Building"
   - ✅ After 2-5 minutes → "Running"
   - ✅ App URL appears (top right)

3. **If stuck on "Building":**
   - Click "Logs" tab
   - Check for error messages
   - Common issue: missing dependencies in requirements.txt

---

## 📦 Your Deployment Package

```
Employee-Attrition-Predictor/
├── app.py                    # Streamlit web application
├── requirements.txt          # Dependencies: streamlit, pandas, scikit-learn
├── hr_rf1.pickle            # Trained Random Forest model (97.6% accuracy)
├── README.md                # Documentation
├── .streamlit/
│   └── config.toml          # Streamlit configuration
└── .gitattributes           # Git LFS settings
```

---

## 🎉 Once Deployed

Your app will be accessible at:
```
https://huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor
```

Users can:
- 📊 Input employee data
- 🤖 Get instant attrition predictions
- 📈 See probability of leaving
- 💡 Receive HR recommendations

---

## 🚀 Quick Command (After Getting Token)

```powershell
cd "c:\Users\gande\OneDrive\Desktop\Employee Attrition Prediction & HR Analytics\Employee-Attrition-Predictor"

# Authenticate once
git config --global credential.helper store

# Push
git push origin main

# Enter when prompted:
# Username: gramesh0404
# Password: <your-hugging-face-token>
```

**That's it!** Your app will be live in 2-5 minutes! 🎊

---

**Need Help?**
- Check Hugging Face Spaces documentation: https://huggingface.co/docs/hub/spaces
- Your Space Logs: https://huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor
