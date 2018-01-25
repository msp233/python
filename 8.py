temp = input('请输入您的分数：')
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

#三元运算符
x,y = 4,5
small = x if x<y else y
print(small)

#断言
assert 8<9
assert 1>6

print(7)