# "test" --> "e" ->"KKK"
# "tKKKst"
#   "test", "e", "KK"
def T(Str, ch, s):
    if len(Str)==1:
        return Str[0] if Str[0] != ch else s
    return T(Str[:-1], ch, s) + T(Str[-1], ch, s)
print(T("wetybgtest", "e", "KK"))


def change(s, c, s1):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        if s == c:
            return s1
    else:
        return s
    return change(s[0], c, s1) + change(s[1:], c, s1)
print(change("test", "e", "KK"))