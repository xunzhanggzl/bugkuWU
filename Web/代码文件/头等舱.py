'''
  利用requests获取响应的headers
  理论：https://2.python-requests.org//en/latest/user/quickstart/#response-headers
  题目：bugkuctf 头等舱
'''
import requests

url = "http://123.206.87.240:9009/hd.php"
r = requests.get(url)
d = r.headers
print(d)

# {'Server': 'nginx', 'Date': 'Fri, 22 Nov 2019 02:11:21 GMT', 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked',
#  'Connection': 'keep-alive', 'Keep-Alive': 'timeout=60', 'flag{Bugku_k8_23s_istra}': '', 'Content-Encoding': 'gzip'}
