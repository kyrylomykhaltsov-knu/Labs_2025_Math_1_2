n = int(input())

counter = 0
sum = 0
dob =1

while n > 0:
    last = n % 10
    sum += last
    dob *= last
    n = n // 10

print(f"{dob / sum:.3f}")