@echo off

REM Check if GitHub CLI is installed
where gh >nul 2>&1
if errorlevel 1 (
  echo GitHub CLI is not installed. Exiting.
  pause
  exit /b 1
)

REM This script deletes all workflow runs for a specific GitHub repository using gh CLI.
REM It now asks for confirmation before deleting workflow runs.
REM Usage: gh-remove-workflow-run.bat ^<username^> ^<repository^>

if "%~1"=="" goto usage
if "%~2"=="" goto usage

set "REPO=%~1/%~2"
echo Repository: %REPO%

REM Ask for confirmation
choice /m "Are you sure you want to delete all workflow runs for %REPO%?"
if errorlevel 2 (
    echo Aborted.
    pause
    exit /b 0
)

call :deleteWorkflowRuns "%REPO%"
echo All workflow runs have been processed.
pause
exit /b 0

:usage
echo Usage: gh-remove-workflow-run.bat ^<username^> ^<repository^>
exit /b 1

:deleteWorkflowRuns
setlocal
set "repo=%~1"
REM Retrieve a list of workflow run IDs using gh api, then delete each workflow run.
for /f "delims=" %%i in ('gh api repos/%repo%/actions/runs --jq ".workflow_runs[] | .id"') do (
  echo Deleting workflow run ID: %%i
  gh api --silent -X DELETE repos/%repo%/actions/runs/%%i
)
endlocal
exit /b 0