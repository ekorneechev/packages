#!/bin/bash

for file in `find perl-* -name "*64.rpm"`
do
	dir=${file%%/*}
	touch $dir/BUILD.OK
done

find . -name BUILD.OK | wc -l
echo 'Need:'
ls | grep ^perl | wc -l
