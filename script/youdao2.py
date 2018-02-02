import requests
import json

while True:
    content = input("请输入：")
    if content == "":
        print("欢迎下次使用")
        break
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
    payload = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1517386828394',
        'sign': '7fa8d0d124838cdc7067a752d5e26f4c',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }

    # 在公司内网，需要使用代理
    proxies = {
        "http": "dev-proxy.oa.com:8080",
        "https": "dev-proxy.oa.com:8080",
    }

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'#'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    response = requests.post(url, params=headers,data=payload,proxies=proxies)

    html = response.text
    target = json.loads(html)
    #print()
    #print(target)
    #print()
    #print(html)
    print("翻译结果：")
    #print(target)
    print(target['translateResult'][0][0]['tgt'])
    print()