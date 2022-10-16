# HClO Luo
# 小罗
# 2022/10/17 0:01
#2
list_input=eval(input())
list_0=[]
list_origin=[]
for i in range(len(list_input)):
    if list_input[i] == 0:
        list_0.append(0)
    else:
        list_origin.append(list_input[i])
print(list_origin+list_0)
