# HClO Luo
# 小罗
# 2022/10/22 22:35
def fun1(n):
    if n==1 or n ==2:
        return 1
    elif n>0:
        return fun1(n-1) + fun1(n-2)
n=int(input())
list1=[]
for i in range(1,n+1):
    list1.append(fun1(i))
print(','.join(str(j) for j in list1))
