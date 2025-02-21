@echo off
REM A script to download and upload files to a Google Drive shared folder using rclone

REM Set default values
set DEFAULT_REMOTE="gdrive"
set DEFAULT_REMOTE_DIR="SharedFolder"
set DEFAULT_LOCAL_DIR=%~dp0
set SCRIPT_NAME=%~n0%~x0

REM Define list of excluded files and folders
set EXCLUDES=
set EXCLUDES=%EXCLUDES% --exclude="%0"
set EXCLUDES=%EXCLUDES% --exclude="*.tmp"
set EXCLUDES=%EXCLUDES% --exclude=".git/**"
set EXCLUDES=%EXCLUDES% --exclude="node_modules/**"
set EXCLUDES=%EXCLUDES% --exclude="*.log"
set EXCLUDES=%EXCLUDES% --exclude="desktop.ini"
set EXCLUDES=%EXCLUDES% --exclude="Thumbs.db"

REM Initialize variables with defaults
set REMOTE=%DEFAULT_REMOTE%
set REMOTE_DIR=%DEFAULT_REMOTE_DIR%
set LOCAL_DIR=%DEFAULT_LOCAL_DIR%
set ACTION=

:parse_args
if "%~1"=="" goto check_requirements
if /i "%~1"=="-r" set REMOTE=%~2& shift & shift & goto parse_args
if /i "%~1"=="-rd" set REMOTE_DIR=%~2& shift & shift & goto parse_args
if /i "%~1"=="-ld" set LOCAL_DIR=%~2& shift & shift & goto parse_args
if /i "%~1"=="download" set ACTION=download& shift & goto parse_args
if /i "%~1"=="upload" set ACTION=upload& shift & goto parse_args
shift
goto parse_args

:print_usage
echo Usage: %SCRIPT_NAME% [download^|upload] [-r remote_name] [-rd remote_dir] [-ld local_dir]
echo.
echo Default values:
echo   remote_name (-r):  %DEFAULT_REMOTE%
echo   remote_dir  (-rd): %DEFAULT_REMOTE_DIR%
echo   local_dir   (-ld): %DEFAULT_LOCAL_DIR%
exit /b

:check_requirements
REM Check if rclone is installed
where rclone >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: rclone is not installed or not in PATH
    echo Please install rclone from https://rclone.org/downloads/
    exit /b 1
)

REM Check if the remote exists in rclone config
rclone listremotes | findstr /B /L /I "%REMOTE%:" >nul
if %errorlevel% neq 0 (
    echo Error: Remote '%REMOTE%' is not configured in rclone
    echo Please run 'rclone config' to set up the remote
    exit /b 1
)

:check_action
if "%ACTION%"=="" (
    call :print_usage
    exit /b 1
)

if "%ACTION%"=="download" (
    rclone --drive-shared-with-me copy "%REMOTE%:%REMOTE_DIR%" "%LOCAL_DIR%" --progress %EXCLUDES% && echo Download completed successfully || echo Download failed
) else if "%ACTION%"=="upload" (
    rclone --drive-shared-with-me copy "%LOCAL_DIR%" "%REMOTE%:%REMOTE_DIR%" --progress %EXCLUDES% && echo Upload completed successfully || echo Upload failed
)

echo Done!
exit /b 0