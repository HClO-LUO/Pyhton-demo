# HClO Luo
# 小罗
# 2022/10/18 17:38
def list_sort():
    list1=eval(input())
    for i in range(1,len(list1)):
        for j in range(0,len(list1)-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)
    return list1
list_sort()

