# 🚀 Hugging Face Spaces Deployment Guide

## Step-by-Step Deployment Instructions

### Step 1: Create a Hugging Face Space

1. Go to **https://huggingface.co/spaces**
2. Click **"Create new Space"** button
3. Fill in the details:
   - **Space name:** `Employee-Attrition-Predictor` (or your preferred name)
   - **Owner:** Select your username (`gramesh0404`)
   - **License:** Choose `openrail` or `mit`
   - **Space SDK:** Select **Streamlit**
   - **Visibility:** **Public** (to make it accessible to everyone)
4. Click **"Create Space"**

### Step 2: Configure Git Credentials (One-Time Setup)

Run these commands in your terminal:

```powershell
git config --global user.email "your_email@example.com"
git config --global user.name "gramesh0404"
```

### Step 3: Clone Your Hugging Face Space

After creating the Space, Hugging Face will show you the repository URL. Clone it:

```powershell
cd Desktop
git clone https://huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor
cd Employee-Attrition-Predictor
```

### Step 4: Copy Your Application Files

Copy all files from your local project to the cloned Space folder:

```powershell
# Copy app files
Copy-Item "..\Employee Attrition Prediction & HR Analytics\app.py" .
Copy-Item "..\Employee Attrition Prediction & HR Analytics\requirements.txt" .
Copy-Item "..\Employee Attrition Prediction & HR Analytics\hr_rf1.pickle" .
Copy-Item "..\Employee Attrition Prediction & HR Analytics\README.md" .
Copy-Item "..\Employee Attrition Prediction & HR Analytics\.streamlit\config.toml" -Recurse -Force

# Optional: Copy HTML template if using Flask version
Copy-Item "..\Employee Attrition Prediction & HR Analytics\templates" -Recurse -Force
```

### Step 5: Create App File Structure

Hugging Face Spaces expects a specific structure. Make sure these files exist:

```
your-space-folder/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── hr_rf1.pickle          # Trained model
├── README.md              # Description
└── .streamlit/
    └── config.toml        # Streamlit configuration
```

### Step 6: Push to Hugging Face

```powershell
cd Employee-Attrition-Predictor

# Add all files
git add .

# Commit changes
git commit -m "Deploy Employee Attrition Predictor"

# Push to Hugging Face (this triggers automatic deployment)
git push
```

### Step 7: Wait for Deployment

1. Go back to your Space on Hugging Face
2. You'll see a **"Building"** status
3. Wait 2-5 minutes for deployment to complete
4. Once complete, you'll see a **"Running"** status
5. A live app URL will appear at the top right

### Step 8: Share Your Live App!

Your app will be live at:
```
https://huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor
```

---

## 🔑 Hugging Face Authentication (If Needed)

If prompted for Hugging Face credentials:

```powershell
# Login to Hugging Face
huggingface-cli login

# You'll be asked for your Hugging Face token
# Get your token from: https://huggingface.co/settings/tokens
```

## ✅ Verification Checklist

- [ ] Space created on Hugging Face
- [ ] All files copied to Space folder
- [ ] `requirements.txt` includes all dependencies
- [ ] `hr_rf1.pickle` is in the root folder
- [ ] `.streamlit/config.toml` exists
- [ ] Changes pushed to Hugging Face
- [ ] Space shows "Running" status
- [ ] Can access the live URL

## 🐛 Troubleshooting

**Problem:** "Model file not found"
- Solution: Make sure `hr_rf1.pickle` is in the root folder and committed to git

**Problem:** "Module not found" error
- Solution: Ensure all packages are listed in `requirements.txt`

**Problem:** App won't load or shows "Building" indefinitely
- Solution: Check the Space's "Logs" tab for error messages
- Click the "Logs" button on your Space page

**Problem:** Authentication failed when pushing
- Solution: Run `huggingface-cli login` and enter your Hugging Face token

## 📊 Other Deployment Options

### Alternative 1: Streamlit Cloud
```
https://streamlit.io/cloud
```
- Pros: Same as Hugging Face, simpler setup
- Cons: Fewer customization options

### Alternative 2: Render.com
```
https://render.com
```
- Pros: More control, supports Flask
- Cons: Limited free tier

### Alternative 3: Railway
```
https://railway.app
```
- Pros: Generous free tier, simple deployment
- Cons: May require credit card

---

**Current Project Status:** Ready for deployment ✅
