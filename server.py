from flask import Flask
from flask import request
import api
import json

app = Flask(__name__)

messages = {}

@app.route("/write", methods=['POST'])
def write_message():
    data = json.loads(request.json['json_payload'])
    key = data['from'] + "_" + data['to']

    messages[key] = data['msg']
    print(messages)

    return api.success()

@app.route("/get/<user>", methods=['GET'])
def get_messages(user):

    print(user)

    return api.send_json({x: messages[x] for x in messages if user == x.split('_')[1]})

app.run(host='0.0.0.0')
