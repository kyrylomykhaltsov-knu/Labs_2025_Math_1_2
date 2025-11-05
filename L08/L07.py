

x=1 ⇒ gen(0,1,[3,1]) — друк 3 1

x=4 ⇒ gen(0,4,[4]) — друк 4

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