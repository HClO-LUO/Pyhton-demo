# HClO Luo
# 小罗
# 2022/8/17 11:12
def again():
    def fun1(a, b, c):
        d = b * b - 4 * a * c
        if d < 0:
            print('error,please press again')
        elif d == 0:
            x = -b / 2 * a
            print('only one value=', '%.2f' % x)
        else:
            x1 = (-b + d ** (0.5)) / 2 * a
            x2 = (-b - d ** (0.5)) / 2 * a
            print('x1=', '%.2f' % x1)
            print('x2=', '%.2f' % x2)
        return d

    a = float(input('Pressing a:'))
    b = float(input('Pressing b:'))
    c = float(input('Pressing c:'))
    d = fun1(a, b, c)
    while d < 0:
        a = float(input())
        b = float(input())
        c = float(input())
        d = fun1(a, b, c)
        if d >= 0:
            break
print('Solution of quadratic equation of one variable')
again()
C=str(input('continue：Y or N?:\n'))
if C=='y' or C=='Y':
    again()

