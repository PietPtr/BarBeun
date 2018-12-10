from flask import Flask
from flask import request
import api

app = Flask(__name__)

messages = {}

@app.route("/write", methods=['POST'])
def write_message():
    key = request.json['from'] + "_" + request.json['to']

    messages[key] = request.json['msg']
    print(messages)

    return api.success()

@app.route("/get/<user>", methods=['GET'])
def get_messages(user):

    print(user)

    return api.send_json({x: messages[x] for x in messages if user == x.split('_')[1]})

app.run()
