from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import update

import requests
import time

app = Flask(__name__)

CORS(app)

@app.route("/telegramNotification/<string:TelegramHandle>/<string:errorMsg>")
@app.route("/telegramNotification/<string:TelegramHandle>/<string:appointmentDate>/<string:appointmentTime>/<string:clinicName>")
def sendTelegramNoti(TelegramHandle, appointmentDate=None, appointmentTime=None, clinicName=None, errorMsg=None):
    getChatID = "http://localhost:4646/telegram/getChatID/" + TelegramHandle
    sendToChat = "http://localhost:4646/telegram/sendMessage/"

    result = requests.get(getChatID).json()
    chatID = str(result['message'])

    if (errorMsg != None):
        sendToChat += chatID + "/" + errorMsg

    else:
        sendToChat += chatID + "/" + appointmentDate + "/" + appointmentTime + "/" + clinicName

    sendResult = requests.get(sendToChat).json()

    print(sendResult)

    return sendResult

# @app.route("\notification\email\<string:customerID>/<more>")
    # pass
    # try {
    #     const mailresponse = await fetch (mailURL,
    #         {
    #             method: 'POST',
    #             mode: 'no-cors',
    #             headers: {"Content-Type": "application/json"},
    #             body: JSON.stringify ({
    #                 customerID: customerID, clinicID : clinicID, doctorID : doctorID, 
    #                 appointmentDate : appointmentDate, appointmentTime : appointmentTime
    #                 })
    #         }

            
    #     );

    #     const maildata = await mailresponse.json();

    #     if (!response.ok) {
    #     var msg = maildata['message'];
    #     showError(msg);
    #     } 
    # } catch (error){
    #         console.log(error);
    # } 


if __name__ == '__main__':
    app.run(port=5566, debug=True)
