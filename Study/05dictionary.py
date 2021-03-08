###字典创建的两种方式

dict1 = {"xiaoming":60, "xiaoli":25, "wangwu":35}
print(dict1)
print(type(dict))
student = dict(name='zhangsan', age=25)
print(student)

######字典的获取操作
print(student['name'])
print(student.get('name'))

print(dict1.keys())#获取字典的key
print(dict1.values())##获取字典的value
print(type(dict1.values()))
print(dict1.items())##获取字典的所有键值对， 转换之后的列表是由元组组成
print(type(dict1.items()))