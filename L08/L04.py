def isSym(s):
    #
    #
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isSym(s[1:-1])
res = isSym("asdsa")
print(res)

