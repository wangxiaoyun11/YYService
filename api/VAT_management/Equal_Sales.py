import urllib3
import json
from core.rest_client import BasicRequest
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class EqualSales(BasicRequest):
    def __init__(self):
        super(EqualSales, self).__init__()

    def add(self,user):
        url = 'https://yesfp.yonyoucloud.com/output-tax/equivalent-sale/add'
        payload = {"orgid":"1054","abstr":user,"taxMethod":"1","saleClassification":"1","je":"1090","se":"185.30","jshj":"1275.30","billdate":"2021-02-04","slv":"0.17"}
        headers = {
            'content-type': "application/json"
        }
        request = self.post(url=url, json=payload, headers=headers)
        return request

    def query(self,user):
        url = 'https://yesfp.yonyoucloud.com/output-tax/equivalent-sale/query'
        querystring = {"pagenum": "1", "pagesize": "15", "sortby":"billdate", "order":"desc"}
        payload ={"keyword":user}
        headers = {
            'content-type': "application/json"
        }
        request = self.post(url=url, json=payload, headers=headers,params=querystring)
        return request

    def deletes(self,id):
        url = 'https://yesfp.yonyoucloud.com/output-tax/equivalent-sale/delete'
        querystring = {"id": id, "_": "1612407504529"}
        headers = {
            'content-type': "application/json"
        }
        request = self.get(url=url, headers=headers,params=querystring)
        return request


