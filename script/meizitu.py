import requests
import os
import re
import time


def url_open(url):
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
        }
    # 在公司内网，需要使用代理
    proxies = {
        "http": "dev-proxy.oa.com:8080",
        "https": "dev-proxy.oa.com:8080",
    }
    response = requests.get(url, headers=header,proxies=proxies)
    return response


def find_imgs(url):
    html = url_open(url).text
    p = r'<img src="([^"]+\.jpg)"'

    img_addrs = re.findall(p, html)

    return img_addrs


def download_mm(folder='OOXX'):
    os.mkdir(folder)
    os.chdir(folder)

    page_num = 1  # 设置为从第一页开始爬取，可以自己改
    x = 0  # 自命名图片
    img_addrs = []  # 防止图片重复

    # 只爬取前两页的图片，可改，同时给图片重命名
    while page_num <= 2:
        page_url = url + 'a/more_' + str(page_num) + '.html'
        addrs = find_imgs(page_url)
        print(len(addrs))
        # img_addrs = []
        for i in addrs:
            if i in img_addrs:
                continue
            else:
                img_addrs.append(i)
        print(len(img_addrs))
        for each in img_addrs:
            print(each)
        page_num += 1
        # x = (len(img_addrs)+1)*(page_num-1)
    for each in img_addrs:
        print('each:'+each)
        if(x>10):
            break
        filename = str(x) + '.' + each.split('.')[-1]
        print('filename:'+filename)
        x += 1
        with open(filename, 'wb') as f:
            img = url_open(each).content
            f.write(img)
            # page_num += 1


if __name__ == '__main__':
    url = 'http://www.meizitu.com/'
    download_mm()