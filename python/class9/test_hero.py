# coding=utf-8
import requests,json

url = 'http://112.74.191.10:80/inter/HTTP/auth'
session = requests.session()

# 获取token
res = session.post(url)
res_json = json.loads(res.text)
print(res_json)
token = res_json['token']
print('token:'+ token)

session.headers['token'] = token
# print(session.headers)


# 注册
url1 = 'http://112.74.191.10:80/inter/HTTP/register'
params = {'username':'hero15',
          'pwd':'123456',
          'nickname':'朱哥666',
          'describe':'接口测试1'
          }

res1 = session.post(url1, data=params)
print(res1.text)

res_json1 = json.loads(res1.text)
if res_json1['msg'] == '注册成功':
    print(params['username'] + '注册成功')
else:
    print(params['username'] + '注册失败')


# 登录
url2 = 'http://112.74.191.10:80/inter/HTTP/login'
params = {'username':'hero15',
          'password':'123456'
          }
res2 = session.post(url2, data=params)
print(res2.text)

res_json2 = json.loads(res2.text)
if res_json2['msg'] == '恭喜您，登录成功':
    print(params['username'] + '登录成功')
else:
    print(params['username'] + '登录失败')



# 获取用户id
url3 = 'http://112.74.191.10:80/inter/HTTP/getUserInfo'
params = {
    'id': res_json2['userid']
}
res3 = session.post(url3, data=params)
print(res3.text)

res_json3 = json.loads(res3.text)
if res_json3['msg'] == '查询成功':
    print(params['username'] + '登录成功')
else:
    print(params['username'] + '登录失败')


# 退出登录
url4 = 'http://112.74.191.10:80/inter/HTTP/logout'
res4 = session.post(url4)
print(res4.text)

res_json4 = json.loads(res4.text)
if res_json4['msg'] == '用户已退出登录':
    print(params['username'] + '成功退出')
else:
    print(params['username'] + '退出失败')

