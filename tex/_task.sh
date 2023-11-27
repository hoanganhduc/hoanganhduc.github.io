#!/bin/bash

WORKDIR=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

function extract() {
	find "$WORKDIR/examples" -type d -exec bash -c "[ -f "{}/main.zip" ] && cd {} && unzip -o main.zip && echo \"{}/main.zip extracted\" && cd $WORKDIR" \;
}

function sync() {
	declare -a FILES=("ducha.sty" "Makefile" "make.bat" "latexmkrc" "vietex.sty")
	for f in ${FILES[@]}; do
		find examples -type f -name $f -exec bash -c "rsync -arv $f {}" \;
	done
}

function generate() {
	find "$WORKDIR/examples" -type d -exec bash -c "[ -f "{}/Makefile" ] && cd {} && latexmk -C && make && make clean && make archive && make clean-all && cd $WORKDIR" \;
}

"$@"
