import yaml
import os

class Read_Yaml():
    def __init__(self):
        self.path = r'D:\YYService\YYService\test_data\yamldata'
        self.current_filename = os.path.split(os.path.realpath(__file__))[1].split('.')[0] + '.yaml'
        self.abs_path = os.path.abspath(os.path.join(self.path, self.current_filename))

    def read_yaml(self,**kwargs):
        try:
            with open(self.abs_path, encoding='UTF-8') as f:
                content = yaml.safe_load(f)
            return content
        except Exception as f:
            print('读取yaml文件报错如下：{}'.format(f))

    def get_querystring(self,**kwargs):
        content = self.read_yaml()
        querystring = content["querystring"]
        return querystring

    def get_headers(self,**kwargs):
        content = self.read_yaml()
        headers = content["headers"]
        return headers

    def get_data(self,**kwargs):
        content = self.read_yaml()
        data = content["data"]
        return data
    def get_url(self,**kwargs):
        content = self.read_yaml()
        url = content["url"]
        return url

