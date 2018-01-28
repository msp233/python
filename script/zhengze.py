import requests
import os
import re
import time

content = '''
src="http://www.baidu.com/abc-def/uploads/2011a/12/69/06.jpg"
src="http://www.baidu.com/abc-def/uploads/2011a/12/69/light.jpg"
src="http://www.baidu.com/abc-def/uploads/2017a/06/15/limg.jpg"
src="http://www.baidu.com/abc-def/uploads/2017a/19/69/06.jpg"
src="http://www.baidu.com/abc-def/uploads/2016b/37/69/28.jpg"
'''
arr = re.findall("http://www.baidu.com/abc-def/uploads/(\w+)/(\d+)/(\d+)/(\d+).jpg",content)
print(arr)