import requests
import json
import jsonpath
import pprint

def test_create_new_user():
    # adding new student and fetch his id
    app_url = "https://thetestingworldapi.com/api/studentsDetails"
    #read input from json file
    file = open("/home/rhythmic/Downloads/RestApiNew/Request.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(app_url,request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    # add technical details
    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    #read input from json file
    file = open("/home/rhythmic/Downloads/RestApiNew/Techdetails.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url,request_json)
    print(response.text)

    #adding addresses and fetching the complete data
    add_api_url = "https://thetestingworldapi.com/api/addresses"
    #read input from json file
    file = open("/home/rhythmic/Downloads/RestApiNew/address.json",'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    request_json['stId'] = id[0]
    response = requests.post(add_api_url,request_json)
    
    final_details = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(final_details)
    pprint.pprint(response.text)