###；类的继承



class preson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class student(preson):
    def __init__(self, name, age, stu_num):
        self.name = name
        self.age = age
        super().__init__(name, age)
        self.stu_num = stu_num
    
    #方法重写
    def info(self):
        super().info()
        print(self.stu_num)

class teacher(preson):
    def __init__(self, name, age, teacherofyear):
        self.name = name
        self.age = age
        super().__init__(name, age)
        self.teacherofyear = teacherofyear

    #方法重写
    def info(self):
        super().info()
        print(self.teacherofyear)

stu1 = student("zhangsan", 20, "1001")
tea1 = teacher('wangwu', 34, 10)

print(stu1.info())
print('____________________________')
print(tea1.info())

