##index()  查找子串substr第一次出现的位置， 如果查找不到，则抛出ValueError
##rindex() 查找子串substr最后一次出现的位置， 如果差找不到， 则抛出ValueError
##find()   查找子串substr第一次出现的位置， 如果查找不到，则返回-1
##rfind()  查找子串substr最后一次出现的位置， 如果差找不到， 则返回-1


s = 'hello, hello'
print(s.index('lo'))  #3
print(s.find('lo'))   #3
print(s.rindex('lo')) #10
print(s.rfind('lo'))  #10

##upper()           把字符串中所有字符都转成大写字母
##lower()           把字符串中所有字符都转成小写字母
##swapcase()        把字符串中所有大写字母转成小写字母，把所有小写转成大写字母
##caplitalize()     把第一个字符转成大写，把其余转成小写
##title()           把每个单词的第一个字符转成大写， 把每个单词的剩余字符转成小写


s1 = 'hell,world,python'
print(s1.rsplit(sep=',', maxsplit=1))

##isidentifier()  判断指定的字符串是否是合法的标识符
##isspace()       判断指定的字符串是否全部由空白字符组成（回车、 换行、水平制表符）
##isalpha()       判断指定的字符串是否全部由字母组成
##isdecimal()     判断指定字符是否全部由十进制的数字组成
##isnumeric()     判断指定字符是否全部由数字组成
##isalnum()       判断指定字符是否全部由子母和数字组成
##isidentifier()判断是否是合法的标识符
s2 = 'hello world'
print('1'.isidentifier())
print('zhangsan'.isidentifier())

###字符的替换和合并replace()   join()
s = 'hello world'
print(s.replace('hello', 'world'), 2)
print(s.replace('world', 'aa'))
#print(s.replace('world', 'aa'))

