#!/bin/bash
strings ./authenticate | grep -o -E '[pP][eE][cC][aA][nN]\{.+?\}'
