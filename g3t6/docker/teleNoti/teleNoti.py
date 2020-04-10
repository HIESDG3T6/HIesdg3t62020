from flask import Flask, request, jsonify
from flask_cors import CORS

import json
import datetime
import requests

app = Flask(__name__)
CORS(app)

@app.route("/telegram/getUpdates")
@app.route("/telegram/getUpdates/<string:offset>")
def getUpdates(offset = None):
    getUpdatesLink = "https://api.telegram.org/bot<APIKEY>/getUpdates"

    if offset != None:
        getUpdatesLink += "?offset=" + offset

    try:
        r = requests.get(getUpdatesLink)
        reply = r.json()
        data = reply['result']

        return jsonify({"status": True, "message":data})

    except requests.exceptions.RequestException as e:
        print(e)
        return jsonify({"status":False, "message":e}), 400


@app.route("/telegram/sendMessage/<string:chatID>/<string:errorMsg>")
@app.route("/telegram/sendMessage/<string:chatID>/<string:appointmentDate>/<string:appointmentTime>/<string:clinicName>")
def sendMessage(chatID, appointmentDate=None, appointmentTime=None, clinicName=None, errorMsg=None):
    if (errorMsg != None):
        text = "Hello! There is issue creating your appointment. " + errorMsg

    else:
        text = "Hello! Your appointment at " + clinicName + " on " + appointmentDate + ", " + appointmentTime + " is confirmed. "

    sendMessageLink = "https://api.telegram.org/bot<APIKEY>/sendMessage?chat_id=" + chatID + "&text=" + text

    # return str(sendMessageLink), 200

    try:
        r = requests.get(sendMessageLink)
        
        return jsonify({"status":True, "message": "Message sent"}), 201

    except requests.exceptions.RequestException as e:
        print(e)

        return jsonify({"status":False, "message": e}), 400

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4646, debug=True)

