#!/bin/bash

EXTDIR="/usr/lib/firefox-addons/extensions"
TMPDIR="/tmp/ext"
clobber=false

USG="	${0##*/} [-f] XPI_FILE_TO_INSTALL

	# Source: http://ubuntuforums.org/showthread.php?t=1485995
	Installs the xpi file to /usr/lib/firefox-addons/extensions which
	will enable the installation next time the firefox starts.

	-f Overwrite existing extensions - may be useful for upgrading."

setUp(){
	umask 0022
	mkdir -p "$TMPDIR"
	echo 'Working...'
	unzip "$1" -d "$TMPDIR" &> /dev/null
}

getID(){
	local IFS="
"
	FILE="`cat "$TMPDIR/install.rdf"`"; GET=; ID=
	for i in $FILE; do
		if echo "$i" | grep "urn:mozilla:install-manifest" > /dev/null; then
			GET=true
			continue
		fi
		if [ "$GET" = true ]; then
			if echo "$i" | grep "<em:id>" > /dev/null; then ID=`echo "$i" | sed 's#.*<em:id>\(.*\)</em:id>.*#\1#'`
			elif echo "$i" | grep "em:id=\"" > /dev/null; then ID=`echo "$i" | sed 's/.*em:id="\(.*\)".*/\1/'`; fi

			[ -n "$ID" ] && return
		fi
	done
	echo "ERROR: Error parsing file: \"$FILE\"" && return 1
}

installExtention(){
	[ "$clobber" = true ] && [ -d "$EXTDIR/$ID" ] && rm -rf "$EXTDIR/$ID"
	[ -d "$EXTDIR/$ID" ] && echo "SKIP: Extension already installed: \"$EXTDIR/$ID\"" && return 1
	mv "$TMPDIR" "$EXTDIR/$ID"
}

cleanUp(){
	[ $? = 0 ] && echo "Extension installed: \"$1\"" || echo "ERROR: Failed to install extension: \"$1\""
	[ -d "$TMPDIR" ] && rm -rf "$TMPDIR"
}

[ $# -lt 1 ] && echo "$USG" && exit
[ ! -w /etc/passwd ] && echo "Need root. Exiting!" && exit
[ -d "$TMPDIR" ] && echo "ERROR: Temporary folder already exists: \"$TMPDIR\"" && exit
[ "$1" = -f ] && clobber='true' && shift

warning='Please exit Firefox before continuing: (k=kill)'
while [ 1 ]; do
	psff=`ps --no-headers -o user,pid,cmd -C firefox-bin`
	[ ! "$psff" ] && break
	[ "$warning" ] && echo "$warning"; warning=
	echo -n "$psff: "
	read killff
	[ "$killff" = k ] && killall -i firefox-bin
	sleep 2
done

for each in $@; do
	trap "cleanUp 1 \"$each\"" 1 2 3 15
	[ ! -f "$each" ] && echo "ERROR: File doesn't exist: \"$each\"" && continue
	setUp "$each"
	[ $? = 0 ] && getID
	[ $? = 0 ] && installExtention
	cleanUp "$each"
done
