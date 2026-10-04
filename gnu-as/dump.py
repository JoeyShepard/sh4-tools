#!/usr/bin/env python3

with open("build/test.bin","rb") as f:
    data=f.read()

for i in range(0,len(data),2):
    for j in range(2):
        byte=hex(data[i+j]).upper()[2:]
        byte=("00"+byte)[-2:]
        print(byte,end="")
    print()

