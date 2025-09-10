n = int(input())
print("YES" if n%2==1 or (99<n and n<1000) else "NO")

condition_1 = n % 2 == 1
condition_2 = 99 < n < 1000
condition = condition_1 or condition_2

if condition:
    print("YES")
else:
    print("NO")

pass