@echo off
setlocal EnableDelayedExpansion

REM Check if GitHub CLI is installed
where gh >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo GitHub CLI is not installed. Please install it first.
    echo Visit: https://cli.github.com/
    exit /b 1
)

REM Check if repository argument is provided
if "%~1"=="" (
    echo Usage: %~nx0 repository [destination_folder]
    echo Example: %~nx0 owner/repo [D:\downloads]
    exit /b 1
)

set "REPO=%~1"
set "DEST_FOLDER=%~2"

REM List all releases with numbers
echo Fetching releases from %REPO%...
set "counter=1"
set "releases="
for /f "tokens=*" %%a in ('gh release list --repo %REPO%') do (
    echo !counter!^) %%a
    set "release_!counter!=%%a"
    set /a "counter+=1"
)
set /a "last_number=counter-1"

:prompt_selection
REM Prompt user to enter release numbers
echo.
echo Enter the release numbers to download (separate multiple numbers with spaces)
echo Example: 1 3 5 (or 'q' to quit)
set /p "SELECTION=Your selection: "
if "%SELECTION%"=="q" exit /b 0

REM If destination folder is not provided, create one in Downloads
if "%DEST_FOLDER%"=="" (
    set "DEST_FOLDER=%USERPROFILE%\Downloads\%REPO:.=_%"
    echo No destination folder specified. Using: !DEST_FOLDER!
)

REM Process each selected number
for %%n in (%SELECTION%) do (
    set "num=%%n"
    if !num! leq !last_number! if !num! gtr 0 (
        for /f "tokens=2" %%t in ("!release_%%n!") do (
            set "TAG=%%t"
            
            REM Create release-specific subfolder
            set "RELEASE_FOLDER=!DEST_FOLDER!\!TAG!"
            if not exist "!RELEASE_FOLDER!" mkdir "!RELEASE_FOLDER!"
            
            echo.
            echo Downloading release !TAG! to "!RELEASE_FOLDER!"...
            gh release download !TAG! --repo %REPO% --dir "!RELEASE_FOLDER!"
            
            if !ERRORLEVEL! equ 0 (
                echo Download completed for release !TAG!
            ) else (
                echo Error occurred while downloading release !TAG!
            )
        )
    ) else (
        echo Invalid selection: %%n
    )
)

echo.
echo All downloads completed.
echo Files saved to: !DEST_FOLDER!

exit /b 0