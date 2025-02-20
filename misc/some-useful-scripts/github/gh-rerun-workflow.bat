@echo off
setlocal EnableDelayedExpansion

REM Check if GitHub CLI is installed
where gh >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo GitHub CLI is not installed. Please install it first.
    exit /b 1
)

REM Check if repository argument is provided
if "%~1"=="" (
    echo Usage: %~nx0 repository [branch]
    echo Example: %~nx0 owner/repo main
    exit /b 1
)

REM Store repository and branch arguments
set "repo=%~1"
set "branch=%~2"

REM Validate repository format
echo %repo% | findstr /r /c:"^[^/]*/[^/]*$" >nul
if %ERRORLEVEL% neq 0 (
    echo Invalid repository format. Use owner/repo format.
    exit /b 1
)

REM Create temporary file for workflow runs
set "temp_file=%TEMP%\workflow_runs.txt"

REM List workflow runs and store in temporary file
if "%branch%"=="" (
    echo Listing all workflow runs...
    gh run list --repo %repo% --limit 20 > "%temp_file%"
) else (
    echo Listing workflow runs for branch: %branch%
    gh run list --repo %repo% --branch %branch% --limit 20 > "%temp_file%"
)

REM Display numbered workflow runs
set "count=1"
for /f "usebackq tokens=1* delims=	" %%a in ("%temp_file%") do (
    echo [!count!] %%a	%%b
    set /a "count+=1"
)

:prompt
set /p "selection=Enter number to re-run (or 'q' to quit): "

if "%selection%"=="q" (
    del "%temp_file%"
    echo Exiting...
    exit /b 0
)

REM Validate selection is a number
echo %selection%| findstr /r "^[1-9][0-9]*$" >nul
if %ERRORLEVEL% neq 0 (
    echo Invalid selection. Please enter a valid number or 'q' to quit.
    goto prompt
)

REM Check if selection is within range
if %selection% GEQ %count% (
    echo Invalid selection. Number out of range.
    goto prompt
)

REM Get run ID for selected number
set "current_count=1"
for /f "usebackq tokens=1* delims=	" %%a in ("%temp_file%") do (
    if !current_count! equ %selection% (
        set "run_id=%%a"
        goto rerun
    )
    set /a "current_count+=1"
)

:rerun
REM Re-run the workflow
echo Re-running workflow run ID: %run_id%
gh run rerun %run_id% --repo %repo%

if %ERRORLEVEL% equ 0 (
    echo Workflow re-run initiated successfully.
) else (
    echo Failed to re-run workflow.
)

del "%temp_file%"
exit /b 0