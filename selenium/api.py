from requests import request
from json import loads,dumps
def test_log():
    url = "https://reqres.in/api/login"
    payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
              }
    response = request("POST", url, json=payload)
    print(response.status_code)
    assert response.status_code == 200
    json_string = response.text
    print(json_string)
    json_object = loads(json_string)
    print(json_object)
    actual_token =  json_object['token']
    assert actual_token ==  "QpwL5tke4Pnpja7X4"
