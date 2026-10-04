#!/usr/bin/env python3

data=bytes()
for i in range(2**16):
    data+=bytes([i>>8,i&0xFF])

with open("all.bin","wb") as f:
    f.write(data)
