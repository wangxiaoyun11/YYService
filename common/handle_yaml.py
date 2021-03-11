import yaml
import os
from common.handle_log import run_log as logger

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
            logger.exception('读取yaml文件报错如下：{}'.format(f))

    def get_querystring(self,**kwargs):
        try:
            content = self.read_yaml()
            querystring = content["querystring"]
            logger.info('获取querystring数据')
            return querystring
        except Exception as f:
            logger.exception('读取yaml文件报错如下：{}'.format(f))

    def get_headers(self,**kwargs):
        try:
            content = self.read_yaml()
            headers = content["headers"]
            logger.info('获取headers数据')
            return headers
        except Exception as f:
            logger.exception('读取yaml文件报错如下：{}'.format(f))

    def get_data(self,**kwargs):
        try:
            content = self.read_yaml()
            data = content["data"]
            logger.info('获取data数据')
            return data
        except Exception as f:
            logger.exception('读取yaml文件报错如下：{}'.format(f))

    def get_url(self,**kwargs):
        try:
            content = self.read_yaml()
            url = content["url"]
            logger.info('获取url数据')
            return url
        except Exception as f:
            logger.exception('读取yaml文件报错如下：{}'.format(f))
    def get_value(self,keyword,**kwargs):
        try:
            content = self.read_yaml()
            value = content[keyword]
            logger.info('获取value数据')
            return value
        except Exception as f:
            logger.exception('读取yaml文件报错如下：{}'.format(f))

