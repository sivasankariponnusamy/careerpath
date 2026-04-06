# Restart Frontend to Use Local Backend
# This ensures the frontend picks up the .env.local configuration

Write-Host "🔄 Restarting Frontend to use local backend..." -ForegroundColor Cyan
Write-Host ""

# Kill existing frontend process
$frontendPID = (Get-NetTCPConnection -LocalPort 5173 -ErrorAction SilentlyContinue).OwningProcess
if ($frontendPID) {
    Write-Host "⏹️  Stopping existing frontend (PID: $frontendPID)..." -ForegroundColor Yellow
    Stop-Process -Id $frontendPID -Force
    Start-Sleep -Seconds 2
}

# Verify .env.local exists
if (Test-Path "frontend\.env.local") {
    Write-Host "✅ .env.local found" -ForegroundColor Green
    Get-Content "frontend\.env.local"
} else {
    Write-Host "⚠️  Creating .env.local..." -ForegroundColor Yellow
    "VITE_API_URL=http://localhost:5000/api" | Out-File -FilePath "frontend\.env.local" -Encoding utf8
    Write-Host "✅ .env.local created" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Starting frontend..." -ForegroundColor Cyan
Write-Host ""

# Start frontend
Push-Location frontend
Start-Process powershell -ArgumentList "-NoExit", "-Command", "npm run dev"
Pop-Location

Write-Host ""
Write-Host "✅ Frontend restarted!" -ForegroundColor Green
Write-Host ""
Write-Host "📱 Frontend: " -NoNewline
Write-Host "http://localhost:5173" -ForegroundColor Blue
Write-Host "🔧 Backend:  " -NoNewline  
Write-Host "http://localhost:5000" -ForegroundColor Blue
Write-Host ""
Write-Host "⚠️  IMPORTANT: Wait 5 seconds for frontend to start, then:" -ForegroundColor Yellow
Write-Host "   1. Refresh your browser (Ctrl+F5)" -ForegroundColor Gray
Write-Host "   2. Upload a resume" -ForegroundColor Gray
Write-Host "   3. Check database with: cd backend; python test_database.py" -ForegroundColor Gray
Write-Host ""
