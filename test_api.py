import requests
import json
heard={'Connection': 'keep-alive',
'Content-Length': '102',
'Accept': 'application/json',
'Origin': 'http://v3.carenergynet.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'Content-Type': 'application/json; charset=UTF-8',
'Referer': 'http://v3.carenergynet.cn/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9'
}
#r=requests.get(url='http://v3.carenergynet.cn/')
r=requests.post(url='https://api.carenergynet.cn/plat/api/users/auth',headers=heard,data=json.dumps({'t':1584927385462,'token':{'principal':'林思捷','credentials':'sijie1013','type':'01'},'userId':0}))
print(r.text) #打印返回的正文信息
print(r.encoding) #返回的编码方式
print(r.url) #url地址
print(r.headers) #返回的消息头
print(r.cookies)#返回的用户辨明信息，cookies
#print(r.content)#返回的正文信息，二进制去保存