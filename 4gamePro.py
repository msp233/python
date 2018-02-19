import random
#游戏说明，1-10任意整数，三次机会
secret = random.randint(1,2)
guess = 0
print('猜猜看数字为多少：',end=' ')

i=0
#times 总次数
times = 3

while(guess!=secret and i<times):
    i+=1
    temp = input('')
    if(i>=times):
        print('三次机会用完了，',end='')
        break
    if(not (temp.isdigit())):
        print('输入的类型不合法，请重新输入:',end='')
        continue
    num = int(temp)
    if (num > secret):
        print('大了',end=' ')
    elif(num < secret):
        print('小了',end=' ')
    elif(num==secret):
        print('猜对了！',end=' ')
        break
    print('猜错了，重新猜：',end='')
print('游戏结束！')

