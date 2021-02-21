import pytest
import urllib3
from apipageobject.VAT_management.Equal_Sales import EqualSales
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@pytest.mark.parametrize("user", ["18221124104","1111","22222"])
def test_homepage_add(user):
    test = EqualSales()
    request = test.add(user)
    assert request.status_code==200
    assert request.json()['code']== "0000"

@pytest.mark.parametrize("user", ["18221124104","1111","22222"])
def test_homepage_query(user):
    test = EqualSales()
    request = test.query(user)
    assert request.status_code==200
    assert request.json()['code']== "0000"