def isSym(s):
    # "2"
    # "asdsa"
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return isSym(s[1:-1])
res = isSym("asdsa")
print(res)

