#function finding numbers to flip in bits

def bit_flips(a, b):
    count= 0
    xor= a^b
    while xor:
        count += xor & 1
        xor >>= 1
    return count
