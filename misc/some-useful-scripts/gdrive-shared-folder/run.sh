#!/bin/bash
# A script to download and upload files to a Google Drive shared folder using rclone
#
# This script facilitates downloading and uploading files to a Google Drive shared folder using rclone.
# 
# Usage:
#   bash run.sh [download|upload]
#
# Arguments:
#   download  - Downloads files from the specified Google Drive shared folder to the local directory.
#   upload    - Uploads files from the local directory to the specified Google Drive shared folder.
#
# Variables:
#   REMOTE_DIR - The name of the directory in the Google Drive shared folder.
#   LOCAL_DIR  - The local directory where the script is located.
#   REMOTE     - The name of the remote configuration in rclone.
#
# Notes:
#   - The script excludes "run.sh" and "run.bat" files from being copied during both download and upload operations.
#   - The script uses the --drive-shared-with-me flag to access shared files in Google Drive.
#   - The script provides progress information during the copy operations.
#   - The script prints a success or failure message based on the result of the rclone operation.
#   - If an invalid argument is provided, the script prints usage information.

# Define the name of the directory in the Google Drive shared folder
REMOTE_DIR="SharedFolder"
# Define the local directory where the script is located
LOCAL_DIR="$(dirname "$(realpath "$0")")"
# Define the name of the remote configuration in rclone
REMOTE="gdrive"

# Check if the first argument is "download"
if [ "$1" == "download" ]; then
    # Download files from Google Drive to local directory
    rclone --drive-shared-with-me copy "$REMOTE:$REMOTE_DIR" "$LOCAL_DIR" --progress --exclude="run.sh"
    # Check if the rclone command was successful
    if [ $? -eq 0 ]; then
        echo "Download completed successfully."
    else
        echo "Download failed."
    fi
# Check if the first argument is "upload"
elif [ "$1" == "upload" ]; then
    # Upload files from local directory to Google Drive
    rclone --drive-shared-with-me copy "$LOCAL_DIR" "$REMOTE:$REMOTE_DIR" --progress --exclude="run.sh"
    # Check if the rclone command was successful
    if [ $? -eq 0 ]; then
        echo "Upload completed successfully."
    else
        echo "Upload failed."
    fi
# If the argument is neither "download" nor "upload"
else
    echo "Invalid argument. Use \"download\" or \"upload\"."
    echo "Usage: bash $0 [download|upload]"
fi

# Print a completion message
echo "Done!"