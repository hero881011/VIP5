from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# # 使用用户文件加载缓存和配置chrome的安装路径
# # 创建一个chrome的配置项对象
option = Options()

# # 获取用户文件路径
userfile = os.environ['USERPROFILE']
# print(userfile)

# # 添加用户文件配置
option.add_argument('--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data-autotest' % userfile)

# # 配置chrome安装路径
# option.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# 打开浏览器
driver = webdriver.Chrome(options=option)  # 谷歌浏览器

# driver = webdriver.Ie(executable_path='../lib/IEDriverServer.exe')   # IE浏览器

# driver = webdriver.Firefox(executable_path='../lib/geckodriver.exe')   # 火狐浏览器

# 访问网址
driver.get('http://testingedu.com.cn:8000/index.php')
