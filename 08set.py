###集合的创建方式
#直接{} s={'python', 'hello', 90}
##使用内置函数set()
####集合的特点是无序且不重复

s = set(range(6))
print(s)
print(set([3,4,56,89]))
print(set('python'))


############空集合方式
s = set()

#####集合的相关操作
s = {10, 20, 30, 40, 50}
print(type(s))
print(10 in s) ####True
print(100 in s) ###False
print(10 not in s)#####False

s.add(58)####add一次只能添加一个元素
print(s)
s.update([68, 95, 165])
print(s)
s.update({988, 600, 500})
print(s)
s.update((8568, 25))
print(s)


#####删除方式remvoe() 一次删除一个指定元素， 如果指定元素不存在抛出KeyError
#  discord() 一次删除一个指定元素， 如果指定元素不存在不抛出异常
#  clear() 清空集合
#  pop() 一次只删除一个任意元素


##一个集合是否是另一个集合的子集
s1 = {10, 20, 30, 40, 50, 60, 70, 80, 90}
s2 = {20, 30, 40, 50}
s3 = {30, 90}

print(s2.issubset(s1))#True
print(s3.issubset(s1))#True

####一个集合是否是另一个集合的超集
print(s1.issuperset(s2))#True
print(s1.issubset(s3))#False

#####两个集合是否有交集
print(s3.isdisjoint(s1))#False
print(s2.isdisjoint(s1))#False

####数学中的交集
print(s1.intersection(s2))
###数学中的并集
print(s2.union(s1))
print(s2 | s1)
###数学中的差集操作
print(s2.difference(s1))
####对称差集
print(s1.symmetric_difference(s2))

###集合生成式
##列表生成式是list = [i*i for i in range(10)]
s = {i*i for i in range(10)}
print(s)


