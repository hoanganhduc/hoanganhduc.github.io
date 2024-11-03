# This script provides two functions: backup and restore.
# It is used to backup and restore file timestamps (creation time, modification time, and access time) in the current directory.
#
# Usage:
#   ./timestamp.sh backup   # To create a backup of the timestamps
#   ./timestamp.sh restore  # To restore the timestamps from the backup
#
# Functions:
#   backup:
#     - Finds all files in the current directory, excluding those with names matching ".timestamps".
#     - Collects the creation time, modification time, and access time of each file.
#     - Saves this information in a file named ".timestamps.new".
#     - Compares the new timestamps file with the existing ".timestamps" file.
#     - If there are no changes, it removes the ".timestamps.new" file.
#     - If there are changes, it replaces the old ".timestamps" file with the new one.
#
#   restore:
#     - Reads the ".timestamps" file.
#     - Restores the modification time and access time of each file listed in the ".timestamps" file.
#
# Note:
#   - Ensure you have the necessary permissions to read and modify the files in the directory.
#   - The script uses Perl for processing file timestamps.
#!/bin/bash

function backup () {
	find ./ -mount ! -name ".timestamps" -print0 | perl -ne 'INIT{ $/ = "\0"; use File::stat;} chomp; my $s = stat($_); next unless $s; print $s->ctime . "/" . $s->mtime . "/" . $s->atime ."/$_\0"; ' > .timestamps.new
	if cmp --silent -- .timestamps .timestamps.new; then rm -rf .timestamps.new; else mv .timestamps.new .timestamps; fi
}

function restore () {
	cat .timestamps |  perl -ne 'INIT{ $/ = "\0";} chomp; m!^([0-9]+)/([0-9]+)/([0-9]+)/(.*)!s or next; my ($ct, $mt, $at, $f) = ($1, $2, $3, $4); utime $at, $mt, $f;'
}

"$@"