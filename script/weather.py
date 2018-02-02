import requests

url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E5%8C%97%E4%BA%AC&output=json&ak=E4805d16520de693a3fe707cdc962045'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# 在公司内网，需要使用代理
proxies = {
    "http": "dev-proxy.oa.com:8080",
    "https": "dev-proxy.oa.com:8080",
}
re = requests.get('url',header=header,proxies=proxies)
print(re)
