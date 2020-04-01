# coding=utf-8
import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 获取当前用户环境变量
# d = os.environ["USERPROFILE"]
# print(d)

# 谷歌浏览器配置文件对象
opt = Options()
opt.add_argument('--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data-autotest' % os.environ["USERPROFILE"])

# 打开浏览器
driver = webdriver.Chrome(options=opt, executable_path='../lib/chromedriver')
# driver = webdriver.Chrome()
driver.set_window_size(800, 600)

# 隐式等待
driver.implicitly_wait(10)

#  访问网页
driver.get('http://112.74.191.10:8000/')
# driver.get('https://pan.baidu.com/')


# 找元素
ele = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
ele.click()

# 操作元素
# 登录
driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('111')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a').click()

# 校验登录
time.sleep(2)
txt = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/a[1]')

if txt == 'summer':
    print('登录成功')
else:
    print('登录失败')

# 关闭浏览器
driver.quit()
