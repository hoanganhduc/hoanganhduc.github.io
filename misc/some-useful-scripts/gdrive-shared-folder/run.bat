@echo off
REM A script to download and upload files to a Google Drive shared folder using rclone

REM Set the name of the remote directory on Google Drive
set REMOTE_DIR="SharedFolder"
REM Set the local directory to the directory where the script is located
set LOCAL_DIR=%~dp0
REM Set the name of the remote (Google Drive) configured in rclone
set REMOTE="gdrive"

REM Check if the first argument is "download"
if "%1"=="download" (
    REM Download files from Google Drive to the local directory
    rclone --drive-shared-with-me copy "%REMOTE%:%REMOTE_DIR%" %LOCAL_DIR% --progress --exclude="run.bat"
    REM Check if the rclone command was successful
    if %errorlevel% equ 0 (
        echo Download completed successfully.
    ) else (
        echo Download failed.
    )
) else if "%1"=="upload" (
    REM Check if the first argument is "upload"
    REM Upload files from the local directory to Google Drive
    rclone --drive-shared-with-me copy %LOCAL_DIR% "%REMOTE%:%REMOTE_DIR%" --progress --exclude="run.bat"
    REM Check if the rclone command was successful
    if %errorlevel% equ 0 (
        echo Upload completed successfully.
    ) else (
        echo Upload failed.
    )
) else (
    REM If the argument is neither "download" nor "upload", print an error message
    echo Invalid argument. Use "download" or "upload".
    echo Usage: %0 [download|upload]
)

REM Indicate that the script has finished running
echo Done!