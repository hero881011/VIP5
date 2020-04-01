# coding=utf-8
import requests,json

class HTTP:

    def __init__(self):
        self.session = requests.session()
        self.url = ''
        self.result = None
        self.resjson = None

    def seturl(self,url):
        self.url = url

    def post(self,path,params):
        self.result = self.session.post(self.url + path, data=self.__get_data(params))
        self.resjson = json.loads(self.result.text)
        print(self.resjson)

    def addheader(self,key,value):
        self.session.headers[key] = value

    def __get_data(self,params):

        if params is None or params == '':
            return None
        else:
            params_dict = {}
            params_list = params.split('&')

            for items in params_list:
                if items.find('=') >= 0:
                    params_dict[items[0:items.find('=')]] = items[items.find('=')+1:]
                else:
                    params_dict[items] = None

            return params_dict
