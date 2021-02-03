# coding=utf-8
import requests
import json
class RestClient():
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

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

    def request(self, url, method, data=None, jsons=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(url, method, data, jsons, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)

        if method == "POST":
            return self.session.post(url, data, jsons, **kwargs)

        if method == "PUT":
            if jsons:
            #  PUT 和 PATCH # json 参数直接自动传 json  #传 data 参数就需要传 json
                data = json.dumps(jsons)
            return self.session.put(url, data, **kwargs)

        if method == "DELETE":
            return self.session.delete(url, **kwargs)

        if method == "PATCH":
            if jsons:
                data = json.dumps(jsons)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data, jsons, params, headers, files, cookies):
        print(url, method, data, jsons, params, headers, files, cookies)