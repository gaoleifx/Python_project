list = []
for i in range(0, 10):
    list.append(i*10)

a1 = list[::-1]#列表反向
a2 = list[1:5]
a3 = list[:3:1]
a4 = list[:5:2]
a5 = list[0::2]

print(list)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)