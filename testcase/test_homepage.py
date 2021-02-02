from pageobject import login
from pageobject.HomePage import homepage
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_homepage_query():
    home=homepage()
    request = home.query()
    assert request.status_code==200
    assert request.json()['code']== "0000"
