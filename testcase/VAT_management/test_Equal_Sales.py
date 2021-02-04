import pytest
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@pytest.mark.parametrize("user", ["18221124104","1111","22222"])
def test_homepage_query():

    assert request.status_code==200
    assert request.json()['code']== "0000"