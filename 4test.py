import random
temp = input('请输入一个整数')
num = int(temp)
i = 1
while(num):
    print(i)
    i+=1
    num-=1

print('################')
temp = input('请输入一个整数')
num = int(temp)
while num:
    i = num-1
    while i:
        print(' ',end=' ')
        i = i-1
    j = num
    while j:
        print('*',end=' ')
        j = j-1
    print()
    num = num-1

print('###########')
temp = input('请输入一个整数')
num = int(temp)
while num:
    j = num-1
    while j:
        print(' ',end=' ')
        j-=1

    k = num
    while k:
        print('*',end = ' ')
        k-=1
    print()
    num -= 1
