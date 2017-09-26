#!/bin/bash
cd zimbra/
for dir in `ls` 
do
	cd $PWD/$dir; make; cd ..
done
