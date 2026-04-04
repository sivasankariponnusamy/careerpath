#!/bin/bash

echo "================================"
echo "Starting CareerPath AI System"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    echo "Please install Node.js 16 or higher"
    exit 1
fi

echo "[1/4] Setting up Backend..."
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
echo "Installing backend dependencies..."
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

echo ""
echo "[2/4] Starting Backend Server..."
python app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

cd ..
echo ""
echo "[3/4] Setting up Frontend..."
cd frontend

# Install frontend dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

echo ""
echo "[4/4] Starting Frontend Server..."
npm run dev &
FRONTEND_PID=$!

cd ..

echo ""
echo "================================"
echo "✅ System Started Successfully!"
echo "================================"
echo ""
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Wait for user interrupt
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
