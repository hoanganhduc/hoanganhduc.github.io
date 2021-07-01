#!/bin/bash

WORKDIR=./x86_64

cd $WORKDIR

for package in {*.pkg.tar.zst,*.pkg.tar.xz} ; do
	if [ -f "$package" ]; then
		if  [ ! -f "$package.sig" ]; then
			gpg --local-user 0xD4E51506 --detach-sign $package;
		# else
			# repo-add -n hoanganhduc.db.tar.gz $package;
		fi
	fi
done

repo-add -n hoanganhduc.db.tar.gz *.pkg.tar.xz *.pkg.tar.zst
