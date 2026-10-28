# ============================================================
# sync_leetcode.ps1
# Exports LeetCode submissions and pushes to GitHub
# Usage: .\sync_leetcode.ps1
# ============================================================

$ErrorActionPreference = "Stop"

# ---- CONFIGURATION (fill these in) -------------------------
$GITHUB_REPO  = "https://github.com/Silapareddy-Praveen-Kumar-Reddy/Mycode.git"
$GITHUB_USER  = "Silapareddy-Praveen-Kumar-Reddy"
$LEETCODE_EXE = "C:\Users\pp911\AppData\Roaming\Python\Python313\Scripts\leetcode-export.exe"
$EXPORT_DIR   = "C:\Users\pp911\IdeaProjects\Mycode\submissions"
# -----------------------------------------------------------

Write-Host "`n=== LeetCode → GitHub Sync ===" -ForegroundColor Cyan

# Step 1: Ask for GitHub PAT (masked input)
$GITHUB_PAT = Read-Host -Prompt "Enter your GitHub Personal Access Token (PAT)" -AsSecureString
$GITHUB_PAT_PLAIN = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto(
    [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($GITHUB_PAT)
)

# Step 2: Ask for LeetCode cookie
Write-Host "`nPaste your LeetCode session cookie (from browser DevTools -> Network -> any request -> Request Headers -> cookie:)"
$LEET_COOKIE = Read-Host -Prompt "Cookie"

# Step 3: Clone or update the GitHub repo
Write-Host "`n[1/4] Setting up local repo..." -ForegroundColor Yellow
$repoDir = "C:\Users\pp911\IdeaProjects\Mycode"
Set-Location $repoDir

if (!(Test-Path "$repoDir\.git")) {
    # Embed PAT in URL for authentication
    $authUrl = "https://${GITHUB_USER}:${GITHUB_PAT_PLAIN}@github.com/Silapareddy-Praveen-Kumar-Reddy/Mycode.git"
    git clone $authUrl . 2>&1 | Write-Host
} else {
    Write-Host "Repo already initialized, pulling latest..."
    git pull 2>&1 | Write-Host
}

# Step 4: Export LeetCode submissions
Write-Host "`n[2/4] Exporting LeetCode submissions..." -ForegroundColor Yellow
if (!(Test-Path $EXPORT_DIR)) { New-Item -ItemType Directory -Path $EXPORT_DIR | Out-Null }
Set-Location $EXPORT_DIR

& $LEETCODE_EXE --cookies $LEET_COOKIE
if ($LASTEXITCODE -ne 0) {
    Write-Error "leetcode-export failed! Check your cookie and try again."
    exit 1
}
Write-Host "Export complete!" -ForegroundColor Green

# Step 5: Commit and push
Write-Host "`n[3/4] Committing changes..." -ForegroundColor Yellow
Set-Location $repoDir

git add .
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$commitMsg = "feat: sync LeetCode submissions ($timestamp)"
git commit -m $commitMsg 2>&1 | Write-Host

Write-Host "`n[4/4] Pushing to GitHub..." -ForegroundColor Yellow
$authUrl = "https://${GITHUB_USER}:${GITHUB_PAT_PLAIN}@github.com/Silapareddy-Praveen-Kumar-Reddy/Mycode.git"
git push $authUrl HEAD:main 2>&1 | Write-Host

Write-Host "`n✅ Done! Your LeetCode submissions are now on GitHub." -ForegroundColor Green
Write-Host "   https://github.com/Silapareddy-Praveen-Kumar-Reddy/Mycode" -ForegroundColor Cyan
