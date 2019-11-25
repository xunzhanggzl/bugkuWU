'''
  利用requests发送post请求，并定制请求头Referer
  理论：https://2.python-requests.org//en/latest/user/quickstart/#custom-headers
  题目：bugkuctf 你从哪里来
'''
import requests

url = "http://123.206.87.240:9009/from.php"
headers = {'Referer': 'https://www.google.com'}
r = requests.get(url, headers=headers)
print(r.text)

# flag{bug-ku_ai_admin}
