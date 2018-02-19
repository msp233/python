#闰年计算方法
#1、年份能被4整除；
#2、年份若是100的整数倍的话，需被400整除，否则是平年。
#举例如下：
#1900年能被4整除，但是因为其是100的整数倍，却不能被400整除，所以是平年；而2000年就是闰年；
# 1904和2004、2008等直接能被4整除且不被100整除，都是闰年。
print('###########闰年计算器##############')
while(True):
    print('请输入一个年份:',end='')
    temp = input('')
    if(temp ==''):
        break
    if(temp.isdigit()):
        num = int(temp)
        if(num%4 == 0):
            if(num%100 == 0):
                if(num%400 == 0):
                    print('是闰年')
                    continue
                print('是平年')
                continue
            print('是闰年')
            continue
        print('是平年')
        continue
    print('输入的类型不合法，请重新输入：',end='')
print('结束进程\n')

