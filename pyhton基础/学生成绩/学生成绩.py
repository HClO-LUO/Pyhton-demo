class student():
    def __init__(self):
        self.name = None
        self.num = None
        self.score = None
        self.grade = None
    def g(self):
        if self.score>90:
            self.grade='A'
        elif 80 < self.score < 89:
            self.grade = 'B'
        elif 70 < self.score < 79:
            self.grade = 'C'
        elif 60 < self.score < 69:
            self.grade = 'D'
        elif self.score > 100:
            self.score='Error'
        else:
            self.grade = 'E'
        return self.grade
    def p(self):
        print("%s，学号%s，成绩为%s，等级为%s"%(self.name,self.num,self.score,self.grade))

def fun1():
    s1 = student()
    s1.name = input('姓名')
    s1.num = input('学号')
    s1.score = int(input('成绩'))
    s1.grade = s1.g()
    s1.p()

t=int(input('班级总人数'))
for r in range(1,t+1):
    fun1()







