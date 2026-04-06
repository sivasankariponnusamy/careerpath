#!/bin/bash
# Start CareerPath AI in Local Development Mode
# This script starts both backend and frontend servers

echo "🚀 Starting CareerPath AI - Local Development Mode"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo -e "${BLUE}📋 Checking prerequisites...${NC}"

if ! command_exists python3; then
    echo -e "${YELLOW}⚠️  Python 3 not found. Please install Python 3.8+${NC}"
    exit 1
fi

if ! command_exists node; then
    echo -e "${YELLOW}⚠️  Node.js not found. Please install Node.js 16+${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Prerequisites OK${NC}"
echo ""

# Start Backend
echo -e "${BLUE}🔧 Starting Backend Server...${NC}"
cd backend

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment and install dependencies
source .venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1

# Start backend in background
python main.py &
BACKEND_PID=$!
echo -e "${GREEN}✅ Backend started on http://localhost:5000 (PID: $BACKEND_PID)${NC}"
cd ..

# Wait for backend to be ready
echo "Waiting for backend to initialize..."
sleep 3

# Start Frontend
echo ""
echo -e "${BLUE}🎨 Starting Frontend Server...${NC}"
cd frontend

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Start frontend
echo -e "${GREEN}✅ Starting frontend...${NC}"
npm run dev &
FRONTEND_PID=$!

cd ..

echo ""
echo -e "${GREEN}🎉 CareerPath AI is running!${NC}"
echo ""
echo -e "📱 Frontend: ${BLUE}http://localhost:5173${NC}"
echo -e "🔧 Backend:  ${BLUE}http://localhost:5000${NC}"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop all servers${NC}"
echo ""

# Wait for Ctrl+C
trap "echo ''; echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
