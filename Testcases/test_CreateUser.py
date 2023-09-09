import requests
import json
import jsonpath
import pprint

url = "https://reqres.in/api/users"

def test_create_new_user():
    #read input from json file
    file = open("/home/rhythmic/Downloads/RestApiNew/CreateUser.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    response = requests.post(url,request_json)

    assert response.status_code == 201

    print(response.headers.get("Content-Length"))

    response_json = json.loads(response.text)

    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])
    # pprint.pprint(response.content)

def test_create_other_user():
    #read input from json file
    file = open("/home/rhythmic/Downloads/RestApiNew/CreateUser.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    response = requests.post(url,request_json)

    assert response.status_code == 201

    print(response.headers.get("Content-Length"))

    response_json = json.loads(response.text)

    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])
    # pprint.pprint(response.content)