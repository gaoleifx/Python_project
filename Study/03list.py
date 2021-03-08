###列表元素的删除操作
###remove()一次删除一个元素
###        重复元素只删除一个
###        元素不存在抛出ValueError
###pop()删除一个指定索引位置的元素
###     制定索引不存在抛出IndexError
###     不指定索引， 删除列表中最后一个元素
###clear()一次至少删除一个元素
###del删除列表

list1 = [10, 20, 30, 40]
list2 = ["xiaoming", "xiaoli", "wang"]

list1.extend(list2)
newList = list1

print(newList)

#newList.remove(20)
#newList.pop(1)
#newList.pop(2)
print(newList, id(newList))

list1 = [10, 20, 30, 40]
new_list = sorted(list1)
desc_list = sorted(list1, reverse=True)
print(new_list)
print(desc_list)