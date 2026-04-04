@echo off
echo ================================
echo Starting CareerPath AI System
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 16 or higher
    pause
    exit /b 1
)

echo [1/4] Setting up Backend...
cd backend

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment and install dependencies
echo Installing backend dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt >nul 2>&1

echo.
echo [2/4] Starting Backend Server...
start "Flask Backend" cmd /k "cd /d %CD% && venv\Scripts\activate.bat && python app.py"

REM Wait for backend to start
timeout /t 5 /nobreak >nul

cd ..
echo.
echo [3/4] Setting up Frontend...
cd frontend

REM Install frontend dependencies if needed
if not exist "node_modules" (
    echo Installing frontend dependencies...
    call npm install
)

echo.
echo [4/4] Starting Frontend Server...
start "React Frontend" cmd /k "cd /d %CD% && npm run dev"

echo.
echo ================================
echo ✅ System Started Successfully!
echo ================================
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Press any key to open the application in your browser...
pause >nul

start http://localhost:5173

cd ..
