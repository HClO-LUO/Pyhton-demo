# HClO Luo
# 小罗
# 2022/9/15 17:39
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
tuple1=(2,3,4,5,6)
dict1={1:'a',2:'b'}
set1={6,7,8,9}
for i in list1:
    print(i,end=',')
print(type(list1))
print()

for i in tuple1:
    print(i,end=',')
print(type(tuple1))
print()

for k,v in dict1.items():
    print(k,v,end=',')
print(type(dict1))
print()

for i in set1:
    print(i,end=',')
print(type(set1))
print()

print(set(list1))   #列表转为集合
print(dict(zip(list1,list2)))   #两个列表转换为字典
list1[1]=100    #修改列表中第二个数字
print(list1)







