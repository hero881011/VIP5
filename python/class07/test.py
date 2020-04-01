from class07.homework07 import Web

web = Web()
web.openbrowser('gc')
web.geturl('http://testingedu.com.cn:8000/index.php')
web.click_href('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
web.input('//*[@id="username"]', '13800138006')
web.input('//*[@id="password"]', '123456')
web.input('id=verify_code', '111')
web.click_enter('//*[@id="loginform"]/div/div[6]/a')
# 校验
web.sleep()
web.gettext('/html/body/div[1]/div/div/div/div[2]/a[1]')
web.assertequals('summer', '登录')
web.sleep()
web.quit()
