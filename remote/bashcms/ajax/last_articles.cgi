#!/bin/bash -xv
dir=$(dirname $0)/../pages

echo "Content-Type: text/html"
echo
ls -f $dir |
grep -E "^[0-9]{14}_" |
sort -r
