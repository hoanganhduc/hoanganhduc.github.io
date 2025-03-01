@echo off
setlocal enabledelayedexpansion

REM Check if GitHub CLI is installed
gh --version >nul 2>&1
if errorlevel 1 (
    echo GitHub CLI is not installed. Please install it first.
    exit /b 1
)

REM Get repository input from argument
if "%~1"=="" (
    echo Usage: %~nx0 owner/repo
    exit /b 1
)
set "repo=%~1"

REM Verify the repository input
gh repo view %repo% >nul 2>&1
if errorlevel 1 (
    echo Invalid repository: %repo%
    exit /b 1
)

REM Fetch releases using GitHub API
echo Fetching releases for %repo%...
set count=0
for /f "tokens=* usebackq" %%i in (`gh api repos/%repo%/releases --paginate --jq ".[].tag_name"`) do (
    set /a count+=1
    set "release[!count!]=%%i"
    echo !count!. %%i
)

if !count! equ 0 (
    echo No releases found for %repo%.
) else (
    REM Ask user for input
    set /p choice="Enter the numbers of the releases you want to delete (comma-separated, 'all' to delete all, or press Enter to skip): "

    if not "!choice!"=="" (
        if /i "!choice!" equ "all" (
            for /l %%i in (1,1,!count!) do (
                echo Deleting release and corresponding tag !release[%%i]!...
                gh release delete --cleanup-tag !release[%%i]! --repo %repo% --yes
            )
        ) else (
            for %%i in (!choice!) do (
                echo Deleting release and corresponding tag !release[%%i]!...
                gh release delete --cleanup-tag !release[%%i]! --repo %repo% --yes
            )
        )
    )
)

echo Done.
endlocal
