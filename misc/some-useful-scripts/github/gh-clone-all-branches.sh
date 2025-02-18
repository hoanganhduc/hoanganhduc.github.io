#!/bin/bash

# Verify that at least one argument is provided and valid.
if [ "$#" -lt 1 ]; then
    echo "Usage: $(basename "$0") <github_repo_id> [folder]"
    exit 1
fi

REPO_ID="$1"

# Validate REPO_ID format: should be "user/repo"
if [[ ! "$REPO_ID" =~ ^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$ ]]; then
    echo "Invalid repository identifier."
    echo "Usage: $(basename "$0") <github_repo_id> [folder]"
    exit 1
fi

# Use the part after the slash as folder name if not specified.
TARGET="${2:-${REPO_ID#*/}}"

# Define SSH and HTTPS URLs.
SSH_URL="git@github.com:${REPO_ID}.git"
HTTPS_URL="https://github.com/${REPO_ID}.git"

# Attempt clone using SSH first.
echo "Cloning via SSH: $SSH_URL into $TARGET..."
if ! git clone "$SSH_URL" "$TARGET"; then
    echo "SSH clone failed, trying HTTPS: $HTTPS_URL..."
    if ! git clone "$HTTPS_URL" "$TARGET"; then
        echo "Clone failed using both SSH and HTTPS."
        exit 1
    fi
fi

cd "$TARGET" || exit 1

echo "Setting up local tracking branches for all remote branches..."
for remote in $(git branch -r | grep -v HEAD); do
    branch=${remote#origin/}
    # Skip if the branch already exists.
    if ! git show-ref --verify --quiet "refs/heads/$branch"; then
        git branch --track "$branch" "$remote"
    fi
done

git fetch --all
echo "Done."