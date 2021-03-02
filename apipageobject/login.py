import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
def test_login():
    url = "https://idtest.yyuap.com/cas/login"

    querystring = {"service":"https://yesfp.yonyoucloud.com/piaoeda-cloud/cas","isAjax":"true"}

    payload = {'tenantCode': 'default','username': 'hhxyonghu@piaoeasy.cn','sysid': 'yonyoueinvoice','tenantid': '-1','lt': 'LT-2-keaMyYygjLPVVU73hsioSirdimkVG5-cas01.example.org','_eventId': 'submit','tokeninfo': '3130f3d0e6b66f52c02bcbc9f38a7359d8b93cebc2da777846a8a63307904e878fe4c9eb03079aa460c053eb0422fce1f56a71978c91ae17e6e2852cca2b2b587c14e2c229691b9c7dae355f64d86a7caafa914386ca96da61c733cfa1615a7db45f27b55eb960368a90a6ac8eeec3c9608458ebe4aa3db64130ee04da1b03a6_encrypted','isAutoLogin': '0','randomvalue': '1494307679324','shaPassword': 'bfff2dd4f1b310eb0dbf593bd83f94dd8d34077e','md5Password': 'aec60231d83fe6cf81444bc536596887','validateCode': '','validateKey':'1494307694000','yourcasurl': 'https://yesfp.yonyoucloud.com/piaoeda-cloud/cas'}
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    # print(response.text)
    text = response.text
    ticket = re.findall('ticket=(.+?)"}', text)
    if response.status_code == 200:
        print("登录获取ticket成功")
        print('ticket是：{}'.format(ticket))

    url1 = "https://yesfp.yonyoucloud.com/piaoeda-cloud/cas"
    querystring1 = {"ticket": ticket}
    headers1 = {
        'cache-control': "no-cache",
        'postman-token': "6049b73f-402c-dceb-0844-b9ca99a526db"
        }

    session = requests.session()
    login_response = session.get(url1, headers=headers1, params=querystring1,verify=False)
    if login_response.status_code == 200:
        print("登录成功")
    return session
test_login()