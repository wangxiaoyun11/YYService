import urllib3
from base.base_request import BasicRequest
from common.read_config import ReadConfig
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Homepage(BasicRequest):
    def __init__(self):
        super(Homepage, self).__init__()

    def query(self,user):
        url = 'https://yesfp.yonyoucloud.com/' + "input-tax/reimbursement-account/query"
        querystring = {"pagenum": "1", "pagesize": "15"}
        payload = {"keyword":user}
        headers = {
            'content-type': "application/json"
        }
        request = self.run_main(method='post',url=url, data=payload, header=headers,params=querystring)
        return request
