# HClO Luo
# 小罗
# 2022/10/16 23:41
#1
def fun1():
    N = int(input())
    if N in range(1,4):
        print(True)
    else:
        for n in range(2,N):
            j=N%n
            if j==0:
                print(False)
                break
            else:
                print(True)
            return n
fun1()