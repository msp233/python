while True:
    temp = input('请输入您的分数：')
    if temp == '':
        break
    if temp.isdigit():
        screct = int(temp)
        if(90<screct<=100):
            print('A')
        elif(screct>100 or screct<0):
            print('输入的分数有误！')
        elif(screct>=80):
            print('B')
        elif(screct>=60):
            print('C')
        elif(screct<60):
            print('D')
    else:
        print('输入的格式错误',end=' ')
print('程序结束')

#三元运算符
x,y = 4,5
small = x if x<y else y
    #当 x<y 条件为真时，将x值赋给small，否则将y值赋给small
print(small)

#断言 当关键字后面的条件为假的时候，程序自动崩溃并抛出异常 AssertionError
#防止条件有问题导致程序异常
assert 8<9
assert 1>6

print(7)