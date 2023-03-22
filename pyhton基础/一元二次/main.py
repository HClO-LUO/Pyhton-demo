# HClO Luo
# 小罗
# 2022/8/18 8:49
def fun1():
    a = float(input('Press a:'))
    b = float(input('Press b:'))
    c = float(input('Press c:'))
    d = b * b - 4 * a * c
    if d < 0:
        print('Error,please enter again')
        return fun1()
    elif d == 0:
        x = -b / 2 * a
        print('only one value=', '%.2f' % x)
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        print('x1=', '%.2f' % x1)
        print('x2=', '%.2f' % x2)
    return d

def fun2():
    i=int(input('是否继续：1.Yes or 2.No'))
    while True:
        if i==1:
            fun1()
            return fun2()
        elif i==2:
            break
        else:
            return fun2()