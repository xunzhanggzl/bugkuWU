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

# 文件包含2

查看源码，发现注释中有 upload.php 的提示，于是打开 http://123.206.31.85:49166/upload.php，发现是文件上传。

在php文件里写入 `<script language=php>system("ls")</script>` ，列当前目录，修改后缀名为jpg,如1.php;.jpg,上传成功，如下图所示：

访问 http://123.206.31.85:49166/index.php?file=upload/201911191206089664.jpg，提示我们：about hello.php index.php this_is_th3_F14g_154f65sd4g35f4d6f43.txt upload upload.php。

然后访问 http://123.206.31.85:49166/index.php?file=this_is_th3_F14g_154f65sd4g35f4d6f43.txt，得到flag

# sql注入2

题目网站：http://123.206.87.240:8007/web2/

直接在后面加上 flag，即http://123.206.87.240:8007/web2/flag，然后下载了一个文件结果就是flag，但是不知道是什么原因，御剑没有扫出来。

# Trim的日记本

使用御剑扫描出来下面的结果，然后打开发现flag，竟然真的是flag

![Trim的日记本](https://raw.githubusercontent.com/xunzhanggzl/bugkuWU/master/image/web_img/Trim%E7%9A%84%E6%97%A5%E8%AE%B0%E6%9C%AC.png)