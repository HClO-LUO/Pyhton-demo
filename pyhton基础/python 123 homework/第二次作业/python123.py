#1
n=input()
set=set(n)
s=0
for i in set:
    s=s+eval(i)
print(s)

#2
ls = eval(input())
k = int(input())
ls.sort(reverse=True)
print(ls[k-1])

#3
def fun1(list1):
    set1=set(list1)
    if len(set1)<len(list1):
        return True
    else:
        return False
list1=eval(input())
print(fun1(list1))

#4
a=eval(input())
a['chemist']=205
a['math']=201
a.pop('biology','not exist')
ks=sorted(a.keys())
b = {}
for key in ks:
    b[a[key]]=key
for k,v in b.items():
    print('{}:{}'.format(k,v))

#5
dict1=eval(input())
a=input()
print(dict1.get(a,'您输入的键不存在!'))