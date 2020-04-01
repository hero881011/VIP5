# coding=utf-8
import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Web:
    """
    封装Web自动化的常用操作
    """

    def __init__(self):
        # 定义实例变量，存储浏览器，这个浏览器可以在整个类里面被调用
        self.driver = None
        self.txt = ''

    def openbrowser(self, br=None, dr=None):
        """
        打开浏览器

        :param br: 指定打开浏览器的类型
        （gc：谷歌，ff：火狐，ie：IE浏览器,默认为gc）
        :param dr: 指定driver文件的位置
                    (默认为：../lib/chromedriver)
        :return:
        """
        if br is None or br == '':
            br = 'gc'

        if dr is None or dr == '':
            dr = '../lib/chromedriver'

        if br == 'gc':
            # 谷歌浏览器配置对象
            opt = Options()
            opt.add_argument(
                '--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data' % os.environ["USERPROFILE"])

            # 打开浏览器
            self.driver = webdriver.Chrome(options=opt, executable_path=dr)
            self.driver.set_window_size(900, 800)

            # 隐式等待
            self.driver.implicitly_wait(10)
        else:
            print('waiting')

    def geturl(self, url):
        """
        打开网页地址
        :param url: 网站地址，必须以http/htpps开头
        :return:
        """
        self.driver.get(url)

    def click(self, xpath):
        """
        点击元素
        :param xpath: 定位元素的xpath
        :return:
        """
        ele = self.__findele(xpath)
        ele.click()

    def input(self, xpath, value):
        """
        输入文本
        :param xpath: 定位元素的xpath
        :param value: 需要输入的文本
        :return:无
        """
        ele = self.__findele(xpath)
        ele.send_keys(value)

    def gettext(self, xpath):
        """
        获取元素的文本
        :param xpath: 定位元素的xpath
        :return:元素的文本
        """
        ele = self.__findele(xpath)
        self.txt = ele.text
        return self.txt

    def __findele(self, xpath):
        """
        封装xpath找元素的方法
        :param xpath:
        :return:
        """

        ele = self.driver.find_element_by_xpath(xpath)
        return ele

    def sleep(self, t=1):
        if t is None or t == '':
            t = 1
        else:
            t = int(t)

        time.sleep(t)

    def assertequals(self, exp_value, msg=''):
        """
         校验上一步获取的文本和期望值一样
        :param exp_value: 期望值
        :return:是否一样
        """
        if self.txt == exp_value:
            print(msg + '校验成功')
            return True
        else:
            print(msg + '校验失败')
            return False

    def quit(self):
        """
        退出当前打开的浏览器
        :return:
        """
        self.driver.quit()
