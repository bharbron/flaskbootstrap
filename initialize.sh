#!/bin/bash

if [ $# -eq 0 ]
	then
		echo "Usage: initialize.sh NEWPROJECTNAME"
		exit 1
fi

sed -i '' 's/PROJECTNAME_SECRET_KEY/'`echo $1 | awk '{print toupper($0)}'`'_SECRET_KEY/g' PROJECTNAME/config.py
find PROJECTNAME/ -type f -exec sed -i '' 's/PROJECTNAME/'$1'/g' {} +
sed -i '' 's/PROJECTNAME/'$1'/g' manage.py
mv PROJECTNAME $1

virtualenv --no-site-packages env

exit 0