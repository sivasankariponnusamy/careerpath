# Deploy Backend to Vercel (Windows PowerShell)

Write-Host "🚀 Deploying CareerPath Backend to Vercel..." -ForegroundColor Green
Write-Host ""
Write-Host "Step 1: Installing Vercel CLI (if not installed)" -ForegroundColor Yellow
npm install -g vercel

Write-Host ""
Write-Host "Step 2: Deploying backend to production" -ForegroundColor Yellow
cd backend
vercel --prod

Write-Host ""
Write-Host "✅ Deployment complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Next Steps:" -ForegroundColor Cyan
Write-Host "1. Copy the production URL from above (e.g., https://careerpath-ai-xxx.vercel.app)"
Write-Host "2. Go to Vercel Dashboard: https://vercel.com/dashboard"
Write-Host "3. Click on your project > Storage > Create Database"
Write-Host "4. Select 'Postgres' and create it"
Write-Host "5. The DATABASE_URL will be auto-configured"
Write-Host "6. Upload Surya-Resume-1.pdf again to test - should now show 'Full Stack Developer' 34.12%!"
