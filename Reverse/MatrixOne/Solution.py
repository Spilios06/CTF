#!/usr/bin/env python3

import numpy as np

def transform(s, l):
    table = np.zeros((l, l), dtype=np.uint8)
    for i in range(l*l):
        table[i // l, i % l] = s[i]
    return table

len = 6
def prepare(s):
    trans = transform(s, len)
    for i in range(len//2 + 1):
        for i2 in range(len - 2*i - 1):
            c = trans[i, i+i2]
            trans[i, i+i2] = trans[len - 1 - i - i2, i]
            trans[len - 1 - i - i2, i] = trans[len - 1 -i , len - 1 - i - i2]
            trans[len - 1 -i , len - 1 - i - i2] = trans[i+i2, len-1-i]
            trans[i+i2, len-1-i] = c
    return trans

print(prepare(list(range(36))))

encoded = b"oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2"

blk1 = encoded[:12]
l0 = [b^2 for b in reversed(blk1[::2])]
l5 = [b^2 for b in reversed(blk1[1::2])]

blk2 = encoded[12:24]
l1 = [b^1 for b in reversed(blk2[::2])]
l4 = [b^1 for b in reversed(blk2[1::2])]

blk3 = encoded[24:36]
l2 = list(reversed(blk3[::2]))
l3 = list(reversed(blk3[1::2]))

flag = 36*[0]
for i in range(6):
    flag[30 - 6*i] = l0[i]
    flag[31 - 6*i] = l1[i]
    flag[32 - 6*i] = l2[i]
    flag[33 - 6*i] = l3[i]
    flag[34 - 6*i] = l4[i]
    flag[35 - 6*i] = l5[i]
print(bytes(flag))