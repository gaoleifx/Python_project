####来的封装

class ani:
    def __init__(self, name, type, gender):
        self.name = name
        self.type = type
        self.__gender = gender
    def eat(self):
        print(self.name + " is eating!")
    def show(self):
        print(self.name)
        print(self.type)
        print(self.__gender)#这位类外不希望被访问的


dog = ani("dog", "canine", "he")
print(dog.show())
print(dog.eat())
print(dog.name)
#print(dir(dog))

 