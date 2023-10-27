import pytest, json

@pytest.fixture()
def checkReturnJson():
    return { "hello": "world" }

def testRequestExample(client, checkReturnJson):
    response = client.get("/")
    resData = json.loads(response.data)
    resHttpCode = response.status_code
    
    assert checkReturnJson == resData
    assert resHttpCode == 200
