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

