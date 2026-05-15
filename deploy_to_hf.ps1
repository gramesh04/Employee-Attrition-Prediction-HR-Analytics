#!/usr/bin/env powershell
<#
.SYNOPSIS
    Automated deployment helper for Hugging Face Spaces
.DESCRIPTION
    This script helps deploy the Employee Attrition Predictor to Hugging Face Spaces
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File deploy_to_hf.ps1
#>

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Hugging Face Spaces Deployment Helper  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Git
Write-Host "[1/5] Checking Git installation..." -ForegroundColor Yellow
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git not found! Please install Git from https://git-scm.com" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Git is installed" -ForegroundColor Green
git --version
Write-Host ""

# Step 2: Check Hugging Face CLI
Write-Host "[2/5] Checking Hugging Face CLI..." -ForegroundColor Yellow
if (!(Get-Command huggingface-cli -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️  Hugging Face CLI not installed. Installing..." -ForegroundColor Yellow
    pip install huggingface-hub --upgrade
}
Write-Host "✅ Hugging Face CLI ready" -ForegroundColor Green
Write-Host ""

# Step 3: Verify project files
Write-Host "[3/5] Verifying project files..." -ForegroundColor Yellow
$requiredFiles = @("app.py", "requirements.txt", "hr_rf1.pickle", "README.md")
$allFilesMissing = $false

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "✅ $file found" -ForegroundColor Green
    } else {
        Write-Host "❌ $file NOT found" -ForegroundColor Red
        $allFilesMissing = $true
    }
}

if ($allFilesMissing) {
    Write-Host "Please run this script from the project root directory!" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 4: Git commit
Write-Host "[4/5] Preparing Git commit..." -ForegroundColor Yellow
git add .
git commit -m "Prepare for Hugging Face Spaces deployment" -q
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Changes committed" -ForegroundColor Green
} else {
    Write-Host "⚠️  No changes to commit (this is fine)" -ForegroundColor Yellow
}
Write-Host ""

# Step 5: Manual steps
Write-Host "[5/5] Next Steps - Manual Configuration Required:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Open https://huggingface.co/spaces" -ForegroundColor Cyan
Write-Host "2. Click 'Create new Space'" -ForegroundColor Cyan
Write-Host "3. Fill in:" -ForegroundColor Cyan
Write-Host "   - Space name: Employee-Attrition-Predictor" -ForegroundColor White
Write-Host "   - SDK: Streamlit" -ForegroundColor White
Write-Host "   - Visibility: Public" -ForegroundColor White
Write-Host "4. Once created, copy the git URL from the Space" -ForegroundColor Cyan
Write-Host ""
Write-Host "5. Then run these commands:" -ForegroundColor Cyan
Write-Host '   cd ..\new-space-folder' -ForegroundColor White
Write-Host '   Copy-Item ..\employee-attrition-*\app.py .' -ForegroundColor White
Write-Host '   Copy-Item ..\employee-attrition-*\requirements.txt .' -ForegroundColor White
Write-Host '   Copy-Item ..\employee-attrition-*\hr_rf1.pickle .' -ForegroundColor White
Write-Host '   git add .' -ForegroundColor White
Write-Host '   git commit -m "Deploy app"' -ForegroundColor White
Write-Host '   git push' -ForegroundColor White
Write-Host ""
Write-Host "6. Your app will be live at:" -ForegroundColor Cyan
Write-Host "   https://huggingface.co/spaces/gramesh0404/Employee-Attrition-Predictor" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host "  Deployment preparation complete! ✅" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
