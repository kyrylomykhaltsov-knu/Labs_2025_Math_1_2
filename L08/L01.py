# 0! = 1
# 5! = 4! * 5
#      //
# 4! = 3! * 4
#      //
# 3! = 2! * 3
#      //
# 2! = 1! * 2
#      //
# 1! = 0! * 1
#      //
# 0! = 1

########## Main ##########

def Fact(n):
    if n == 0:
        return 1
    else:
        f = Fact(n-1)
        return f * n

f = Fact(5)
print(f)