import random
secret = random.randint(1,10)
temp = input('猜猜看数字为多少：')
num = int(temp)
while(num != secret):
    if (num > secret):
        print('大了')
    else:
        print('小了')
    temp = input('猜错了，重新猜：')
    num = int(temp)

print('猜对了！')
print('游戏结束！')