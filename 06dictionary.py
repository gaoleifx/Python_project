#字典的生成式

myitems = ['Frults', 'Books', 'Apples']
myprices = [96, 35, 84]

mycomp = {myitem:myprice for myitem, myprice in zip(myitems, myprices)}

print(mycomp)