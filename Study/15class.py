####多态



class animal:
    def eat(self):
        print('animal is eating........')
    
class dog(animal):
    def eat(self):
        print('dog is eating.....')

class cat(animal):
    def eat(self):
        print('cat is eating.......')

class preson:
    def eat(self):
        print('preson is eating aaaaaaaa')

def fun(obj):
    obj.eat()

fun(dog())
fun(cat())
fun(preson())

dog1 = dog()
cat1 = cat()

fun(dog1)
fun(cat1)