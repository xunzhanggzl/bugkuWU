'''
  利用requests持续发送get请求
  理论：https://2.python-requests.org//en/latest/user/advanced/#session-objects
  代码：https://cloud.tencent.com/developer/news/294560
  题目：你必须让他停下
'''
import requests

while True:
    url = "http://123.206.87.240:8002/web12/"
    s = requests.session()
    r = s.get(url)
    # print(a1.text)
    if "flag{" in r.text:
        print(r.text)
        break

# ï»¿<html>
# <head>
# <meta charset="utf-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <meta name="description" content="">
# <meta name="author" content="">
# <title>Dummy game</title>
# </head>

# <script language="JavaScript">
# function myrefresh(){
# window.location.reload();
# }
# setTimeout('myrefresh()',500);
# </script>
# <body>
# <center><strong>I want to play Dummy game with othersÂ£Â¡But I can't stop!</strong></center>
# <center>Stop at panda ! u will get flag</center>
# <center><div><img src="10.jpg"/></div></center><br><a style="display:none">flag{dummy_game_1s_s0_popular}</a></body>   </html>