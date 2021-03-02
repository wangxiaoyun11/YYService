import pytest
from apipageobject.Home_Page.HomePage import Homepage
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from base.base_request import BasicRequest
from common.handle_yaml import Read_Yaml

@pytest.mark.parametrize("user", ["18221124104","1111","22222"])
def test_homepage_query(user):
    home = Homepage()
    request = home.query(user)
    print(request.text)
    assert request.status_code==200
    assert request.json()['code']== "0000"
# 直接调用request基类

@pytest.mark.parametrize(
    'url,querystring,headers,data', [[Read_Yaml().get_url(),Read_Yaml().get_querystring(),Read_Yaml().get_headers(),Read_Yaml().get_data()]])
def test_homepage_query3(url, querystring, data, headers):
    home = BasicRequest()
    request = home.send_post(url=url, data=data, header=headers, param=querystring)
    assert request.status_code == 200
    assert request.json()['code'] == "0000"

# 调用po
# @pytest.mark.parametrize(
#     'url,querystring,headers,data', [[Read_Yaml().get_url(),Read_Yaml().get_querystring(),Read_Yaml().get_headers(),Read_Yaml().get_data()]])
# def test_homepage_query3(url, querystring, data, headers):
#     home = Homepage()
#     request = home.query2(url, querystring, data, headers)
#     assert request.status_code == 200
#     assert request.json()['code'] == "0000"