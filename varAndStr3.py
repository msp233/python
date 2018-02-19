teacher = 'msp'
print(teacher)
teacher = 'MSP'
print(teacher)

first = 6
second = 8
third = first + second
print(third)
aa = str(third)
print(teacher + aa)

print(5+8)
print('5'+'8')

print('Let\'s go')

path = 'c:\now'     #不用转义字符
print(path)
path = 'c:\\now'    #转义字符转义\
print(path)
path = r'c:\now\time'  #原始字符串
print(path)
path = r'c:\now\time'+'\\'  #原始字符串尾部是\
print(path)
path = 'c:\\now\\time\\'  #转义字符串尾部是\
print(path)

print('错误：str是内置函数，不能用作变量名')
str = """
《少年中国说》
少年强
则国强
少年独立
则国独立
...
"""
print (str)

a = 'msp'
b = a
b = 'abc'
print (a)

a = 'msp'
b = a
a = 'abc'
print (b)

# c  小甲鱼 小甲鱼  '520'  原始字符串  5不知道