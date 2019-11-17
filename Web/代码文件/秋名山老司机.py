import requests
import re  # 这个库一般用来匹配文字

url = 'http://123.206.87.240:8002/qiumingshan/'  # url
r = requests.session()  # requests.sesssion()对象可以跨请求的保存某些参数
g = r.get(url)  # 产生一个请求资源的对象，get方法
# 使用re库中的findall方法，匹配正则。第一个参数是要匹配的正则表达式，第二个参数是将我们请求到的资源变成字符串的形式，再以列表的形式返回到变量ans中
ans = re.findall('<div>(.*?)=?;</div>', g.text)
ans = "".join(ans)  # 将ans从列表的形式转化为字符串的形式
ans = ans[:-2]  # 去掉ans最后的两个字符，这里即去掉 =？
# print(ans)  # 测试打印一下
post = eval(ans)  # 执行我们处理完的字符串，即那个变态的表达式
data = {'value': post}  # 构造data的post部分
flag = r.post(url, data=data)  # 生成post请求，post的值是算出来的结果
# print(flag) # 测试打印返回的结果
print(flag.text)  # 打印返回的数据即flag值
