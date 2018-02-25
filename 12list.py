#单个元素列表比较
print('单个元素列表比较')
list1 = [123]
list2 = [234]
print(list1>list2)
print(list1<list2)

print('\n多个元素列表比较 只比较第一个元素')
list1 = [123,678]
list2 = [234,567]
print(list1>list2)
print(list1<list2)

print('\n列表的相加')
print(list1)
print(list2)
print(list1+list2)

print('\n 123 in list1')
print(123 in list1)

print('\n 123 not in list1')
print(123 not in list1)

list3 = [123,['abc','bcd',123],456]
status = 'abc' in list3
print('\'abc\' in list3')
print(status)

status = 'abc' in list3[1]
print('\'abc\' in list3[1]')
print(status)
print()

#print(dir(list))

list4 = list3 * 3
counts = list4.count(123)
print(list4)
print(counts)
print(list4.count(456))

print(list4.index(456))
print('list4.index(123,2,8) 在列表list4的下标为2(包括2)开始到下标为8(不包括8)之间，第一次出现 123 的位置')
print(list4.index(123,2,8)) #在列表list4的下标为2开始到下标为8之间，第一次出现 123 的位置

print('\nreverse 翻转列表(列表中的列表不翻转)')
print('list4:')
print(list4)
list4.reverse()
print(list4)

print('''
sort 将列表排序 
reverse参数默认为False，此时从小到大排序，
为True时，从大到小排序
''')
list5 = [3,7,2,98,12,1,11,17,32,8]
print(list5)
list5.sort(reverse=True)
print(list5)