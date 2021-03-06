# coding=utf-8
from common.handle_log import run_log as logger
from apipageobject import login
from common.read_config import ReadConfig

class BasicRequest(object):

    def __init__(self):
        READ = ReadConfig()
        self.api_root_url = READ.get_value(key='url',node='pre')
        self.path = r'D:\YYService\YYService\test_data\yamldata'
        self.session = login.test_login()

    def send_get(self,url,data=None,header=None,cookie=None):
        try:
            logger.info('调用get接口')
            return self.session.get(url=self.api_root_url+url,params=data,headers=header,cookies=cookie)

        except Exception as e:
            logger.exception('get接口调用失败，信息如下：'.format(e))

    def send_post(self,url,data,header=None,cookie=None,param=None):
        try:
            logger.info('调用post接口')
            return self.session.post(url=self.api_root_url+url,json=data,headers=header,cookies=cookie,params=param)
        except Exception as e:
            logger.exception('post接口调用失败，信息如下：'.format(e))

    def send_delete(self,url,data,header=None,cookie=None,param=None):
        try:
            logger.info('调用delete接口')
            return self.session.delete(url=self.api_root_url+url,json=data,headers=header,cookies=cookie,params=param)
        except Exception as e:
            logger.exception('删除接口调用失败，信息如下：'.format(e))

    def run_main(self, method, url, data, header, cookie=None,params=None):
        try:
            if method.upper() == 'GET':
                result = self.send_get(url, data, header, cookie)
                logger.info('get请求')
                return result
            elif method.upper() == 'POST':
                result = self.send_post(url, data, header, cookie, params)
                logger.info('post请求')
                return result
            elif method.upper() == 'DELETE':
                result = self.send_delete(url, data, header, cookie, params)
                logger.info('delete请求')
                return result
        except Exception as e:
            logger.exception('请求主函数调用失败：{}'.format(e))

