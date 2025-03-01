#!/bin/bash

print_usage() {
    echo "Usage: $0 <owner/repository>"
}

# Check if a repository is provided
if [ $# -ne 1 ]; then
    print_usage
    exit 1
fi

# Validate repository format
if [[ ! "$1" =~ ^[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+$ ]]; then
    echo "Error: Invalid repository format. Expected format: <owner/repository>"
    print_usage
    exit 1
fi

REPO=$1

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed"
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub CLI"
    exit 1
fi

# Get all releases and tags
echo "Fetching releases and tags from $REPO..."
releases=$(gh release list -R "$REPO")

if [ -z "$releases" ]; then
    echo "No releases found in repository $REPO"
    exit 0
fi

# Display releases with numbers
echo "Available releases:"
echo "==================="
echo "$releases" | nl -w3 -s') '
echo "==================="
echo "A) Delete all releases and tags"
echo "Q) Quit"
echo "Note: You can select multiple releases by separating numbers with spaces"

# Ask for user input
read -p "Enter number(s) of release to delete (or 'A' for all, 'Q' to quit): " choice

case $choice in
    [Aa])
        total=$(echo "$releases" | wc -l)
        current=0
        echo "Deleting all releases and tags..."
        while read -r line; do
            ((current++))
            tag=$(echo "$line" | awk '{print $(NF-1)}')
            echo "[$current/$total] Deleting release and tag: $tag"
            if gh release delete "$tag" -R "$REPO" --cleanup-tag -y; then
                echo "✓ Release and tag deleted successfully"
            else
                echo "✗ Failed to delete release and tag"
            fi
            echo "-------------------"
        done <<< "$releases"
        echo "Operation completed: All releases and tags have been processed."
        ;;
    [Qq])
        echo "Operation cancelled."
        exit 0
        ;;
    *)
        total_releases=$(echo "$releases" | wc -l)
        selected_count=$(echo "$choice" | wc -w)
        current=0
        for num in $choice; do
            ((current++))
            if [[ "$num" =~ ^[0-9]+$ ]] && [ "$num" -le "$total_releases" ]; then
                selected=$(echo "$releases" | sed -n "${num}p")
                tag=$(echo "$selected" | awk '{print $3}')
                echo "[$current/$selected_count] Deleting release and tag: $tag"
                if gh release delete "$tag" -R "$REPO" --cleanup-tag -y; then
                    echo "✓ Release and tag deleted successfully"
                else
                    echo "✗ Failed to delete release and tag"
                fi
                echo "-------------------"
            else
                echo "✗ Invalid number: $num (skipped)"
            fi
        done
        echo "Operation completed: Selected releases and tags have been processed."
        ;;
esac
