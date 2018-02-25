#假设给定以下列表：
#member = ['msp','maoshiping','v_shipmao']
#要求将列表修改为：
#member = ['msp',88,'maoshiping',99,'v_shipmao',100]

#方法一：使用insert() 和append()方法修改列表
member = ['msp','maoshiping','v_shipmao']
for i in range(3,0,-1):
    if(i == 3):
        member.insert(i,100)
        continue
    if(i == 2):
        member.insert(i,99)
        continue
    if(i == 1):
        member.insert(i,88)
        continue
print(member)
#方法二：创建一个同名字的列表覆盖
member = ['msp',88,'maoshiping',99,'v_shipmao',100]

#利用for循环打印上面member列表中的每个内容
print('利用for循环打印上面member列表中的每个内容')
for each in member:
    print(each)

#优化打印效果
print('优化打印效果')
print('方法一')
i = 0
for each in member:
    if(i % 2 == 0):
        print(each,end='\t')
    else:
        print(each)
    i+=1
print('小甲鱼方法一')
for each in range(len(member)):
    if(each % 2 == 0):
        print(member[each],member[each+1])

print('小甲鱼方法二')
count = 0
length = len(member)
while count < length:
    print(member[count],member[count+1])
    count += 2