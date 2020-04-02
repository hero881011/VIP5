import requests, json, traceback

# 会话管理
session = requests.session()

# 获取token
print('\n==========获取token：==========\n')
auth_result = session.post('http://testingedu.com.cn:8081/inter/HTTP/auth')
print(auth_result.text)

auth_json = json.loads(auth_result.text)
print('token=' + auth_json['token'])

# 添加键值对到头里面
session.headers['token'] = auth_json['token']

# 登录
print('\n==========登录：==========\n')
params = {'username': 'hero', 'password': '123456'}
login_result = session.post('http://testingedu.com.cn:8081/inter/HTTP/login', data=params)
print(login_result.text)

login_json = json.loads(login_result.text)

try:
    if login_json['msg'] == '恭喜您，登录成功':
        print('PASS')
    else:
        print('FAIL')

except Exception as e:
    print('FAIL')
    print(traceback.format_exc())

# 获取用户ID
print('\n==========获取用户ID：==========\n')
get_json = json.loads(login_result.text)
params = {'id': get_json['userid']}
get_result = session.post('http://testingedu.com.cn:8081/inter/HTTP/getUserInfo', data=params)
print(get_result.text)

user_json = json.loads(get_result.text)
try:
    if user_json['msg'] == '查询成功':
        print('PASS')
    else:
        print('FAIL')
except Exception as e:
    print('FAIL')
    print(traceback.format_exc())

# 退出登录
print('\n==========退出登录：==========\n')
result = session.post('http://testingedu.com.cn:8081/inter/HTTP/logout')
print(result.text)

# 注册
print('\n==========注册：==========\n')
auth_result = session.post('http://testingedu.com.cn:8081/inter/HTTP/auth')
auth_json = json.loads(auth_result.text)
session.headers['token'] = auth_json['token']
params = {'username': 'hero106', 'pwd': '123456', 'nickname': 'HEROZHU', 'describe': '英雄哥'}
register_result = session.post('http://testingedu.com.cn:8081/inter/HTTP/register', data=params)
print(register_result.text)

register_json = json.loads(register_result.text)
try:
    if register_json['msg'] == '注册成功':
        print('PASS')
    else:
        print('FAIL')
except Exception as e:
    print('FAIL')
    print(traceback.format_exc())
