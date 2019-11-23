'''
  利用requests保持一个session发送get请求，并进行base64解码
  理论：https://2.python-requests.org/en/master/user/advanced/#session-objects
  代码：https://blog.csdn.net/lanchunhui/article/details/72681978
  题目：bugkuctf 速度要快
'''
import requests
import base64

url = "http://123.206.87.240:8002/web6/"
r = requests.session()
headers = r.get(url).headers  # 因为flag在消息头里
mid = base64.b64decode(headers['flag'])

print(mid) # 这里解码出来是byte类型的
# b'\xe8\xb7\x91\xe7\x9a\x84\xe8\xbf\x98\xe4\xb8\x8d\xe9\x94\x99\xef\xbc\x8c\xe7\xbb\x99\xe4\xbd\xa0flag\xe5\x90\xa7: NjM5ODk5'

mid = mid.decode()  # 为了下一步用split不报错，b64decode后操作的对象是byte类型的字符串，而split函数要用str类型的

print(mid)
# 跑的还不错，给你flag吧: NjM5ODk5

flag = base64.b64decode(mid.split(':')[1])  # 获得flag:后的值，这里不知道为什么还有这一步解码

print(flag)
# b'639899'

data = {'margin': flag}

print(r.post(url, data).text)  # post方法传上去
# KEY{111dd62fcd377076be18a}
