#!/bin/bash

# Function to print usage information
usage() {
    echo "Usage: $0 [-r <repository>] [-b <branch>]"
    echo "Example: $0 -r owner/repo -b quiz"
    exit 1
}

echo "Checking if GitHub CLI is installed..."
# Ensure GitHub CLI is installed
if ! command -v gh &> /dev/null
then
    echo "GitHub CLI (gh) could not be found. Please install it first."
    exit 1
fi

# Default values
repository=""
branch=""

echo "Parsing command line arguments..."
# Parse command line arguments
while getopts ":r:b:" opt; do
    case ${opt} in
        r )
            repository=$OPTARG
            ;;
        b )
            branch=$OPTARG
            ;;
        \? )
            usage
            ;;
    esac
done

echo "Determining the repository..."
# Get the current repository if not provided
if [ -z "$repository" ]; then
    repository=$(gh repo view --json nameWithOwner --jq '.nameWithOwner')
    if [ -z "$repository" ]; then
        echo "Failed to determine the current repository."
        usage
        exit 1
    fi
fi

echo "Repository: $repository"

echo "Determining the branch..."
# Get the current branch if not provided
if [ -z "$branch" ]; then
    branch=$(git rev-parse --abbrev-ref HEAD)
fi

echo "Branch: $branch"

echo "Listing all workflow runs for the specified branch and repository..."
# List all workflow runs for the specified branch and repository
if [ -n "$branch" ]; then
    workflow_runs=$(gh run list --repo "$repository" --branch "$branch" --limit 100 --json databaseId,createdAt,headBranch,workflowName,status,conclusion --jq '.[] | "\(.databaseId) \(.createdAt) \(.headBranch) \(.workflowName) \(.status) \(.conclusion)"')
else
    workflow_runs=$(gh run list --repo "$repository" --limit 100 --json databaseId,createdAt,headBranch,workflowName,status,conclusion --jq '.[] | "\(.databaseId) \(.createdAt) \(.headBranch) \(.workflowName) \(.status) \(.conclusion)"')
fi

if [ -z "$workflow_runs" ]; then
    echo "No workflow runs found for the $branch branch in the $repository repository."
    exit 1
fi

echo "Workflow runs for repository '$repository':"
echo "$workflow_runs" | nl | while read -r line; do
    run_id=$(echo "$line" | awk '{print $2}')
    created_at=$(echo "$line" | awk '{print $3}')
    head_branch=$(echo "$line" | awk '{print $4}')
    workflow_name=$(echo "$line" | awk '{for (i=5; i<=NF-3; i++) printf $i " "; print ""}')
    status=$(echo "$line" | awk '{print $(NF-2)}')
    conclusion=$(echo "$line" | awk '{print $(NF)}')
    
    # Colorize output
    case "$status" in
        "completed")
            status_color="\033[0;32m" # Green
            ;;
        "in_progress")
            status_color="\033[0;33m" # Yellow
            ;;
        "queued")
            status_color="\033[0;34m" # Blue
            ;;
        *)
            status_color="\033[0m" # Default
            ;;
    esac

    case "$conclusion" in
        "success")
            conclusion_color="\033[0;32m" # Green
            ;;
        "failure")
            conclusion_color="\033[0;31m" # Red
            ;;
        "cancelled")
            conclusion_color="\033[0;33m" # Yellow
            ;;
        *)
            conclusion_color="\033[0m" # Default
            ;;
    esac

    echo -e "\033[1;36m${line%% *}\033[0m \033[1;35m$run_id\033[0m \033[1;34m$created_at\033[0m \033[1;33m$head_branch\033[0m \033[1;32m$workflow_name\033[0m ${status_color}$status\033[0m ${conclusion_color}$conclusion\033[0m"
done

# Ask the user which workflow they want to re-run
read -p "Enter the number of the workflow you want to re-run (or 'q' to quit): " workflow_number

# Check if the user wants to quit
if [[ "$workflow_number" == "q" || "$workflow_number" == "Q" ]]; then
    echo "Quitting..."
    exit 0
fi

# Get the selected workflow run ID
selected_run_id=$(echo "$workflow_runs" | sed -n "${workflow_number}p" | awk '{print $1}')

if [ -z "$selected_run_id" ]; then
    echo "Invalid selection."
    exit 1
fi

# Ask for confirmation before re-running the workflow
read -p "Are you sure you want to re-run the selected workflow run ID '$selected_run_id'? (y/n): " confirm
if [[ $confirm != [yY] ]]; then
    echo "Re-run cancelled."
    exit 0
fi

echo "Triggering re-run for workflow run ID: $selected_run_id..."
# Re-run the selected workflow
gh run rerun "$selected_run_id" --repo "$repository"

echo "Re-run triggered for workflow run ID: $selected_run_id"