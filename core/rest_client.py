# coding=utf-8
import requests
import json
from api import login


class BasicRequest(object):

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = login.test_login()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, json=None, headers=None,params=None,**kwargs):
        url = self.api_root_url + url
        if method == "GET":
            return self.session.get(url=url,params=params,**kwargs)
        if method == "POST":
            return self.session.post(url=url, json=json,headers=headers,**kwargs)
        if method == "DELETE":
            return self.session.delete(url=url, **kwargs)
        if method == "PUT":
            if json:
                #  PUT 和 PATCH # json 参数直接自动传 json  #传 data 参数就需要传 json
                data = json.dumps(json)
            return self.session.put(url=url, data=data, **kwargs)
        if method == "PATCH":
            if json:
                data = json.dumps(json)
            return self.session.patch(url=url, data=data, **kwargs)

