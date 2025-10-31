def gen(m, prev, cur):
    # m - задане число
    # prev - максимально дозволений наступний доданок
    # (щоб доданки були у незростаючому порядку

    if m == 0:
        print(*cur)
        return

    limit = prev if prev < m else m
    for x in range(1, limit+1):
        cur.append(x)
        gen(m - x, x, cur)
        cur.pop()

n = int(input().strip())
gen(n, n, [])