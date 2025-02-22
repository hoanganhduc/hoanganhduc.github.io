#!/bin/bash

# Function to print usage information
print_usage() {
  echo "Usage: $0 <owner/repo>"
  echo "Example: $0 username/repository"
  exit 1
}

# Function to delete a specific workflow run
delete_workflow_run() {
  local repo="$1"
  local run_id="$2"

  echo "Deleting workflow run with ID $run_id..."
  if gh api --silent repos/$repo/actions/runs/$run_id -X DELETE; then
    echo "Deleted workflow run with ID $run_id."
  else
    echo "Failed to delete workflow run with ID $run_id."
  fi
}

# Function to list and delete workflow runs
manage_workflow_runs() {
  local repo="$1"

  echo "Fetching all workflow runs for repository $repo..."

  # Fetch all workflow runs and store in a temporary file
  local temp_file
  temp_file=$(mktemp)
  
  # Updated query to include more information about the workflow run
  gh api repos/$repo/actions/runs --paginate -q '.workflow_runs[] | "\(.id)\t\(.name)\t\(.created_at)\t\(.status)"' > "$temp_file"

  if [ ! -s "$temp_file" ]; then
    echo "No workflow runs found."
    rm "$temp_file"
    return
  fi

  # Display workflow runs with formatting
  echo "Found workflow runs:"
  local i=1
  while IFS=$'\t' read -r id name created status; do
    printf "%d. [ID: %s] %s (Created: %s, Status: %s)\n" "$i" "$id" "$name" "$created" "$status"
    i=$((i + 1))
  done < "$temp_file"

  # Ask user which workflow run(s) to delete
  echo "Enter the number(s) of the workflow run(s) to delete"
  read -p "(comma-separated, 'all' to delete all, or 'q' to quit): " choice

  if [[ "$choice" == "q" ]]; then
    echo "Operation cancelled."
    rm "$temp_file"
    return
  elif [[ "$choice" == "all" ]]; then
    # Delete all workflow runs
    while IFS=$'\t' read -r id _ _ _; do
      delete_workflow_run "$repo" "$id"
    done < "$temp_file"
  else
    # Convert comma-separated string to array and sort unique values
    IFS=',' read -ra choices <<< "$choice"
    # Use associative array to track processed numbers
    declare -A processed
    local total_lines=$(wc -l < "$temp_file")

    for num in "${choices[@]}"; do
      if [[ "$num" =~ ^[0-9]+$ ]]; then
        # Check if number is within valid range and hasn't been processed
        if [ "$num" -gt 0 ] && [ "$num" -le "$total_lines" ] && [ -z "${processed[$num]}" ]; then
          selected_run=$(sed "${num}q;d" "$temp_file")
          run_id=$(echo "$selected_run" | cut -f1)
          delete_workflow_run "$repo" "$run_id"
          processed[$num]=1
        elif [ -n "${processed[$num]}" ]; then
          echo "Skipping duplicate selection: $num"
        else
          echo "Invalid selection: $num (must be between 1 and $total_lines)"
        fi
      else
        echo "Invalid input: $num (not a number)"
      fi
    done
  fi

  # Clean up
  rm "$temp_file"
  echo "Operation completed."
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
if [ "$#" -ne 1 ]; then
  print_usage
fi

repo="$1"

# Verify that repo is not empty and has the correct format
if [[ ! "$repo" =~ ^[^/]+/[^/]+$ ]]; then
  echo "Error: Repository must be in the format 'owner/repo'"
  print_usage
fi

# Call the function to manage workflow runs
manage_workflow_runs "$repo"
