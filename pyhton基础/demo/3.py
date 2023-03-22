# HClO Luo
# 小罗
# 2022/10/18 17:48
def fun1(n):
    if n <1:
        return 1
    else:
        return fun1(n-1)*n
n=int(input())
fun1(n)
print(fun1(n))


