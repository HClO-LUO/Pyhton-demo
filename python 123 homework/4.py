# HClO Luo
# 小罗
# 2022/9/12 17:20
#https://github.com/HClO-LUO/Pyhton-demo.git
a = int(input())
if a > 0:
    a = a
elif a < 0:
    a = abs(a)
h=a//100
t=(a//10)%10
o=a%10
print('{},{},{}'.format(o,t,h))

