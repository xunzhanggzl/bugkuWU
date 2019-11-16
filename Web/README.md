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



