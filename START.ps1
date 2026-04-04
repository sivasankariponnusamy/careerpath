# Quick Start Script for AI Career Recommendation System

Write-Host "🎓 AI-Driven Career Recommendation System" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check if Node.js is installed
Write-Host "Checking Node.js installation..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "✓ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Node.js not found! Please install Node.js 16+" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Setting up Backend..." -ForegroundColor Cyan
Write-Host "===================" -ForegroundColor Cyan

# Navigate to backend directory
Set-Location -Path "backend"

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -q -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

Write-Host ""
Write-Host "Starting Backend Server..." -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host "Backend will run on: http://localhost:5000" -ForegroundColor Green
Write-Host ""

# Start backend in a new window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; venv\Scripts\Activate.ps1; python main.py"

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Navigate to frontend directory
Set-Location -Path "..\frontend"

Write-Host ""
Write-Host "Setting up Frontend..." -ForegroundColor Cyan
Write-Host "=====================" -ForegroundColor Cyan

# Check if node_modules exists
if (Test-Path "node_modules") {
    Write-Host "✓ Node modules found" -ForegroundColor Green
} else {
    Write-Host "Installing Node dependencies..." -ForegroundColor Yellow
    npm install
    Write-Host "✓ Dependencies installed" -ForegroundColor Green
}

Write-Host ""
Write-Host "Starting Frontend Server..." -ForegroundColor Cyan
Write-Host "===========================" -ForegroundColor Cyan
Write-Host "Frontend will run on: http://localhost:5173" -ForegroundColor Green
Write-Host ""

Write-Host "🎉 System is starting up!" -ForegroundColor Green
Write-Host ""
Write-Host "Access the application at: http://localhost:5173" -ForegroundColor Cyan
Write-Host "Backend API available at: http://localhost:5000/api" -ForegroundColor Cyan
Write-Host ""
Write-Host "To install LLaMA AI (optional):" -ForegroundColor Yellow
Write-Host "1. Download Ollama from: https://ollama.ai" -ForegroundColor Yellow
Write-Host "2. Run: ollama pull llama2" -ForegroundColor Yellow
Write-Host ""

# Start frontend
npm run dev

# Navigate back to root
Set-Location -Path ".."
