#!/bin/bash

for file in `find * -name "*64.rpm"`
do
	dir=${file%%/*}
	touch $dir/BUILD.OK
	echo $dir
done

find . -name BUILD.OK | wc -l
echo 'Need:'
ls | grep -v "check_build.sh" | wc -l
