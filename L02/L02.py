n = 325

s = n // 100
d = n % 100 // 10
o = n % 100 % 10

condition_n = s == 2 or d == 2 or o == 2
print("n) ", condition_n)

condition_p = s % 2 == 0 and d % 2 == 0 and o % 2 == 0
print("n) ", condition_p)

condition_s = s + d + o == 18
print("n) ", condition_s)