#!/bin/bash
# Deploy Backend to Vercel

echo "🚀 Deploying CareerPath Backend to Vercel..."
echo ""
echo "Step 1: Installing Vercel CLI (if not installed)"
npm install -g vercel

echo ""
echo "Step 2: Deploying backend to production"
cd backend
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Next Steps:"
echo "1. Copy the production URL from above (e.g., https://careerpath-ai-xxx.vercel.app)"
echo "2. Go to Vercel Dashboard: https://vercel.com/dashboard"
echo "3. Click on your project > Storage > Create Database"
echo "4. Select 'Postgres' and create it"
echo "5. The DATABASE_URL will be auto-configured"
echo "6. Test your deployment by uploading a resume!"
