import requests
import json

while True:
    content = input("请输入：")
    if content == "":
        print("欢迎下次使用")
        break
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"

        , 'i': content
        , 'from': 'AUTO'
        , 'to': 'AUTO'
        , 'smartresult': 'dict'
        , 'client': 'fanyideskweb'
        , 'salt': '1514345577426'
        , 'sign': '8a12c3bae1619e0d60247aa90a4d945e'
        , 'doctype': 'json'
        , 'version': '2.1'
        , 'keyfrom': 'fanyi.web'
        , 'action': 'FY_BY_REALTIME'
        , 'typoResult': 'false'
        }

    # 在公司内网，需要使用代理
    proxies = {
        "http": "dev-proxy.oa.com:8080",
        "https": "dev-proxy.oa.com:8080",
    }

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'
    response = requests.get(url, params=headers,proxies=proxies)

    html = response.text
    target = json.loads(html)
    #print()
    #print(target)
    #print()
    #print(html)
    print("翻译结果：")
    print(target['translateResult'][0][0]['tgt'])
    print()