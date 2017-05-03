#!/usr/bin/env python3
#
# Solve a crackme using instruction counting. Works if the flag is
# checked byte for byte.
#
# Requires pin and the pintools from the ManualExamples folder.
#

import sys
import os

def run(data):
    with open('input', 'wb') as f:
        f.write(bytes(data))
    os.system("../../../../pin -t inscount0.so -- ~/crackme < input > /dev/null")
    with open('inscount.out', 'r') as f:
        # TODO pintool needs to be modified for this to work
        return int(f.read())

flag = [0x00] * 80
for i in range(len(flag)):
    basecount = run(flag)
    for b in range(0x20, 0x80):
        flag[i] = b
        if run(flag) > basecount:
            print("flag[{}] = {}".format(i, chr(b)))
            break
    else:
        print("Failed")
        sys.exit(-1)

print(bytes(flag))
