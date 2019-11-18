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

# sql注入2

题目网站：http://123.206.87.240:8007/web2/

直接在后面加上 flag，即http://123.206.87.240:8007/web2/flag，然后下载了一个文件结果就是flag，但是不知道是什么原因，御剑没有扫出来。

# Trim的日记本

使用御剑扫描出来下面的结果，然后打开发现flag，竟然真的是flag