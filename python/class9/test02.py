# coding=utf-8
import requests,json


# session管理
session = requests.session()

# 发包
res = session.post('http://112.74.191.10:80/inter/HTTP/auth')
print(res.text)
jsonres = json.loads(res.text)
print(jsonres['token'])

# 添加头
session.headers['token'] = jsonres['token']

# (注册接口)构造函数
params = {'username':'hero11',
          'pwd':'123456',
          'nickname':'朱哥',
          'describe':'测试描述'
          }

# 发包
res = session.post('http://112.74.191.10:80/inter/HTTP/register', data=params)
# print(res.content.decode('utf-8'))
print(res.text)


# (登录接口)构造参数
params = {
    'username': 'hero11',
    'password': '123456'
}
# 发包
res = session.post('http://112.74.191.10:80/inter/HTTP/login', data=params)
print(res.text)

# (获取用户id接口)构造参数
jsonres = json.loads(res.text)
params = {
    'id': jsonres['userid']
}

res = session.post('http://112.74.191.10:80/inter/HTTP/getUserInfo', data=params)
print(res.text)


# (退出登录接口)
# 发包
res = session.post('http://112.74.191.10:80/inter/HTTP/logout')
print(res.text)

