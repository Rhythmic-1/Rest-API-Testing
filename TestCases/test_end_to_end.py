import requests
import json
import jsonpath

def test_Post_user_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    f=open('data.json','r')
    request_json=json.loads(f.read())
    # print(request_json)
    response=requests.post(API_URL,request_json)
    # print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    # print(id[0])