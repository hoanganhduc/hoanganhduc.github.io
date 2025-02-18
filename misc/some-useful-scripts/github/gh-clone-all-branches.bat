@echo off
setlocal EnableDelayedExpansion

if "%~1"=="" (
    echo Usage: %0 repo-id [folder]
    exit /b 1
)

set "REPO=%~1"
rem Check if REPO contains a slash to validate repo-id format (e.g., username/repository)
echo %REPO% | find "/" >nul 2>&1
if errorlevel 1 (
    echo Invalid repo-id. Expected format: username/repository.
    echo Usage: %0 repo-id [folder]
    exit /b 1
)

if "%~2"=="" (
    for /f "tokens=2 delims=/" %%A in ("%REPO%") do set "FOLDER=%%A"
) else (
    set "FOLDER=%~2"
)

set "SSH_URL=git@github.com:%REPO%.git"
set "HTTPS_URL=https://github.com/%REPO%.git"

echo Cloning repository using SSH: %SSH_URL% into folder %FOLDER%...
git clone %SSH_URL% %FOLDER%
if errorlevel 1 (
    echo SSH clone failed. Trying clone using HTTPS: %HTTPS_URL%...
    git clone %HTTPS_URL% %FOLDER%
    if errorlevel 1 (
        echo Failed to clone repository using both SSH and HTTPS.
        exit /b 1
    )
)

pushd %FOLDER%
echo Creating local tracking branches for all remote branches...

for /f "tokens=* delims=" %%L in ('git branch -r ^| findstr /v /c:"->"') do (
    rem Remove leading spaces
    for /f "tokens=* delims= " %%B in ("%%L") do (
        set "branch=%%B"
        if /i not "!branch!"=="origin/HEAD" (
            set "localbranch=!branch:origin/=!"
            git branch --track !localbranch! !branch! 2>nul
        )
    )
)

popd
endlocal