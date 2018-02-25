member = ['msp','maoshiping','v_shipmao']
print(len(member))
print(member)
#append 每次只能加一个元素
print('append 每次只能加一个元素')
member.append('abd')

print(len(member))
print(member)

#extend 每次可以增加多个元素
print('extend 每次可以增加多个元素')
member.extend(['aaa','bbb'])
print(member)

#insert  在列表指定位置插入元素
print('insert  在列表指定位置插入元素')
member.insert(0,'0 first')
print(member)
member.insert(1,'1 second')
print(member)