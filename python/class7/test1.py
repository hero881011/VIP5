# coding=utf-8
from class7.web import Web

webobj = Web()
# 打开谷歌浏览器
webobj.openbrowser()
# 访问网站
webobj.geturl('http://testingedu.com.cn:8000/index.php')
# 登录
webobj.click('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
webobj.input('//*[@id="username"]', '13800138006')
webobj.input('//*[@id="password"]', '123456')
webobj.input('//*[@id="verify_code"]', '111')
webobj.click('//*[@id="loginform"]/div/div[6]/a')

# 校验
# webobj.sleep(2)
# webobj.gettext('/html/body/div[1]/div/div/div/div[2]/a[1]')
# webobj.assertequals('summer', '登录')
# webobj.sleep(3)
# webobj.quit()
