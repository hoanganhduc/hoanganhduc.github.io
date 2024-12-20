#!/bin/bash

# Set the working directory to the directory of the script
WORKDIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

# Function to extract main.zip files in the examples directory
function extract() {
	# Find directories in the examples directory and execute the following commands
	find "$WORKDIR/examples" -type d -exec bash -c "[ -f "{}/main.zip" ] && cd {} && unzip -o main.zip && echo \"{}/main.zip extracted\" && cd $WORKDIR" \;
}

# Function to synchronize specific files to the examples directory
function sync() {
	# Declare an array of filenames to be synchronized
	declare -a FILES=("ducha.sty" "Makefile" "make.bat" "latexmkrc" "vietex.sty")
	# Loop through each file in the array
	for f in ${FILES[@]}; do
		# Find files with the same name in the examples directory and synchronize them
		find examples -type f -name $f -exec bash -c "rsync -arv $f {}" \;
	done
}

# Function to generate output using Makefile in the examples directory
function generate() {
	# Find directories in the examples directory and execute the following commands
	find "$WORKDIR/examples" -type d -exec bash -c "[ -f "{}/Makefile" ] && cd {} && latexmk -C && make && make clean && make archive && make clean-all && cd $WORKDIR" \;
}

# Execute the function passed as an argument to the script
"$@"
