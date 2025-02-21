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

REM Fetch releases and tags
echo Fetching releases and tags for %repo%...
set count=0
for /f "tokens=*" %%i in ('gh release list -R %repo%') do (
    set /a count+=1
    set "release[!count!]=%%i"
    echo !count!. %%i
)

if !count! equ 0 (
    echo No releases found for %repo%.
    exit /b 1
)

REM Ask user for input
set /p choice="Enter the numbers of the releases you want to delete (comma-separated, or 'all' to delete all releases): "

if /i "%choice%" equ "all" (
    for /l %%i in (1,1,!count!) do (
        for /f "tokens=1" %%j in ("!release[%%i]!") do (
            echo Deleting release %%j...
            gh release delete %%j -R %repo% -y
        )
    )
) else (
    for %%i in (%choice%) do (
        for /f "tokens=1" %%j in ("!release[%%i]!") do (
            echo Deleting release %%j...
            gh release delete %%j -R %repo% -y
        )
    )
)

REM Fetch tags
echo Fetching tags for %repo%...
set count=0
for /f "tokens=*" %%i in ('gh tag list -R %repo%') do (
    set /a count+=1
    set "tag[!count!]=%%i"
    echo !count!. %%i
)

if !count! equ 0 (
    echo No tags found for %repo%.
    exit /b 1
)

REM Ask user for input
set /p choice="Enter the numbers of the tags you want to delete (comma-separated, or 'all' to delete all tags): "

if /i "%choice%" equ "all" (
    for /l %%i in (1,1,!count!) do (
        for /f "tokens=1" %%j in ("!tag[%%i]!") do (
            echo Deleting tag %%j...
            gh tag delete %%j -R %repo% -y
        )
    )
) else (
    for %%i in (%choice%) do (
        for /f "tokens=1" %%j in ("!tag[%%i]!") do (
            echo Deleting tag %%j...
            gh tag delete %%j -R %repo% -y
        )
    )
)

echo Done.
endlocal