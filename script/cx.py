#考拉兹猜想（英语：Collatz conjecture），又称为奇偶归一猜想、3n＋1猜想、冰雹猜想、角谷猜想、哈塞猜想、乌拉姆猜想或叙拉古猜想，
# 是指对于每一个正整数，如果它是奇数，则对它乘3再加1，如果它是偶数，则对它除以2，如此循环，最终都能够得到1。
x = input('number: ')
trans = 0
print(x,end='')
length = len(x)
x = int(x)
while x != 1:
    if x%2 == 1:
        x = x*3+1
        print('→%d'%x,end='')
        length += len('→%d'%x)
    else:
        x = x/2
        print('\n'+(length-len(str(x))//2)*' '+'↓'+'\n'+\
              (length-len(str(x))//2)*' '+'%d'%x,end='')
    trans += 1
print('\n经过%d次变换' %trans)