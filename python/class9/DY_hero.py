# coding=utf-8
from FZ_hero import HTTP

# 创建一个http请求库的实例对象
http = HTTP()
# 设置基础url地址
http.seturl('http://112.74.191.10:80/inter/HTTP/')
http.post('auth', '')
# 添加token到头里面
http.addheader('token', http.resjson['token'])
# 注册
http.post('register', 'username=hero944&pwd=123456&nickname=777888&describe=test999')
# 登录
http.post('login', 'username=hero944&password=123456')
# 获取用户信息
http.post('getUserInfo', 'id=%s' % http.resjson['userid'])
http.post('logout', None)
