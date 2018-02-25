import itchat
import time

itchat.auto_login()

itchat.send('Hello, test', toUserName='filehelper')
time.sleep(3)

users = itchat.search_friends(name='世平a')
#aa = itchat.search_friends(name='张三')
i = 0
while True:
    users = itchat.search_friends(name='邹华风')
    itchat.send('第'+str(i)+'次问你在干嘛啊？', toUserName=users[0]['UserName'])
    itchat.send('测试', toUserName='filehelper')
    #print(users)
    i+=1
    print(i)
    time.sleep(1)
