from api import login
import urllib3
from core.rest_client import RestClient
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

    url = 'https://yesfp.yonyoucloud.com/bd/employee/vaguequery'
    querystring = {"pagenum": "1", "pagesize": "15"}
    payload = "{'keyword':'南志姣'}"
    headers = {
        'content-type': "application/json"
    }
    reaa = RestClient().post(url=url,data=payload,headers=headers)
    print(reaa)


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def home_page_query(self, **kwargs):
        return self.post("/bd/employee/vaguequery", **kwargs)

    def home_page_queryw(self, username, **kwargs):
        return self.get("/users/{}".format(username), **kwargs)

    def register(self, **kwargs):
        return self.post("/register", **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

    def update(self, user_id, **kwargs):
        return self.put("/update/user/{}".format(user_id), **kwargs)

    def delete(self, name, **kwargs):
        return self.post("/delete/user/{}".format(name), **kwargs)