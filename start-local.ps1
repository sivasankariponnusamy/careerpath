# Start CareerPath AI in Local Development Mode
# This script starts both backend and frontend servers

Write-Host "🚀 Starting CareerPath AI - Local Development Mode" -ForegroundColor Cyan
Write-Host ""

# Function to check if a command exists
function Test-CommandExists {
    param($command)
    $null -ne (Get-Command $command -ErrorAction SilentlyContinue)
}

# Check prerequisites
Write-Host "📋 Checking prerequisites..." -ForegroundColor Blue

if (-not (Test-CommandExists python)) {
    Write-Host "⚠️  Python not found. Please install Python 3.8+" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-CommandExists node)) {
    Write-Host "⚠️  Node.js not found. Please install Node.js 16+" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Prerequisites OK" -ForegroundColor Green
Write-Host ""

# Start Backend
Write-Host "🔧 Starting Backend Server..." -ForegroundColor Blue
Push-Location backend

# Check if virtual environment exists
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

# Activate virtual environment and install dependencies
& .venv\Scripts\Activate.ps1
pip install -r requirements.txt | Out-Null

# Start backend in background
Start-Process -NoNewWindow python -ArgumentList "main.py" -PassThru | Out-Null
Write-Host "✅ Backend started on http://localhost:5000" -ForegroundColor Green
Pop-Location

# Wait for backend to initialize
Write-Host "Waiting for backend to initialize..."
Start-Sleep -Seconds 3

# Start Frontend
Write-Host ""
Write-Host "🎨 Starting Frontend Server..." -ForegroundColor Blue
Push-Location frontend

# Install dependencies if needed
if (-not (Test-Path "node_modules")) {
    Write-Host "Installing frontend dependencies..."
    npm install
}

# Check if .env.local exists
if (-not (Test-Path ".env.local")) {
    Write-Host "Creating .env.local file..."
    "VITE_API_URL=http://localhost:5000/api" | Out-File -FilePath ".env.local" -Encoding utf8
}

# Start frontend
Write-Host "✅ Starting frontend..." -ForegroundColor Green
Start-Process -NoNewWindow npm -ArgumentList "run", "dev"
Pop-Location

Write-Host ""
Write-Host "🎉 CareerPath AI is running!" -ForegroundColor Green
Write-Host ""
Write-Host "📱 Frontend: " -NoNewline
Write-Host "http://localhost:5173" -ForegroundColor Blue
Write-Host "🔧 Backend:  " -NoNewline
Write-Host "http://localhost:5000" -ForegroundColor Blue
Write-Host ""
Write-Host "To test database storage:" -ForegroundColor Yellow
Write-Host "  cd backend" -ForegroundColor Gray
Write-Host "  python test_database.py" -ForegroundColor Gray
Write-Host ""
Write-Host "Press Ctrl+C in the terminal windows to stop the servers" -ForegroundColor Yellow
