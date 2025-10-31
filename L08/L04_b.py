def inv(s) -> str:
    if s == "":
        return s
    return s[-1] + inv(s[:-1])

print(inv("Hello"))  # "fdsa"