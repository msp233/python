import itchat
import time

itchat.auto_login()

itchat.send('Hello, test', toUserName='filehelper')
time.sleep(3)

users = itchat.search_friends(name='少雄')
#aa = itchat.search_friends(name='张三')
itchat.send('Hello, filehelper', toUserName=users[0]['UserName'])
print(users)
