import os, time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as gcOptions
# from selenium.webdriver.firefox.options import Options as ffOptions
from selenium.webdriver.common.keys import Keys


class Web:

    def __init__(self):

        self.driver = None

    def openbrowser(self, br='gc', dr=None):

        if br == 'gc':
            option = webdriver.ChromeOptions()
            profile = os.environ['USERPROFILE']
            option.add_argument('--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data-autotest' % profile)

            if dr is None:
                ex = '../lib/chromedriver.exe'

            self.driver = webdriver.Chrome(chrome_options=option, executable_path=dr)  # 谷歌浏览器
            self.driver.set_window_size(800, 600)

        elif br == 'ff':
            if dr is None:
                ex = '../lib/geckodriver.exe'

            # 有cookie的，但是缓存不存在，所以架在还是比较慢
            # 使用cmd命令去创建一个用户文件
            # "C:\Program Files\Mozilla Firefox\firefox.exe" -p

            profile = r'C:\Users\herozhu\AppData\Roaming\Mozilla\Firefox\Profiles\mytest.mytest'
            option = webdriver.FirefoxOptions()
            option.profile = profile
            self.driver = webdriver.Firefox(firefox_options=option, executable_path=dr)
            self.driver.set_window_size(800, 600)

        elif br == 'ie':
            if dr is None:
                ex = '../lib/IEDriverServer.exe'
            self.driver = webdriver.Ie(executable_path=dr)
            self.driver.set_window_size(800, 600)

        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath().get_attribute()
        return True

    def geturl(self, url):

        if self.driver is None:
            return False

        self.driver.get(url)
        return True

    def click(self, locator):
        ele = self.__find_ele(locator)
        ele.click()

    def click_href(self, locator):
        """
        通过定位器招到a标签元素，然后获取到href链接，进行跳转
        主要是处理IE点击失败的情况
        :param locator:
        :return:
        """
        ele = self.__find_ele(locator)
        href = ele.get_attribute('href')
        self.driver.get(href)

    def click_enter(self, locator):
        ele = self.__find_ele(locator)
        ele.send_keys(Keys.ENTER)

    def input(self, locator, text):
        ele = self.__find_ele(locator)
        ele.send_keys(text)

    def __find_ele(self, locator):
        if locator.startswith('id='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_id(locator)
        elif locator.startswith('xpath='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_xpath(locator)
        elif locator.startswith('class='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_class_name(locator)
        elif locator.startswith('className='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_class_name(locator)
        elif locator.startswith('name='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_name(locator)
        else:
            ele = self.driver.find_element_by_xpath(locator)

        return ele

    def gettext(self, location):
        ele = self.__find_ele(location)
        self.txt = ele.text
        return self.txt

    def assertequals(self, exp_value, msg=''):
        if self.txt == exp_value:
            print(msg + '校验成功')
            return True
        else:
            print(msg + '校验失败')
            return False

    def sleep(self, t=3):
        if t == '' or t is None:
            t = 3
        else:
            t = int(t)
        time.sleep(t)

    def quit(self):
        self.driver.quit()
