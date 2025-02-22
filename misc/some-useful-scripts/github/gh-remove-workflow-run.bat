@echo off
setlocal EnableDelayedExpansion

REM Check if GitHub CLI is installed
where gh >nul 2>&1
if errorlevel 1 (
  echo GitHub CLI is not installed. Exiting.
  pause
  exit /b 1
)

if "%~1"=="" goto usage

set "REPO=%~1"
echo Repository: %REPO%

REM Create a temporary file to store workflow runs
set "tempfile=%temp%\workflow_runs.txt"

REM Get workflow runs with more details
echo Fetching workflow runs...
gh api repos/%REPO%/actions/runs --jq ".workflow_runs[] | {id: .id, name: .name, status: .status, created_at: .created_at}" > "%tempfile%"

REM Count and display workflow runs
set /a count=0
echo.
echo Available workflow runs:
echo ---------------------
for /f "tokens=*" %%a in (%tempfile%) do (
  set /a count+=1
  echo !count!: %%a
)

if %count% EQU 0 (
  echo No workflow runs found.
  del "%tempfile%"
  pause
  exit /b 0
)

:input
echo.
echo Enter numbers of workflow runs to delete (comma or space-separated),
echo or type 'all' to delete all runs, or 'q' to quit:
set /p "selection="

if "%selection%"=="q" (
  echo Operation cancelled.
  del "%tempfile%"
  pause
  exit /b 0
)

if /i "%selection%"=="all" (
  call :deleteWorkflowRuns "%REPO%"
) else (
  REM Replace commas with spaces
  set "selection=%selection:,= %"
  
  REM Create an array to track processed numbers
  set "processed="
  
  REM Process individual selections
  for %%i in (%selection%) do (
    set /a num=%%i
    if !num! LEQ 0 (
      echo Invalid selection: %%i
      goto input
    )
    if !num! GTR %count% (
      echo Invalid selection: %%i
      goto input
    )
    
    REM Check if number was already processed
    echo !processed! | findstr /C:"[!num!]" >nul
    if errorlevel 1 (
      REM Add number to processed list
      set "processed=!processed![!num!]"
      
      for /f "tokens=* usebackq" %%j in (`powershell -Command "Get-Content '%tempfile%' | Select-Object -Index (!num!-1) | ConvertFrom-Json | Select-Object -ExpandProperty id"`) do (
        set "id=%%j"
        echo Deleting workflow run ID: !id!
        gh api --silent -X DELETE repos/%REPO%/actions/runs/!id!
      )
    ) else (
      echo Skipping duplicate selection: !num!
    )
  )
)

del "%tempfile%"
echo Workflow runs deletion completed.
pause
exit /b 0

:usage
echo Usage: %~nx0 ^<owner/repository^>
echo Example: %~nx0 octocat/Hello-World
exit /b 1

:deleteWorkflowRuns
setlocal
set "repo=%~1"
for /f "delims=" %%i in ('gh api repos/%repo%/actions/runs --jq ".workflow_runs[] | .id"') do (
  echo Deleting workflow run ID: %%i
  gh api --silent -X DELETE repos/%repo%/actions/runs/%%i
)
endlocal
exit /b 0
