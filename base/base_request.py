# coding=utf-8
from common.handle_log import run_log as logger
from apipageobject import login
from common.read_config import ReadConfig

class BasicRequest(object):

    def __init__(self):
        # READ = ReadConfig()
        # self.api_root_url = READ.get_value(key='url',node='pre')
        self.session = login.test_login()

    def send_get(self,url,data=None,header=None,cookie=None):
        return self.session.get(url=url,params=data,headers=header,cookies=cookie)

    def send_post(self,url,data,header=None,cookie=None,param=None):
        return self.session.post(url=url,json=data,headers=header,cookies=cookie,params=param)

    def send_delete(self,url,data,header=None,cookie=None,param=None):
        return self.session.delete(url=url,json=data,headers=header,cookies=cookie,params=param)

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

