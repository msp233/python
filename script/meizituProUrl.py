import requests
import os
import re
import time


x = 11991
#y = 3985
y = 68
def url_open(url):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
        }
    # 在公司内网，需要使用代理
    proxies = {
        "http": "dev-proxy.oa.com:8080",
        "https": "dev-proxy.oa.com:8080",
    }
    response = requests.get(url, headers=header)#,proxies=proxies
    return response

def download_mm(url):
    print('url:'+url)
    #http://mm.chinasareview.com/wp-content/uploads/2017a/06/11/09.jpg
    #filename = str(x) + '.' + url.split('.')[-1]
    global x
    #print('x:'+str(x))

    filename = str(x) + '.' + url.split('.')[-1]
    print(filename)
    x += 1
    #print('filename:'+filename)
    with open(filename, 'wb') as f:
        img = url_open(url).content
        f.write(img)
        # page_num += 1

def find_imgs(url):
    html = url_open(url).text

    # <div id="picture"><p>
    #	<img alt="清纯菇娘来一组，妹子你这手机真长得像奶嘴，第1张" src="http://mm.chinasareview.com/wp-content/uploads/2017a/06/05/01.jpg" /><br />
    # </div>
    print('temp')
    #print(html)
    #http://mm.chinasareview.com/wp-content/uploads/2011a/12/69/06.jpg
    url = re.findall('http://mm.chinasareview.com/wp-content/uploads/2011a/12/69/06.jpg',html,re.S)
    temp = re.findall('<div id="picture">(.*?)</div>', html,re.S)
    #print(temp)
    #src="http://mm.chinasareview.com/wp-content/uploads/2017a/08/02/01.jpg"
    if(len(temp) == 0):
        temp = re.findall('<div class="postContent">(.*?)</div>', html, re.S)
    if len(temp)>=1:
        content = temp[0]
        #print(content)
        img_addrs = re.findall('src="(.*?)"', content)
        #print(img_addrs)
        for img_url in img_addrs:
            download_mm(img_url)
def find_article(url):
    html = url_open(url).text
    #print(html)
    print('html')
    article_url_arr = re.findall('<h3 class="tit"><a href="(.*?)"  target=\'_blank\'>',html,re.S)
    #print(article_url_arr)
    for article_url in article_url_arr:
        print(article_url)
        find_imgs(article_url)

def open_mm(folder='test'):
    os.mkdir(folder)
    os.chdir(folder)

    global y

    while y >= 1:
        article_url = url + 'a/' + str(y) + '.html'
        print('article_url:'+article_url)
        #addrs = find_imgs(page_url)
        find_imgs(article_url)
        # x = (len(img_addrs)+1)*(page_num-1)
        y -= 1
        break

    # 只爬取前两页的图片，可改，同时给图片重命名



#http://www.meizitu.com/a/3985.html
if __name__ == '__main__':
    url = 'http://www.meizitu.com/'
    open_mm()