#for while
author = 'msp maoshiping v_shipmao'
for i in author:
    print(i,end=' ')

print()

member = ['msp','maoshiping','v_shipmao']
for each in member:
    print(each,len(each))
    print(each,len(member))

#range([strat,] stop[, step=1])
print('range([strat,] stop[, step=1])   \nrange作用：生成一个从start值（默认为0）开始，步长为step（默认为1），到stop结束(不包括stop)的数字序列')

arr = range(0,20,2)
print(arr)
arr1 = list(arr)
print(arr1)
print(list(range(5)))
for i in range(5):
    print(i)

print('--------test---------')
for i in range(10):
    if(i%2 != 0):
        print(i)
        continue
    i += 2
    print(i)