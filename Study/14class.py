###object类内方法的重写

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return '我的名字是{0}, 今年是{1}岁'.format(self.name, self.age)
    
stu1 = student("zhangsan", 10)
print(stu1)