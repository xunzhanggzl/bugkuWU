# 秋名山老司机

亲请在2s内计算老司机的车速是多少

702165421+1154429138+1042541861*338334935-739834476-1652744732-1887097714-244715547*1461030294-401250319-977461116=?;

Give me value post about 1531922609+1823637330*1021219038*24080258-1453837304+724139088+460522784-596962562-1691520371*1512685444-1749655109=?

上面的提示给出是用POST请求，发送value值，两秒内肯定自己算不出来，写一个python脚本如下

```python
import requests
import re  # 这个库一般用来匹配文字

url = 'http://123.206.87.240:8002/qiumingshan/'  # url
r = requests.session()  # requests.sesssion()对象可以跨请求的保存某些参数
g = r.get(url)  # 产生一个请求资源的对象，get方法
# 使用re库中的findall方法，匹配正则。第一个参数是要匹配的正则表达式，第二个参数是将我们请求到的资源变成字符串的形式，再以列表的形式返回到变量ans中
ans = re.findall('<div>(.*?)=?;</div>', g.text)
ans = "".join(ans)  # 将ans从列表的形式转化为字符串的形式
ans = ans[:-2]  # 去掉ans最后的两个字符，这里即去掉 =？
print(ans)  # 测试打印一下
post = eval(ans)  # 执行我们处理完的字符串，即那个变态的表达式
data = {'value': post}  # 构造data的post部分
flag = r.post(url, data=data)  # 生成post请求，post的值是算出来的结果
print(flag) # 测试打印返回的结果
print(flag.text)  # 打印返回的数据即flag值
```

运行这段脚本，即可得到flag

# 速度要快

通过抓包得到了下面的内容

```
HTTP/1.1 200 OK
Server: nginx
Date: Sun, 17 Nov 2019 07:45:55 GMT
Content-Type: text/html;charset=utf-8
Connection: close
Set-Cookie: PHPSESSID=v3p9s5foi1t6b351e05nm86e6pk49js3; path=/; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
flag: 6LeR55qE6L+Y5LiN6ZSZ77yM57uZ5L2gZmxhZ+WQpzogTXpNd05URTM=
Content-Length: 89

</br>ææè§ä½ å¾å¿«ç¹!!!<!-- OK ,now you have to post the margin what you find -->
```

将flag那个字段进行base64解码，得到的是**跑的还不错，给你flag吧: MzMwNTE3**，然而这是不对的，然后发现每次抓包flag那个字段都会改变，所以要写脚本。

```python
import requests
import base64
url = "http://123.206.87.240:8002/web6/"
r = requests.session()
headers = r.get(url).headers  # 因为flag在消息头里

mid = base64.b64decode(headers['flag'])
mid = mid.decode()  # 为了下一步用split不报错，b64decode后操作的对象是byte类型的字符串，而split函数要用str类型的

flag = base64.b64decode(mid.split(':')[1])  # 获得flag:后的值
data = {'margin': flag}
print(r.post(url, data).text)  # post方法传上去
```

运行这段脚本，即可得到flag