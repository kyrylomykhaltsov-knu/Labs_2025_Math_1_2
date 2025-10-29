def BinToDec(b):
    d = 0
    pow2 = 1
    while b > 0:
        r = b % 10
        d += r * pow2
        b = b // 10
        pow2 *= 2
    return d

def BinToDec2(b):
    d = 0
    b = str(b)
    for c in b:
        r = int(c)
        d = d * 2 + r
    return d


# 29 (10)  - > ??? (2)
# 1 2 4 8 16 32 64 128 256
# 29 : 16  8 4 2 1
#      29 13 5 1 1
# 11101


def DecToBin(d):
    b = 0
    pow10 = 1
    while d > 0:
        r = d % 2
        b += r * pow10
        d = d // 2
        pow10 *= 10
    return b

######### Main #########

A = int(input()) # A = 101
B = int(input()) # B = 100
Adec = BinToDec(A) # Adec = 5
Bdec = BinToDec2(B) # Bdec = 4
Cdec = Adec + Bdec
C = DecToBin(Cdec)
print(C)
# d = BinToDec2("101")
# b = DecToBin(29)
# print(b)