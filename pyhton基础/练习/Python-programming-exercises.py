# HClO Luo
# 小罗
# 2022/8/17 13:10
#Q1
list=[]
for i in range(2000,3201):  #range 相当于（，】区间，可以设置步长
    if i%7==0 and i%5!=0:
        list.append(str(i)) #.append 向每个匹配元素内部的末尾位置追加指定的内容
    print(','.join(list))   #.join 输出时在每个元素之间加入符号
#Q2
#函数
def fun1(x):
    if x==0:
        return 1
    return x*fun1(x-1)
x=int(input())
print(fun1(x))

#循环
x=int(input())
s=1
if x==0:
    print('1')
elif x<0:
    print('error')
else:
    for i in range(1, x + 1):
        s *= i
    print(s)
#Q3
n=int(input())
d=dict()    #dict 字典
for i in range(1,1+n):
    d[i]=i*i
print(d)
#Q4
n=input()
l=n.split(',')  #.split(','),按照，分割元素转为列表
t=tuple(l)  #tuple 将列表转为元组
print(l)
print(t)
#Q5
class caps():   #构建组
    def __init__(self):
        self.a=''
    def g(self):
        self.a=input()
    def p(self):
        print(self.a.upper())
a=caps()
a.g()
a.p()









