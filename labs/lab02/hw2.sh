#!/usr/bin/bash
cd ~
x=$(find . -not -path '*/.*' -type f | wc -l)
touch info.txt
echo "Hello, $USER" >> info.txt
echo -n "time: " >> info.txt
date >> info.txt
echo "os: $OSTYPE" >> info.txt
echo -n "home directory size: " >> info.txt
du -sh --apparent-size | awk '{print $1}' >> info.txt
echo -n "free space on disk: " >> info.txt
df . -h | tail -1 | awk '{print $4}' >> info.txt
echo -n "num folders: " >> info.txt
ls -l | grep ^d | wc -l >> info.txt
echo -n "num files: $x" >> info.txt
echo $'\n' >> info.txt
