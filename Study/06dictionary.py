#字典的生成式
a = dict(one=1, two=2, three=3)
b = {'one':1, 'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'one':1, 'two':2, 'three':3})
a == b == c == d == e

myitems = ['Frults', 'Books', 'Apples']
myprices = [96, 35, 84]

mycomp = {myitem:myprice for myitem, myprice in zip(myitems, myprices)}

print(mycomp)