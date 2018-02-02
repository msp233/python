import random
import codecs

secret = random.randint(1,10)
file_name = 'files/user.log'

file_object = codecs.open(file_name ,'a','utf-8-sig')
title = '学号\t姓名\t性别\t年龄\t'
file_object.write(title+"\n")

arr = list(range(1,1000,1))
for i in arr:
    lastName = '张李王周武赵钱孙'
    firstName = '三四五平建军国庆不凡桐福东顺兰茜雅'
    len = random.randint(1,2)
    #print(len)
    num = 1
    name = ''
    fname = ''
    while(num<=len):
        lname = lastName[random.randint(0,7)]
        f = random.randint(0,16)
        fname += firstName[f]
            #print(n)
        num += 1
    name = lname+fname


    id= str(i)
    sex = str(random.randint(0,1))
    age = str(random.randint(6,100))
    str2 = id+'\t'+name+'\t'+sex+'\t'+age+'\t'
    print(str2)
    file_object.write(str2 + "\n")


file_object.close()