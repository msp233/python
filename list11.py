member = ['0 first', 'msp', 'maoshiping', 'v_shipmao', 'abd', 'aaa', 'bbb']
print(member)

#remove 删除列表指定元素
print('remove 删除列表指定元素')
member.remove('maoshiping')
print(member)

#del 删除列表指定位置元素
print('del 删除列表指定位置元素')
del member[0]
print(member)

#pop 删除列表最后一个元素，并将删除的元素返回返回
print('pop 删除列表最后一个元素，并将删除的元素返回')
ll = member.pop()
print(ll)
print(member)

#列表分片
print('列表分片\nmember[1:3] 取出列表中下标1-3(3不包括)')
print(member[1:3])
print('member[:3]')
print(member[:3])
print('member[1:]')
print(member[1:])
print('member[:]')
print(member[:])














