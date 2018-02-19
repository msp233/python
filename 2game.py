print('--------------msp-------------')
temp = input('请猜一个数字:')
guess = int(temp)
if(guess == 8 ):
    print('猜对了')
    print('恭喜')
else:
    print('猜错了')
print('游戏结束！')

print('-------test1----------')
tmp = input('请输入姓名：')
name = str(tmp)
print('hello,'+tmp)
print('hello,'+name)

print('--------test2----------1')
tmp = input('请输入1-100之间的数:')
num = int(tmp)
if(1<=num<=100):#1<=num and num<=100
    print('success')
else:
    print('error')
print('the end')

a = 'abc'
b = 'aBc'
if(a==b):
    print ('相等')
else:
    print('不相等')