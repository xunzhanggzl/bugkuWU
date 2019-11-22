'''
  利用requests发送post请求
  理论：https://2.python-requests.org//en/latest/user/quickstart/
  代码：https://stackoverflow.com/questions/11322430/how-to-send-post-request
  题目：bugkuctf web基础$_POST
'''
import requests

payload = {'what': 'flag'}

r = requests.post("http://123.206.87.240:8002/post/", data=payload)

print(r.text)

# $what=$_POST['what'];<br>
# echo $what;<br>
# if($what=='flag')<br>
# echo 'flag{****}';<br>


# flagflag{bugku_get_ssseint67se}
