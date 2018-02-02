# 身份证号码后四位
day = list(range(1,100,1))  #15 16 位，排序
sex = list(range(1,10,2)) #17位 性别， 奇数男，偶数女
static = list(range(0,11))  #18位，校验码，0-9 X

print(day)
print(sex)
print(static)
num = 1

file_name = 'files/password.txt'

file_object = open(file_name ,'a')

for x in day:
    if x <10:
        x = '0'+str(x)
    for y in sex:
        y = y
        for z in static:
            if (z == 10):
                z = 'X'
            #print('x:'+str(x))
            #print('y:'+str(y))
            #print('z:'+str(z))
            str1 = str(x)+str(y)+str(z)
            print(str1)
            print('num:'+str(num))
            num += 1
            file_object.write(str1+"\n")

file_object.close()