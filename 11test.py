member = ['0 first', 'msp', 'maoshiping', 'v_shipmao', 'abd', 'aaa', 'bbb','a','b','c','d','e','f']
print(member)

print(member[2:5])
print('###list[0] 与 list[0:1] 区别')
print(member[0])
print(member[0:1])

print('###如何每次从列表末尾取出一个元素，并插入到这个列表的最前面')
member1 = member[:]
print(member1)
member1.insert(0,member1.pop())
print(member1)

print('###试试list[-3:-1]')
print(member[-3:-1])

print('分片步长  list[0:8:2]')
print(member)
print(member[0:8:2])
print(member[::-1])
