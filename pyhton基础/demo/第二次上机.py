# HClO Luo
# 小罗
# 2022/9/15 18:13
#1
list1=[1,2,3,4,5,6]
s=1
for x in list1:
    s=s*x
print(s)
#2
list2=['Red','Green','White','Black','Pink','Yellow']
del list2[0]
del list2[3]
del list2[3]
print(list2)
#3
tuple1=20200,15,11
print(tuple1)
tuple2=3,
t1=tuple1+tuple2
print(t1)
#4
t='p','y','t','h','o','n'
str1=''.join(t)
print(str1)
#5
dict1={'Name':'Nobody','Age':0,'Height':175}
dict1['Name']='Lizhe'
dict1['Age']=22
dict1['Height']=183
print(dict1)
#6
d1={1:1,2:2}
d2={3:3,4:4}
d3={**d1,**d2}
print(d3)
#7
dictdemo={}
a=int(input())
for k in range(1,a+1):
    k=k
    v=k**2
    dictdemo[k]=v
print(dictdemo)
#8
set1={1,2,3,4,5}
set2={1,2,3}
if set2&set1 == set2:
    print('ture')
else:
    print('false')





