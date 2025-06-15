#!/usr/bin/env python3

encoded = b"oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2"

def decrypt_block(block, xor_key):
    """Decrypt a block by reversing and applying XOR."""
    half1 = [b ^ xor_key for b in reversed(block[::2])]
    half2 = [b ^ xor_key for b in reversed(block[1::2])]
    return half1, half2

blk1 = encoded[:12]
blk2 = encoded[12:24]
blk3 = encoded[24:36]

l0, l5 = decrypt_block(blk1, 2)
l1, l4 = decrypt_block(blk2, 1)
l2 = list(reversed(blk3[::2]))
l3 = list(reversed(blk3[1::2]))

flag = [0] * 36
for i in range(6):
    flag[30 - 6 * i] = l0[i]
    flag[31 - 6 * i] = l1[i]
    flag[32 - 6 * i] = l2[i]
    flag[33 - 6 * i] = l3[i]
    flag[34 - 6 * i] = l4[i]
    flag[35 - 6 * i] = l5[i]

print(bytes(flag))