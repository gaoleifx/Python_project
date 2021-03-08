


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('the student is eating!')

    @classmethod
    def cm(cls):
        print('you are playing baskball')



stu1 = student('zhangsan', 20)
print(stu1.name)
print(stu1.age)

print(student.eat(stu1))