#!/bin/bash
cd zimbra/
for dir in `ls | grep -v ".sh"`
do
    if [ ! -f "$dir/BUILD.OK" ]; then
        echo "-----------------------------START-----------------------------"
	echo $dir
	echo
	cd $PWD/$dir; make; cd ..
	echo "-----------------------------FINISH----------------------------"
	echo
	echo
	echo
    fi
done
