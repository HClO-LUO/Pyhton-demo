# HClO Luo
# 小罗
#从txt文件中获取数据转换为列表
def openreadtxt(file_name):
    data=[]
    file = open(file_name,'r')
    file_data = file.readlines()
    for row in file_data:
        tmp_list = row.split(';')
        data.append(tmp_list)
    return data
if __name__ == "__main__":
    data = openreadtxt('C:/Users/LUO/Desktop/1500.txt') #括号里面是txt文件地址
    # print(data)
#将列表数据输出到excel
result = open('C:/Users/LUO/Desktop/1500.xls','w',encoding='gbk') #括号里是excel文件地址
for m in range(len(data)):
    for n in range(len(data[m])):
        result.write(str(data[m][n]))
        result.write('\t')
    result.write('\n')
result.close()