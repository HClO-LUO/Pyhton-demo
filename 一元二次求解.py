# HClO Luo
# 小罗
# 2022/8/16 23:34
print('二元一次方程组求解')
a=int(input('输入a的值'))
b=int(input('输入b的值'))
c=int(input('输入c的值'))
d=b*b-4*a*c
if d<0:
    print('错误，请重新输入')
    while d<0:
        a = int(input('输入a的值'))
        b = int(input('输入b的值'))
        c = int(input('输入c的值'))
        print('错误，请重新输入')
        d=b*b-4*a*c
    if d == 0:
        x = -b / 2 * a
        print('结果为', x)
    else:
        x1 = (-b + d ** (0.5)) / 2 * a
        x2 = (-b - d ** (0.5)) / 2 * a
        print('结果为', x1)
        print('结果为', x2)
elif d==0:
    x=-b/2*a
    print('结果为',x)
else:
    x1 = (-b + d ** (0.5)) / 2 * a
    x2 = (-b - d ** (0.5)) / 2 * a
    print('结果为', x1)
    print('结果为', x2)
