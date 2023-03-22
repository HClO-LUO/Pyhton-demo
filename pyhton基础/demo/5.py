# HClO Luo
# 小罗
# 2022/10/18 18:13
n=int(input())
i=2
while i<=n:
    if i==n:
        print(i,end='')
        break
    elif n%i ==0:
        print(i,end='*')
        n=n/i
    else:
        i=i+1



