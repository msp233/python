#0 3.0//2.0  //向下取整
print(3.0//2.0) #1.0
#1  a>b>c  ==   a>b and b<c
#2  5**-2  ==   5**(-2)   5的-2次方  = 1/(5的2次方) = 1/25 = 0.04
#   -5**2  ==   -(5**2)  = -25
print(5**-2)  #0.04
print(-5**2)  #-25
#4
print('not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9 = ',end='')
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
   #False       0         4           6             9
print('原理为')
print('1 and 2 = 2')
print('4 or 5  = 4')

#5 打印一个0-100的所有奇数
print('打印一个0-100的所有奇数')
i = 0
while(i<=100):
    if(i % 2 == 1):
        print(i,end=' ')
    i+=1

#6  有一个长阶梯，每步上2阶，最后剩1阶；每步上3阶，最后剩2阶；每步上5阶，最后剩4阶；每步上6阶，最后剩5阶；每步上7阶，正好；
print('\n有一个长阶梯，每步上2阶，最后剩1阶；每步上3阶，最后剩2阶；每步上5阶，最后剩4阶；每步上6阶，最后剩5阶；每步上7阶，正好；')
print('多重if嵌套')
print('阶梯数为：', end='')
i = 7
while(i % 7 == 0 ):
    if(i % 2 ==1):
        if(i % 3 == 2):
            if(i % 5 == 4):
                if(i % 6 == 5):
                    print(i)
                    break
    i+=14

print('多个and')
print('阶梯数为：',end='')
i = 7
while(i % 7 == 0 ):
    if(i % 2 ==1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5):
        print(i)
        break
    i+=14

##
def funn(max):
    print('多个and yield')
    print('阶梯数为：', end='')
    i = 7
    while (i % 7 == 0 and i<=max):
        if (i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5):
           yield i
        i += 14
Arr = list(funn(999))
print(Arr)
#参考答案
print('参考答案：')
x = 7
i = 1
flag = 0

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1

if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')

print('#####test#######')
e = (i for i in range(10000) if i % 2 ==1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0)
