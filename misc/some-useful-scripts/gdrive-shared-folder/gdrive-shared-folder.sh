#!/bin/bash
# A script to download and upload files to a Google Drive shared folder using rclone

# Function to print usage information
print_usage() {
    echo "Usage: bash $(basename "$0") [download|upload] [remote_name] [remote_dir] [local_dir]"
    echo
    echo "Arguments:"
    echo "  download    - Downloads files from the specified Google Drive shared folder to the local directory."
    echo "  upload      - Uploads files from the local directory to the specified Google Drive shared folder."
    echo "  remote_name - The name of the remote configuration in rclone (default: gdrive)."
    echo "  remote_dir  - The name of the directory in the Google Drive shared folder (default: SharedFolder)."
    echo "  local_dir   - The local directory path (default: current script directory)."
}

# Function to print configuration
print_config() {
    echo "Current Configuration:"
    echo "  Operation:     $1"
    echo "  Remote Name:   $2"
    echo "  Remote Dir:    $3"
    echo "  Local Dir:     $4"
    echo
}

# Check if we have enough arguments
if [ $# -lt 1 ]; then
    echo "Error: Invalid number of arguments."
    print_usage
    exit 1
fi

# Define default values
DEFAULT_REMOTE="gdrive"
DEFAULT_REMOTE_DIR="SharedFolder"
DEFAULT_LOCAL_DIR="$(dirname "$(realpath "$0")")"

# Get remote name, directory and local directory from arguments or use defaults
REMOTE="${2:-$DEFAULT_REMOTE}"
REMOTE_DIR="${3:-$DEFAULT_REMOTE_DIR}"
LOCAL_DIR="${4:-$DEFAULT_LOCAL_DIR}"

# Check if rclone is installed
if ! command -v rclone &> /dev/null; then
    echo "Error: rclone is not installed. Please install it first."
    echo "Visit https://rclone.org/install/ for installation instructions."
    exit 1
fi

# Check if the specified remote exists in rclone config
if ! rclone listremotes | grep -q "^${REMOTE}:"; then
    echo "Error: Remote '${REMOTE}' is not configured in rclone."
    echo "Please run 'rclone config' to set up the remote first."
    exit 1
fi

# Define list of excluded files and folders
EXCLUDED_ITEMS=(
    "$0"
    ".git/**"
    ".gitignore"
    "*.tmp"
    "*.temp"
    "*~"
    ".DS_Store"
    "Thumbs.db"
    "desktop.ini"
    "__pycache__/**"
    "node_modules/**"
)

# Create the exclude parameter string for rclone
EXCLUDE_PARAMS=""
for item in "${EXCLUDED_ITEMS[@]}"; do
    EXCLUDE_PARAMS="$EXCLUDE_PARAMS --exclude=\"$item\""
done

# Print configuration before processing
print_config "$1" "$REMOTE" "$REMOTE_DIR" "$LOCAL_DIR"

# Check if the first argument is "download"
if [ "$1" == "download" ]; then
    # Download files from Google Drive to local directory
    eval "rclone --drive-shared-with-me copy \"$REMOTE:$REMOTE_DIR\" \"$LOCAL_DIR\" --progress $EXCLUDE_PARAMS"
    # Check if the rclone command was successful
    if [ $? -eq 0 ]; then
        echo "Download completed successfully."
    else
        echo "Error: Download failed."
        exit 1
    fi
# Check if the first argument is "upload"
elif [ "$1" == "upload" ]; then
    # Upload files from local directory to Google Drive
    eval "rclone --drive-shared-with-me copy \"$LOCAL_DIR\" \"$REMOTE:$REMOTE_DIR\" --progress $EXCLUDE_PARAMS"
    # Check if the rclone command was successful
    if [ $? -eq 0 ]; then
        echo "Upload completed successfully."
    else
        echo "Error: Upload failed."
        exit 1
    fi
# If the argument is neither "download" nor "upload"
else
    echo "Error: Invalid argument. Use \"download\" or \"upload\"."
    print_usage
    exit 1
fi

# Print a completion message
echo "Done!"
