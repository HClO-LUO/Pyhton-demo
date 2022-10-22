# HClO Luo
# 小罗
# 2022/10/22 23:01
def peach(n):
    if n==10:
        return 1
    else:
        return (peach(n+1)+1)*2
for i in range(10,0,-1):
    print("第{}天有{}只桃子".format(i,peach(i)))