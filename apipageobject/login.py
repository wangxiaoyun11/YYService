import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
def test_login():
    url = "https://idtest.yyuap.com/cas/login"

    querystring = {"service":"https://yesfp.yonyoucloud.com/piaoeda-cloud/cas","isAjax":"true"}

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"tenantCode\"\r\n\r\ndefault\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"username\"\r\n\r\nhhxyonghu@piaoeasy.cn\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"sysid\"\r\n\r\nyonyoueinvoice\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"tenantid\"\r\n\r\n-1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"lt\"\r\n\r\nLT-2-keaMyYygjLPVVU73hsioSirdimkVG5-cas01.example.org\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"_eventId\"\r\n\r\nsubmit\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"tokeninfo\"\r\n\r\n3130f3d0e6b66f52c02bcbc9f38a7359d8b93cebc2da777846a8a63307904e878fe4c9eb03079aa460c053eb0422fce1f56a71978c91ae17e6e2852cca2b2b587c14e2c229691b9c7dae355f64d86a7caafa914386ca96da61c733cfa1615a7db45f27b55eb960368a90a6ac8eeec3c9608458ebe4aa3db64130ee04da1b03a6_encrypted\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"isAutoLogin\"\r\n\r\n0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"randomvalue\"\r\n\r\n1494307679324\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"shaPassword\"\r\n\r\nbfff2dd4f1b310eb0dbf593bd83f94dd8d34077e\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"md5Password\"\r\n\r\naec60231d83fe6cf81444bc536596887\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"validateCode\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"validateKey\"\r\n\r\n1494307694000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-test_data; name=\"yourcasurl\"\r\n\r\nhttps://yesfp.yonyoucloud.com/piaoeda-cloud/cas\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-test_data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "45c6c4e5-4be4-f75e-3f38-ec63e8da4534"

        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    # print(response.text)
    text = response.text
    ticket = re.findall('ticket=(.+?)"}', text)
    print(ticket[0])
    if response.status_code == 200:
        print("登录获取ticket成功")

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
