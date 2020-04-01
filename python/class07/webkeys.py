from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time


class Web:
    """
    封装web自动化函数（关键字）
    """

    def __init__(self):
        self.driver = None

    def openbrowser(self, br='gc', ex=None):
        """
        打开浏览器
        :param br: gc=谷歌浏览器（默认），ff=火狐，ie=IE
        :param ex: 对应driver的路径,默认在项目的lib目录
        :return: 打开成功/失败
        """
        if br == 'gc':
            # 使用用户文件加载缓存和配置chrome的安装路径
            # 创建一个chrome的配置项对象
            option = Options()

            # 获取用户文件路径
            userfile = os.environ['USERPROFILE']
            # print(userfile)

            # 添加用户文件配置
            option.add_argument('--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data-autotest' % userfile)

            # 配置chrome安装路径
            # option.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

            # 驱动就在默认下面（调用的时候可以不写）:
            if ex is None:
                ex = '../lib/chromedriver.exe'

            self.driver = webdriver.Chrome(options=option, executable_path=ex)  # 谷歌浏览器
            self.driver.set_window_size(800, 600)

        elif br == 'ff':
            if ex is None:
                ex = '../lib/geckodriver.exe'

            self.driver = webdriver.Firefox(executable_path=ex)  # 火狐浏览器
            self.driver.set_window_size(800, 600)

        elif br == 'ie':
            if ex is None:
                ex = '../lib/IEDriverServer.exe'
            self.driver = webdriver.Ie(executable_path=ex)  # IE浏览器
            self.driver.set_window_size(800, 600)

        # 隐式等待
        self.driver.implicitly_wait(10)
        return True

    def geturl(self, url):
        """
        打开网站
        :param url: 输入网址
        :return: 打开成功/失败
        """
        if self.driver is None:
            return False

        self.driver.get(url)
        return True

    def click(self, locator):
        """
        通过定位器找到元素，并完成点击
        :param locator:
        :return:
        """
        ele = self.__find_ele(locator)
        ele.click()

    def input(self, locator, text):
        ele = self.__find_ele(locator)
        ele.send_keys(text)

    def __find_ele(self, locator):
        """
        封装xpath找元素的方法
        :param xpath:
        :return:
        """

        if locator.startswith('id='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_id(locator)
        elif locator.startswith('xpath='):
            locator = locator[locator.find('=') + 1:]
            ele = self.driver.find_element_by_xpath(locator)
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

    def sleep(self, t=2):
        if t == '' or t is None:
            t = 2
        else:
            t = int(t)
        time.sleep(t)

    def quit(self):
        self.driver.quit()
