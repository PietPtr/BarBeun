import requests
import json


def request(requester):
    response = requests.get("http://frozenfire.tk:5000/get/" + requester).content.decode('utf8')
    return json.loads(response)

def write(origin, goal, message):
    data = {'from': origin, 'to': goal, 'msg': message}
    data_json = json.dumps(data)
    payload = {'json_payload': data_json}

    result = requests.post('http://frozenfire.tk:5000/write', json=payload)
    return result
