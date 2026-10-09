#!/bin/bash

set -e

rm -f build/*

#Assembled everything up to line 779 without -m4
#sh4-linux-gnu-gcc -mb -c -o build/test.o src/test.S

#Assembled everything up to line 895 with only -m4
#sh4-linux-gnu-gcc -mb -m4 -c -o build/test.o src/test.S

sh4-linux-gnu-gcc -mb -m4a -c -o build/test.o src/test.S

sh4-linux-gnu-objcopy -O binary build/test.o build/test.bin
