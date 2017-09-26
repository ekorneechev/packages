#!/bin/bash
REPO_DIR="/var/ftp/local"
REPO_NAME="zimbra-foss"

sudo find . -name "*64.rpm" -exec cp {} $REPO_DIR/x86_64/RPMS.$REPO_NAME/ \;

sudo rm -rf $REPO_DIR/x86_64/RPMS.$REPO_NAME/*debuginfo*

for ARCH in x86_64-i586 x86_64 noarch; do
    sudo genbasedir --bloat --progress --topdir=$REPO_DIR $ARCH $REPO_NAME
done

sudo apt-get update

