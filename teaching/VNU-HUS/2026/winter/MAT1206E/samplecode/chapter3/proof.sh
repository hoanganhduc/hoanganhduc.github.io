#!/bin/bash

if [ $# == 1 ]
then
	eprover --proof-object $1 | epclextract
else
	# Show user guide
	echo -e "\e[1mUsage: bash $0 [name.lop] \e[0m"
	exit 1
fi
