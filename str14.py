str1 = 'I\'m amazing!'
print(str1)
str1 = str1[:5]+'添加的字符串'+str1[5:]
print(str1)

str2 = 'xiaomi leijun'
print(str2)
#capitalize 把字符串第一个字符改为大写
str2 = str2.capitalize()
print('capitalize:'+str2)
#casefold 将字符串所有字符改为小写
str2 = str2.casefold()
print('casefold'+str2)

str2 = str2.center(15)
print(str2)

print('count(sub[,start[,end]] 返回字符串sub 在字符串中出现的次数，开始位置、结束位置 可选')
str2='abcdfadfadfagfgafgasfgsfgadfafasdffsadf'
counts = str2.count('ad')
print(counts)
print(str2.count('ad',6,7))
print(str2.count('ad',5,7))
print(str2.count('ad',5,6))

#endswith(sub[,start[,end]) 字符串是否以 sub结尾
print('endswith(sub[,start[,end]) 字符串是否以 sub结尾')
print(str2.endswith('ad'))

print('expandtabs([tabsize=8]) 将字符串中的制表符\\t 转换为空格，默认空格为八个字符')
str2 = 'ab cd as\tsdf fda\\tdfa'
print(str2.expandtabs())

print('find(sub[,start[,end]) 检测sub是否在字符串中，有则返回索引值，否则返回-1，start end 范围可选')
str2 = 'ab cd as\tsdf fda\\tdfa'
print(str2.find('a'))
print(str2.find('s'))
print(str2.find('dA'))
print(str2.find('da'))










