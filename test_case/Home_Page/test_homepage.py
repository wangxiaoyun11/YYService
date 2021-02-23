import pytest
from apipageobject.Home_Page.HomePage import Homepage
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.parametrize("user", ["18221124104","1111","22222"])
def test_homepage_query(user):
    home = Homepage()
    request = home.query(user)
    assert request.status_code==200
    assert request.json()['code']== "0000"

