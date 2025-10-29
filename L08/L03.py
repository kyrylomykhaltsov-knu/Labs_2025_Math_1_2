#                       1                  0
#                    1     1               1
#                  1    2    1             2
#                1   3     3    1          3
#              1   4    6    4    1        4
#            1   5   10    10   5    1     5
#
# C(n, k)
# C(n, 0) = 1, C(n, n) = 1
# C(5, 2) = C(4, 1) + C(4, 2)
# C(3, 1) = C(2, 0) + C(2, 1)
# C(n, k) = C(n-1, k-1) + C(n-1, k)

# def C(n, k):
#     if k == 0 or k == n:
#         return 1
#     else:
#         return C(n-1, k-1) + C(n-1, k)
# print(C(5, 2)

def C(n, k):
    # біноміальний коефіцієнт
    if k == 0 or k == n:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)

def print_row(i, k=0):
    # рекурсивно друкує i-й рядок: C(i,0) C(i,1) ... C(i,i)
    if k > i:
        print()            # кінець рядка
        return
    if k > 0:
        print(' ', end='')
    print(C(i, k), end='')
    print_row(i, k + 1)

def pascal_rec(n, i=0):
    # рекурсивно друкує перші n рядків (0..n-1)
    if n <= 0:
        return
    if i == n:
        return
    print_row(i)
    pascal_rec(n, i + 1)

# приклад:
pascal_rec(15)
