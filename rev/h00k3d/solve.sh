#!/bin/bash
FOLDER=$(mktemp -d)
ORIGINAL=$(pwd)
gcc -shared -fPIC -D_GNU_SOURCE -o "${FOLDER}/solution.so" solution.c
cp ./h00k3d "${FOLDER}/"
cp ./libsimple_random.so "${FOLDER}/"
cd "${FOLDER}"
LD_PRELOAD=./solution.so ./h00k3d | grep -o -E '[pP][eE][cC][aA][nN]\{.+?\}'
cd "${ORIGINAL}"
