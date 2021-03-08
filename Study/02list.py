
#######元素列表的添加操作

list1 = [10, 20, 30, 40]
list2 = ["xiaoming", "xiaoli", "wang"]

#以一个元素插入到列表1的末尾
list1.append(list2)
#print(list1)

#将列表2中的元素插入到列表1的末尾
list1.extend(list2)
#print(list1)

#在列表的任意位置以一个元素插入到列表中
list1.insert(2, list2)
print(list1)