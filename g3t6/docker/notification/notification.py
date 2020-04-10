from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

import json
import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)


class UserChatID(db.Model):
    __tablename__ = 'UserChatID'

    # NEED TO ADD IN DB.ForeignKey('databasename.columnname')
    TelegramHandle = db.Column(db.String(100), primary_key= True)
    ChatID = db.Column(db.Integer, nullable= False)


    def __init__(self, TelegramHandle, ChatID):
        self.TelegramHandle = TelegramHandle
        self.ChatID = ChatID

    def json(self):
        return {
            "TelegramHandle" : self.TelegramHandle,
            "ChatID" : self.ChatID
        }

@app.route("/telegramNotification/<string:TelegramHandle>/<string:errorMsg>")
@app.route("/telegramNotification/<string:TelegramHandle>/<string:appointmentDate>/<string:appointmentTime>/<string:clinicName>")
def sendTelegramNoti(TelegramHandle, appointmentDate=None, appointmentTime=None, clinicName=None, errorMsg=None):
    getChatID = "http://localhost:5566/telegramNotification/getChatID/" + TelegramHandle
    sendToChat = "http://<dockerIPAddress>:4646/telegram/sendMessage/"

    result = requests.get(getChatID).json()
    chatID = str(result['message'])

    if (errorMsg != None):
        sendToChat += chatID + "/" + errorMsg

    else:
        sendToChat += chatID + "/" + str(appointmentDate) + "/" + str(appointmentTime) + "/" + str(clinicName)

    sendResult = requests.get(sendToChat).json()

    return sendResult

@app.route("/telegramNotification/getChatID/<string:TelegramHandle>")
def getChatID(TelegramHandle):
    chatID = UserChatID.query.filter_by(TelegramHandle = TelegramHandle).first()
    result = "Not Found"

    if chatID:
        result = chatID.json()['ChatID']
        return jsonify({"status": True, "message": result})

    else:
        return jsonify({"status": False, "message": result})


@app.route("/telegramNotification/addChatID/<string:TelegramHandle>/<int:ChatID>")
def addChatID(TelegramHandle, ChatID):
    getChatIDLink = "http://localhost:5566/telegramNotification/getChatID/" + TelegramHandle
    search = requests.get(getChatIDLink).json()

    # return search.json()

    if search['status'] == False:
        chatIDObj = UserChatID(TelegramHandle, ChatID)

        try:
            db.session.add(chatIDObj)
            db.session.commit()
            return jsonify({"status": True, "message": "ChatID is added into the database"})

        except:
            return jsonify({"status": False, "message": "An error occurred creating chatID."})

    else:
        return jsonify({"status": False, "message": "ChatID has been created"})


@app.route("/telegramNotification/update")
def updateNotification():
    getUpdatesLink = "http://<dockerIPAddress>:4646/telegram/getUpdates"

    result = requests.get(getUpdatesLink).json()

    temp = 0

    if (result["status"] == True):
        data = result["message"]

        for object in data:
            # if chatID is NOT in the database then add the teleHandle and ChatID into the database
            print ("here")
            teleHandle = object['message']['from']['username']
            chatID = object['message']['chat']['id']
            temp = object['update_id']

            getChatIDLink = "http://localhost:5566/telegramNotification/getChatID/" + teleHandle

            found = requests.get(getChatIDLink).json()

            if found['status'] == False:
                addChatIDLink = "http://localhost:5566/telegramNotification/addChatID/" + teleHandle + "/" + str(chatID)

                addStatus = requests.get(addChatIDLink)     

    temp+=1

    resetLink = getUpdatesLink + "/" + str(temp)

    try:
        reset = requests.get(resetLink)
        reply = reset.json()

        return jsonify({"message" : reply}),200

    except requests.exceptions.RequestException as e:
        print(e)

        return jsonify({"message":e}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5566, debug=True)
