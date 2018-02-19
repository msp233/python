#元组，被套上枷锁的列表
#元组，元素值不可修改
tuple1 = (1,2,3,4,5,6,7,8,9)
print(tuple1)
print(tuple1[2])
print(tuple1[1:])
print(tuple1[3:5])
tuple2 = tuple1[:]
print(tuple2)
#tuple1[3] = 3
print(tuple1)
temp = ('a','b','c','d')
temp = temp[:2]+('test',)+temp[2:]
print(temp)
print(8 * ('a',))