#!/bin/bash
echo 'definitely_secure_password12345!!!' | ./authenticate2 | grep -o -E '[pP][eE][cC][aA][nN]\{.+?\}'
