from pageobject import login
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class homepage:
    def __init__(self):
        self.session = login.test_login()

    def get_token(self):
        return self.session


    def list(self):
        pass

    def query(self):
        url = 'https://yesfp.yonyoucloud.com/bd/employee/vaguequery'
        querystring = {"pagenum": "1", "pagesize": "15"}
        payload = "{'keyword':'南志姣'}"
        headers = {
            'content-type': "application/json"
        }
        request = self.session.post(url=url, data=payload.encode(), headers=headers,params=querystring)
        return request
