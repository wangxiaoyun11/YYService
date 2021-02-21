import urllib3

from base.base_request import BasicRequest

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Homepage(BasicRequest):

    def get_token(self):
        return self.session

    def list(self):
        pass

    def query(self,user):
        url = 'https://yesfp.yonyoucloud.com/bd/employee/vaguequery'
        querystring = {"pagenum": "1", "pagesize": "15"}
        payload = {"keyword":user}
        headers = {
            'content-type': "application/json"
        }
        request = self.post(url=url, json=payload, headers=headers,params=querystring)
        return request

