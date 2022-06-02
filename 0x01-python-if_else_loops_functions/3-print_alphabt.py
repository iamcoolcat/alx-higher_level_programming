#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if chr(i) not in "eq":
        print("{:c}".format(i), end='')
