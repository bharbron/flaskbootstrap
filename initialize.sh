#!/bin/bash

if [ $# -eq 0 ]
	then
		echo "Usage: initialize.sh NEWPROJECTNAME"
		exit 1
fi

find PROJECTNAME/ -type f -exec sed -i '' 's/PROJECTNAME/$1/g' {} +
sed -i '' 's/PROJECTNAME/$1/g' manage.py
mv PROJECTNAME $1

exit 0