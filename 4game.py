import random
#游戏说明，1-10任意整数，三次机会
secret = random.randint(1,2)
temp = input('猜猜看数字为多少：')
print(type(temp))
#添加异常处理
print(temp.isdigit())
while(not (temp.isdigit())):
    print('aaa')
    temp = input('输入的类型不合法，请输入整数')
    num = int(temp)

num = int(temp)
#type(num) != type(12)
#
i=0
#times 总次数
times = 3

while(1):
    i+=1
    if(i>=times):
        print('次数用尽，退出游戏！')
        break
    if (num > secret):
        print('大了')
    elif(num < secret):
        print('小了')
    elif(num==secret):
        print('猜对了！')
        break

    temp = input('猜错了，重新猜：')
    num = int(temp)

print('游戏结束！')

i=10
while i:
    #print('I love you!')
    i -= 1

#请写出与10<cost<50等价的表达式
cost = 11
if(cost>10 and cost<50):
    print('10<cost<50')

#一行可以书写多个语句么？
print('aa');print('bb')

#一个语句可以分成多行书写么？
print('a'
      'b')

#python的and操作符与C语言的&&操作符有什么区别？
print(1 and 3);print(0 and 1)