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

mkdir vagrant
cd vagrant
curl http://www.pgdevbox.com/Vagrantfile -o Vagrantfile
vagrant up
vagrant ssh -- -t createdb $1

echo "Now run the following to start the project:"
echo "source env/bin/activate"
echo "pip install -r requirements.txt"
echo `echo $1 | awk '{print toupper($0)}'`"_SECRET_KEY=foobar python manage.py run"

exit 0