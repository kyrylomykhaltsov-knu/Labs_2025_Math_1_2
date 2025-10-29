# n = 5
# def pascal_iter(n: int):
#     if n <= 0:
#         return
#     row = [1]
#     for _ in range(n):
#         print(*row)
#         row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
# # приклад:
# pascal_iter(int(input()))
# від Чуйко Михайло
def R(n):
    A=[[1], [1,1]]
    for i in range(2,n):
        A.append([1])
        for j in range(1,i):
            A[i].append(A[i-1][j]+A[i-1][j-1])
        A[i].append(1)
    return A

A=R(11)
for a in A:
    print(*a)