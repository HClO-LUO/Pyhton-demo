def fun1(n,m):
    if m==n:
        return 1
    elif m==1:
        return n
    else:
        return fun1(n-1,m-1)+fun1(n-1,m)
n=int(input())
m=int(input())
print(fun1(n,m))
