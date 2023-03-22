def add_student_information(all_information):
    while True:
        name = input('输入学生姓名：')
        if not name:
            break
        age = int(input('输入年龄：'))
        id = int(input('输入学号：'))
        score = int(input('输入成绩：'))
        all_information += [{'name': name, 'age': age, 'id': id, 'score': score}]
    return all_information

def show_all_information(all_information):
    for i in all_information:
        print('姓名：%s学号：%s年龄：%s成绩：%s' % (i['name'].center(20),str(i['id']).center(20),str(i['age']).center(6), str(i['score']).center(6)))


def round1(all_information):
    choose1 = int(input('输入需要修改的内容：1.姓名 2.学号 3.年龄 4.成绩'))
    for j in all_information:
        if choose1 == 1:
            name = str(input('输入姓名'))
            j ['name'] = name
            return name
        elif choose1 == 2:
            id = int(input('学号'))
            j ['id'] = id
            return id
        elif choose1 == 3:
            age = int(input('输入年龄'))
            j ['age'] = age
            return age
        elif choose1 == 4:
            score = int(input('输入成绩'))
            j ['score'] = score
            return score
        else:
            print('请重新选择')
            round1(all_information)

def change_student_information(all_information):
    flag=0
    name=input('输入需要修改的学生学号：')
    for j in all_information:
        if j['name']==name:
            flag=1
            print('已找到该学生信息')
            round1()
            print('修改后的信息为：','%s学号：%s年龄：%s成绩：%s' % (j['name'].center(20),str(j['id']).center(20),str(j['age']).center(6), str(j['score']).center(6)))
    if flag==0:
        print('没有该学生信息')
        choose2=str(input('是否重新输入：Y OR N?'))
        if choose2 == 'Y' or 'y':
            change_student_information()

def delete_student_information(all_information):
    flag=0
    count=0
    name=input('输入学生姓名')
    for p in all_information:
        if p['name']==name:
            del all_information[count]
            flag=1
            print('学生',name,'的信息已删除')
        count+=1
    if flag==0:
        print('系统没有',name,'的信息')
