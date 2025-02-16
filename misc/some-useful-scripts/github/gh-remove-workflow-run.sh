#!/bin/bash

# Function to print usage information
print_usage() {
  echo "Usage: $0 <user> <repo>"
  exit 1
}

# Function to delete workflow runs
delete_workflow_runs() {
  local user="$1"
  local repo="$2"

  echo "Fetching all workflow runs for repository $user/$repo..."

  # Fetch all workflow runs and store in a temporary file
  local temp_file
  temp_file=$(mktemp)
  gh api repos/$user/$repo/actions/runs --paginate -q '.workflow_runs[] | "\(.id)"' > "$temp_file"

  if [ ! -s "$temp_file" ]; then
    echo "No workflow runs found to delete."
    rm "$temp_file"
    return
  fi

  local runs
  runs=$(cat "$temp_file")
  echo "Found workflow runs to delete: $runs"

  # Confirm before deleting
  read -p "Are you sure you want to delete all these workflow runs? (y/N): " confirm
  if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Aborted."
    rm "$temp_file"
    return
  fi

  # Delete each workflow run
  while IFS= read -r run_id; do
    echo "Deleting workflow run with ID $run_id..."
    if gh api --silent repos/$user/$repo/actions/runs/$run_id -X DELETE; then
      echo "Deleted workflow run with ID $run_id."
    else
      echo "Failed to delete workflow run with ID $run_id."
    fi
  done < "$temp_file"

  # Clean up
  rm "$temp_file"
  echo "All workflow runs have been deleted."
}

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
  echo "GitHub CLI (gh) is not installed. Please install it and try again."
  exit 1
fi

# Check if GitHub CLI is authorized
if ! gh auth status &> /dev/null; then
  echo "GitHub CLI is not authorized. Please run 'gh auth login' to authorize."
  exit 1
fi

# Verify the number of arguments
if [ "$#" -ne 2 ]; then
  print_usage
fi

user="$1"
repo="$2"

# Verify that user and repo are not empty
if [ -z "$user" ] || [ -z "$repo" ]; then
  print_usage
fi

# Call the function to delete workflow runs
delete_workflow_runs "$user" "$repo"