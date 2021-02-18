###特殊方法

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, other):
        return self + other

stu1 = student('zhangsan', 10)
stu2 = student('lisi', 20)

s = stu1.name.__add__(stu2.name)
print(s)