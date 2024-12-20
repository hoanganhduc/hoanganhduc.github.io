@echo off

:: Get some information
set "CURRENT_DIR=%CD%"
set "TMP_DIR=%TEMP%\%RANDOM%"
set "GITHUB_USERNAME=hoanganhduc"

:: Parse command line arguments
if "%1"=="clone" (
    set "GITHUB_REPO_ID=%2"
    set "OVERLEAF_PROJECT_ID=%3" 
    set "WORKDIR=%CURRENT_DIR%\%GITHUB_REPO_ID%"
) else if "%1"=="github" (
    set "GITHUB_REPO_ID=%2"
    set "OVERLEAF_PROJECT_ID="
    set "WORKDIR=%CURRENT_DIR%\%GITHUB_REPO_ID%"
) else if "%1"=="overleaf" (
    set "GITHUB_REPO_ID="
    set "OVERLEAF_PROJECT_ID=%2"
    set "WORKDIR=%CURRENT_DIR%\%OVERLEAF_PROJECT_ID%"
) else if "%1"=="makefile" (
    set "WORKDIR=%CURRENT_DIR%"
    if not "%2"=="" set "MAKEFILE_OPTION=%2"
) else if "%1"=="initiate" (
    set "GITHUB_REPO_ID=%2"
    set "OVERLEAF_PROJECT_ID=%3"
    set "WORKDIR=%CURRENT_DIR%\%GITHUB_REPO_ID%"
)

:: Set repository URLs
set "GITHUB_REPO_URL=git@github.com:%GITHUB_USERNAME%/%GITHUB_REPO_ID%.git"
set "OVERLEAF_PROJECT_URL=https://git@git.overleaf.com/%OVERLEAF_PROJECT_ID%"

:: Download required files using PowerShell
mkdir "%TMP_DIR%"
powershell -Command "(New-Object Net.WebClient).DownloadString('https://hoanganhduc.github.io/tex/exclude.txt')" > %TMP_DIR%\exclude.txt
powershell -Command "(New-Object Net.WebClient).DownloadString('https://hoanganhduc.github.io/tex/gitignore')" > %TMP_DIR%\.gitignore
powershell -Command "(New-Object Net.WebClient).DownloadString('https://hoanganhduc.github.io/tex/devcontainer.json')" > %TMP_DIR%\devcontainer.json

:: Define files to delete
set "DELETE_FILES=Makefile make.bat exclude.txt .devcontainer README*"

:: Main logic based on command
if "%1"=="clone" (
    call :clone_repo
) else if "%1"=="github" (
    call :clone_repo
) else if "%1"=="overleaf" (
    call :clone_repo
) else if "%1"=="makefile" (
    call :run_makefile
) else if "%1"=="initiate" (
    call :initiate
) else (
    call :print_usage
    exit /b 1
)

goto :eof

:print_usage
:: Print usage instructions
echo Usage: %0 {clone^|github^|overleaf^|makefile^|initiate} [options]
echo Commands:
echo   clone ^<github_repo_id^> ^<overleaf_project_id^>  Clone both GitHub and Overleaf repositories
echo   github ^<github_repo_id^>                      Clone only GitHub repository
echo   overleaf ^<overleaf_project_id^>               Clone only Overleaf repository
echo   makefile [makefile_option]                   Run Makefile in subdirectories
echo   initiate ^<github_repo_id^> ^<overleaf_project_id^> Initiate a new project with GitHub and Overleaf
goto :eof

:check_args_num
:: Check if the required number of arguments are provided for each command
if "%1"=="clone" (
    if "%3"=="" (
        echo Missing arguments
        call :print_usage
        exit /b 1
    )
) else if "%1"=="github" (
    if "%2"=="" (
        echo Missing arguments
        call :print_usage
        exit /b 1
    )
) else if "%1"=="overleaf" (
    if "%2"=="" (
        echo Missing arguments
        call :print_usage
        exit /b 1
    )
) else if "%1"=="initiate" (
    if "%3"=="" (
        echo Missing arguments
        call :print_usage
        exit /b 1
    )
)
goto :eof

:rename_workdir
:: Rename the working directory
set /p NEW_WORKDIR="Do you want to rename the directory %WORKDIR%? Press Enter to skip or type the new name: "
if not "%NEW_WORKDIR%"=="" (
    ren "%WORKDIR%" "%NEW_WORKDIR%"
    echo %WORKDIR% renamed to %NEW_WORKDIR%
)
exit /b 0
goto :eof

:clone_repo
:: Clone the repository based on the provided arguments
call :check_args_num
if exist "%WORKDIR%\.git" (
    echo Repository already cloned.
    goto :eof
)

if not "%GITHUB_REPO_ID%"=="" (
    if not "%OVERLEAF_PROJECT_ID%"=="" (
        echo Cloning GitHub repository %GITHUB_REPO_ID% and Overleaf project %OVERLEAF_PROJECT_ID%
    ) else (
        echo Cloning GitHub repository %GITHUB_REPO_ID%
    )
    mkdir "%WORKDIR%" >nul 2>&1
    cd "%WORKDIR%"
    git init
    git remote add origin "%GITHUB_REPO_URL%"
    git fetch --all
    for /f "tokens=*" %%b in ('git branch -r ^| findstr /v "\-\^\>"') do (
        set "branch=%%b"
        setlocal enabledelayedexpansion
        set "branch=!branch:origin/=!"
        git branch --track "!branch!" "%%b"
        endlocal
    )
    if not "%OVERLEAF_PROJECT_ID%"=="" (
        echo Configuring Git for Overleaf
        > .git\config (
            echo [core]
            echo     repositoryformatversion = 0
            echo     filemode = true
            echo     bare = false
            echo     logallrefupdates = true
            echo [remote "origin"]
            echo     url = %GITHUB_REPO_URL%
            echo     fetch = +refs/heads/*:refs/remotes/origin/*
            echo [branch "master"]
            echo     remote = origin
            echo     merge = refs/heads/master
            echo [remote "overleaf"]
            echo     url = %OVERLEAF_PROJECT_URL%
            echo     fetch = +refs/heads/*:refs/remotes/overleaf/*
            echo     pushurl = %OVERLEAF_PROJECT_URL%
            echo [branch "overleaf"]
            echo     remote = overleaf
            echo     merge = refs/heads/master
        )
    )
    git pull --all
    git checkout master
    cd "%CURRENT_DIR%"
    ) else (
        if not "%OVERLEAF_PROJECT_ID%"=="" (
            echo Cloning Overleaf project %OVERLEAF_PROJECT_ID%
            git clone "%OVERLEAF_PROJECT_URL%" "%WORKDIR%"
        ) else (
            call :print_usage
            exit /b 1
        )
    )
    call :rename_workdir
goto :eof

:run_makefile
:: Run Makefile in subdirectories
call :check_args_num
@for /f "tokens=*" %%a in ('dir /b /s /ad "%WORKDIR%"') do (
    @if exist "%%a\Makefile" (
        @echo Entering "%%a" 
        @cd "%%a" 
        @make "%MAKEFILE_OPTION%"
        @cd "%WORKDIR%"
    )
)
goto :eof

:merge_master_to_overleaf
:: Merge master branch to overleaf branch
echo Merging master onto overleaf
git checkout overleaf
git merge --no-commit --no-ff --allow-unrelated-histories master
for %%f in (%DELETE_FILES%) do (
    if exist "%%f" (
        git rm -rf "%%f"
    )
)
git add --all .
git commit -S -m "Merge master onto overleaf %date% %time%"
git push -u origin overleaf
git push -u overleaf overleaf:master
git checkout master
goto :eof

:merge_overleaf_to_master
:: Merge overleaf branch to master branch
git pull --all
git checkout overleaf
git checkout master
git merge --no-commit --no-ff --allow-unrelated-histories overleaf
git commit -S -m "Merge overleaf onto master %date% %time%"
git push -u origin master
goto :eof

:initiate
:: Initiate a new project with GitHub and Overleaf
call :check_args_num
if not exist "%WORKDIR%" (
    echo Please create a directory named %WORKDIR% and put your LaTeX contents here
    exit /b 1
)

if exist "%WORKDIR%\.git" (
    echo Repository already cloned
    exit /b 1
)

echo Initiating the repository '%WORKDIR%'
cd "%WORKDIR%"
copy %TMP_DIR%\exclude.txt "%WORKDIR%"
copy %TMP_DIR%\.gitignore "%WORKDIR%"
if not exist ".devcontainer" (
    mkdir ".devcontainer"
    copy %\TMP_DIR%\devcontainer.json "%WORKDIR%\.devcontainer"
)
git init
git remote add origin "%GITHUB_REPO_URL%"
git add --all .
git commit -S -m "first commit %date% %time%"
git push -u origin master
git checkout --orphan overleaf
git rm -rf .
git remote add overleaf %OVERLEAF_PROJECT_URL%
git pull overleaf master --allow-unrelated-histories
echo Configuring Git for Overleaf
call :merge_master_to_overleaf
cd "%CURRENT_DIR%"
goto :eof