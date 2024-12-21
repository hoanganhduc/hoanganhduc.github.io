#!/bin/bash

# Last updated: 2024-12-21

# Define color codes for output formatting
CYAN='\033[0;36m'
NC='\033[0m'
# Get the current directory containing the script
CURRENT_DIR="$(cd "$(dirname "$0")" && pwd)" 

GITHUB_USERNAME="hoanganhduc"

# Check the first argument to determine the operation mode
if [ "$1" == "clone" ]; then
	# Set variables for cloning a GitHub repository and Overleaf project
	GITHUB_REPO_ID="$2"
	OVERLEAF_PROJECT_ID="$3"
	WORKDIR="$CURRENT_DIR/$GITHUB_REPO_ID"
fi

if [ "$1" == "github" ]; then
	# Set variables for cloning a GitHub repository
	GITHUB_REPO_ID="$2"
	WORKDIR="$CURRENT_DIR/$GITHUB_REPO_ID"
fi

if [ "$1" == "overleaf" ]; then
	# Set variables for cloning an Overleaf project
	OVERLEAF_PROJECT_ID="$2"
	WORKDIR="$CURRENT_DIR/$OVERLEAF_PROJECT_ID"
fi

if [ "$1" == "makefile" ]; then
	# Set variables for running a Makefile
	WORKDIR="$CURRENT_DIR"
	if [ "$2" ]; then
		MAKEFILE_OPTION="$2"
	fi
fi

if [ "$1" == "initiate" ]; then
	# Set variables for initiating a new project
	GITHUB_REPO_ID="$2"
	OVERLEAF_PROJECT_ID="$3"
	WORKDIR="$CURRENT_DIR/$GITHUB_REPO_ID"
fi

# Define URLs for GitHub and Overleaf repositories
GITHUB_REPO_URL="git@github.com:$GITHUB_USERNAME/$GITHUB_REPO_ID.git"
OVERLEAF_PROJECT_URL="https://git@git.overleaf.com/$OVERLEAF_PROJECT_ID"

# Define the contents of the .git/config file
GIT_CONFIG_FILE_CONTENTS=$(cat <<EOF
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = $GITHUB_REPO_URL
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
[remote "overleaf"]
	url = $OVERLEAF_PROJECT_URL
	fetch = +refs/heads/*:refs/remotes/overleaf/*
	pushurl = $OVERLEAF_PROJECT_URL
[branch "overleaf"]
	remote = overleaf
	merge = refs/heads/master
EOF
)

# Fetch contents for exclude.txt, .gitignore, and .devcontainer/devcontainer.json from URLs
EXCLUDE_FILE_URL="https://hoanganhduc.github.io/tex/exclude.txt"
EXCLUDE_FILE_CONTENT=$(curl -s $EXCLUDE_FILE_URL)
GITIGNORE_FILE_URL="https://hoanganhduc.github.io/tex/gitignore"
GITIGNORE_FILE_CONTENT=$(curl -s $GITIGNORE_FILE_URL)
DEVCONTAINER_FILE_URL="https://hoanganhduc.github.io/tex/devcontainer.json"
DEVCONTAINER_FILE_CONTENT=$(curl -s $DEVCONTAINER_FILE_URL)

# List of files to delete during the merge process
DELETE_FILES=("Makefile" "make.bat" "exclude.txt" ".devcontainer" "README*")

# Function to print usage instructions
print_usage() {
	echo "Usage: $0 {clone|github|overleaf|makefile|initiate} [options]"
	echo "Commands:"
	echo "  clone <github_repo_id> <overleaf_project_id>  Clone both GitHub and Overleaf repositories"
	echo "  github <github_repo_id>                      Clone only GitHub repository"
	echo "  overleaf <overleaf_project_id>               Clone only Overleaf repository"
	echo "  makefile [makefile_option]                   Run Makefile in subdirectories"
	echo "  initiate <github_repo_id> <overleaf_project_id> Initiate a new project with GitHub and Overleaf"
}

# Prompt the user to rename the working directory
rename_workdir() {
	echo -e "${CYAN}Do you want to rename the '$WORDIR' directory? If not, press enter. Otherwise, type a new name:${NC}"
	read NEW_WORKDIR_NAME
	if [ -n "$NEW_WORKDIR_NAME" ]; then
		WORKDIR="$CURRENT_DIR/$NEW_WORKDIR_NAME"
		echo -e "${CYAN}Renaming working directory to $WORKDIR${NC}"
		mv "$CURRENT_DIR/$OVERLEAF_PROJECT_ID" "$WORKDIR"
	fi
}

# Function to clone a GitHub repository with/without an overleaf branch
clone_repo() {
	if [ -d "$WORKDIR/.git" ]; then
		echo -e "${CYAN}Repository already cloned.${NC}"
	else
		if [ -n "$GITHUB_REPO_ID" ]; then
			if [ -n "$OVERLEAF_PROJECT_ID" ]; then
				echo -e "${CYAN}Cloning GitHub repository $GITHUB_REPO_ID and Overleaf project $OVERLEAF_PROJECT_ID${NC}"
			else
				echo -e "${CYAN}Cloning GitHub repository $GITHUB_REPO_ID${NC}"
			fi
			echo -e "${CYAN}Creating working directory $WORKDIR${NC}"
			mkdir -p "$WORKDIR"
			cd "$WORKDIR"
			echo -e "${CYAN}Initializing Git repository${NC}"
			git init
			echo -e "${CYAN}Adding remote origin $GITHUB_REPO_URL${NC}"
			git remote add origin "$GITHUB_REPO_URL"
			echo -e "${CYAN}Fetching all branches${NC}"
			git fetch --all
			echo -e "${CYAN}Tracking remote branches${NC}"
			git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
			if [ -n "$OVERLEAF_PROJECT_ID" ]; then
				echo -e "${CYAN}Configuring Git for Overleaf${NC}"
				echo "$GIT_CONFIG_FILE_CONTENTS" > .git/config
			fi
			echo -e "${CYAN}Pulling all branches${NC}"
			git pull --all
			echo -e "${CYAN}Checking out master branch${NC}"
			git checkout master
			cd ..
			rename_workdir
		else
			if [ -n "$OVERLEAF_PROJECT_ID" ]; then
				echo -e "${CYAN}Cloning Overleaf project $OVERLEAF_PROJECT_ID${NC}"
				git clone "$OVERLEAF_PROJECT_URL" "$WORKDIR"
				rename_workdir
			else
				print_usage
				exit 1
			fi
		fi
	fi
}

# Function to run Makefile in the specified directory
run_makefile() {
	find $WORKDIR -type f -name "Makefile" | while read dir; do name="$(dirname "$dir")" && echo -e "${CYAN}Updating \"$name\"${NC}" && cd "$name" && echo $CURRENT_DIR && if [ "$MAKEFILE_OPTION" ]; then make $MAKEFILE_OPTION; else make; fi; done
}

# Function to merge the master branch onto the overleaf branch
merge_master_to_overleaf() {
	echo -e "${CYAN}Merge 'master' branch onto 'overleaf'${NC}"
	git checkout overleaf
	git merge --no-commit --no-ff --allow-unrelated-histories master
	for file in "${DELETE_FILES[@]}"; do
		if [ -e "$file" ]; then
			echo -e "${CYAN}Deleting $file${NC}"
			git rm -rf "$file"
			echo -e "${CYAN}Deleted $file${NC}"
		fi
	done
	echo -e "${CYAN}Adding all changes${NC}"
	git add --all .
	echo -e "${CYAN}Committing merge${NC}"
	git commit -S -m "Merge master onto overleaf $(date +'%Y-%m-%d  %H:%M:%S %Z')"
	echo -e "${CYAN}Pushing to origin overleaf${NC}"
	git push -u origin overleaf
	echo -e "${CYAN}Pushing to overleaf master${NC}"
	git push -u overleaf overleaf:master
	echo -e "${CYAN}Checking out master branch${NC}"
	git checkout master
}

# Function to merge the overleaf branch onto the master branch
merge_overleaf_to_master() {
	echo -e "${CYAN}Pulling all branches${NC}"
	git pull --all
	echo -e "${CYAN}Checking out overleaf branch${NC}"
	git checkout overleaf
	echo -e "${CYAN}Merge 'overleaf' branch onto 'master'${NC}"
	git checkout master
	echo -e "${CYAN}Merging overleaf into master${NC}"
	git merge --no-commit --no-ff --allow-unrelated-histories overleaf
	echo -e "${CYAN}Committing merge${NC}"
	git commit -S -m "Merge overleaf onto master $(date +'%Y-%m-%d  %H:%M:%S %Z')"
	echo -e "${CYAN}Pushing to origin master${NC}"
	git push -u origin master
}

# Function to initiate a new project
initiate() {
	if [ ! -d "$WORKDIR" ]; then
		echo -e "${CYAN}Please create a directory named $WORKDIR and put your LaTeX contents here${NC}"
		exit 1
	fi

	if [ -d "$WORKDIR/.git" ]; then
		echo -e "${CYAN}Repository already cloned${NC}"
		exit 1
	fi

	echo -e "${CYAN}Initiating the repository '$WORKDIR'${NC}"
	cd "$WORKDIR"
	echo -e "${CYAN}Creating exclude.txt${NC}"
	echo "$EXCLUDE_FILE_CONTENT" > exclude.txt
	echo -e "${CYAN}Creating .gitignore${NC}"
	echo "$GITIGNORE_FILE_CONTENT" > .gitignore
	if [ ! -d ".devcontainer" ]; then
		echo -e "${CYAN}Creating '.devcontainer' directory${NC}"
		mkdir -p ".devcontainer"
		echo -e "${CYAN}Creating './devcontainer/devcontainer.json'${NC}"
		echo "$DEVCONTAINER_FILE_CONTENT" > .devcontainer/devcontainer.json
	fi
	echo -e "${CYAN}Initializing Git repository${NC}"
	git init
	echo -e "${CYAN}Adding remote origin${NC}"
	git remote add origin "$GITHUB_REPO_URL"
	echo -e "${CYAN}Adding all files to Git${NC}"
	git add --all .
	echo -e "${CYAN}Committing changes${NC}"
	git commit -S -m "first commit $(date +'%Y-%m-%d  %H:%M:%S %Z')"
	echo -e "${CYAN}Pushing to origin master${NC}"
	git push -u origin master
	echo -e "${CYAN}Creating orphan branch overleaf${NC}"
	git checkout --orphan overleaf
	echo -e "${CYAN}Removing all files from orphan branch${NC}"
	git rm -rf .
	echo -e "${CYAN}Adding remote overleaf${NC}"
	git remote add overleaf $OVERLEAF_PROJECT_URL
	echo -e "${CYAN}Pulling from overleaf master${NC}"
	git pull overleaf master --allow-unrelated-histories
	echo -e "${CYAN}Configuring Git for Overleaf${NC}"
	echo "$GIT_CONFIG_FILE_CONTENTS" > .git/config
	merge_master_to_overleaf
}

# Main function to handle script arguments and call appropriate functions
main() {
	case "$1" in
		clone|github|overleaf)
			clone_repo
			;;
		makefile)
			run_makefile
			;;
		initiate)
			initiate
			;;
		*)
			print_usage
			exit 1
			;;
	esac
}

# Call the main function with all script arguments
main "$@"