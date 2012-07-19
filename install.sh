#!/bin/bash

mkdir /usr/lib/craesy
mkdir /usr/lib/craesy/scripts
mkdir /usr/lib/craesy/bin
current_dir=$(pwd)
cp $current_dir/scripts/* /usr/lib/craesy/scripts
cp $current_dir/bin/* /usr/lib/craesy/bin

cd /usr/bin
ln -s /usr/lib/craesy/bin/craesy .

echo "Insallation done!"




