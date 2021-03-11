import urllib3
from base.base_request import BasicRequest
from common.read_config import ReadConfig
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pytest
from common.handle_yaml import Read_Yaml

class Homepage(BasicRequest):
    def __init__(self):
        super(Homepage, self).__init__()

    def query(self, user,url):
        querystring = {"pagenum": "1", "pagesize": "15"}
        data = {"keyword":user}
        headers = {
            'content-type': "application/json"
        }
        request = self.run_main(method='post',url=url, data=data, header=headers,params=querystring)
        return request

    def query2(self, url, querystring, user, headers):
        data = {"keyword": user}
        request = self.run_main(method='post', url=url, data=data, header=headers, params=querystring)
        return request

