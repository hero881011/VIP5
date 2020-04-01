# coding=utf-8
import requests,json

class HTTP:

    def __init__(self):
        # session管理
        self.session = requests.session()
        # 基础的host地址
        self.url = ''
        # 结果解析
        self.result = None
        self.jasonres = None

    def seturl(self,url):
        """
        设置基本url地址
        :param url:
        :return:
        """
        self.url = url

    def post(self,path,params):
        """
        发送post请求
        :param path:请求的路径
        :param params:参数
        :return:无
        """
        self.result = self.session.post(self.url + path, data=self.__get_data(params))
        self.jsonres = json.loads(self.result.text)
        print(self.jsonres)

    def addheader(self,key,value):
        """
        在session上面添加头
        :param key: 头的键
        :param value: 头的值
        :return:无
        """
        self.session.headers[key] = value


    def __get_data(self,params):
        """
        将标准的url格式参数转换为字典
        :param params: url参数字符串
        :return: 转换后的字典
        """
        if params is None or params == '':
            # 如果是空或者空字符串，都返回None
            return None
        else:
            params_dict = {}
            # 分割url字符串的键值对
            list_params = params.split('&')
            # 遍历键值对
            for items in list_params:
                # 如果键值对里面有'='，那么我们就取=左边为键，=右边为值
                # 主要是支持值里面传'='
                if items.find('=') >= 0:
                    params_dict[items[0:items.find('=')]] = items[items.find('=')+1:]
                else:
                    # 如果没有=，处理为键，值为空
                    params_dict[items] = None

            return params_dict