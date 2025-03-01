#!/bin/bash

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed"
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check if argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 owner/repo [download_path]"
    echo "If download_path is not specified, files will be saved to the default downloads folder"
    echo "Example: $0 microsoft/vscode /path/to/download"
    exit 1
fi

# Validate input format (should be owner/repo)
if ! [[ $1 =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then
    echo "Error: Invalid repository format. Please use 'owner/repo' format"
    exit 1
fi

repo=$1

releases=$(gh release list -R "$repo" 2>/dev/null)

if [ -z "$releases" ]; then
    echo "No releases found for $repo"
    exit 1
fi

echo "Available releases:"
echo "$releases" | nl

total_releases=$(echo "$releases" | wc -l)
echo -n "Select release numbers to download (1-$total_releases, space-separated): "
read -r selections

for selection in $selections; do
    if ! [[ "$selection" =~ ^[0-9]+$ ]] || [ "$selection" -lt 1 ] || [ "$selection" -gt "$total_releases" ]; then
        echo "Invalid selection: $selection"
        continue
    fi
    
    release_tag=$(echo "$releases" | sed -n "${selection}p" | awk '{print $(NF-1)}')
    download_path=${2:-"$HOME/Downloads/${repo//\//-}-$release_tag"}

    # Check if specified directory exists, if not create it
    if [ ! -d "$download_path" ]; then
        echo "Creating directory: $download_path"
        mkdir -p "$download_path"
    fi

    echo "Downloading release $release_tag to $download_path..."
    gh release download "$release_tag" -R "$repo" -D "$download_path"
done