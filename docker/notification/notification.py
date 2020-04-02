from flask import Flask, request, jsonify
from flask_cors import CORS

import requests
import time

app = Flask(__name__)

CORS(app)

@app.route("/telegramNotification/<string:TelegramHandle>/<string:errorMsg>")
@app.route("/telegramNotification/<string:TelegramHandle>/<string:appointmentDate>/<string:appointmentTime>/<string:clinicName>")
def sendTelegramNoti(TelegramHandle, appointmentDate=None, appointmentTime=None, clinicName=None, errorMsg=None):
    getChatID = "http://172.17.0.2:4646/telegram/getChatID/" + TelegramHandle
    sendToChat = "http://172.17.0.2:4646/telegram/sendMessage/"

    result = requests.get(getChatID).json()
    chatID = str(result['message'])

    if (errorMsg != None):
        sendToChat += chatID + "/" + errorMsg

    else:
        sendToChat += chatID + "/" + appointmentDate + "/" + appointmentTime + "/" + clinicName

    sendResult = requests.get(sendToChat)

    print(sendResult)

    return sendResult

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5566, debug=True)
