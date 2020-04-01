from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

import json
import datetime
import requests
import webbrowser

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


@app.route("/telegram/start")
def startTelegram():
    startBotLink = "https://telegram.me/HIesd_bot?start=check-this-out"

    webbrowser.open_new_tab(startBotLink)


@app.route("/telegram/getUpdates")
def getUpdates():
    getUpdatesLink = "https://api.telegram.org/bot945490371:AAEzLBScwecjy55XQUwREN1n6tXCPGF8I0M/getUpdates"

    offsetValue = 0

    try:
        r = requests.get(getUpdatesLink)
        reply = r.json()
        data = reply['result']

        temp = offsetValue

        for object in data:
            # if chatID is NOT in the database then add the teleHandle and ChatID into the database
            print ("here")
            teleHandle = object['message']['from']['username']
            chatID = object['message']['chat']['id']
            temp = object['update_id']

            search = UserChatID.query.filter_by(TelegramHandle = teleHandle).first()

            if not search:
                chatID = UserChatID(teleHandle, chatID )

                try:
                    db.session.add(chatID)
                    db.session.commit()

                except:
                    return jsonify({"message": "An error occurred creating chatID."}), 500

        temp+=1

        resetLink = getUpdatesLink + "?offset=" + str(temp)

        try:
            reset = requests.get(resetLink)
            reply = reset.json()

            return jsonify({"message" : reply}),200

        except requests.exceptions.RequestException as e:
            print(e)

            return jsonify({"message":e}), 400


    except requests.exceptions.RequestException as e:
        print(e)
        return jsonify({"message":e}), 400


@app.route("/telegram/sendMessage/<string:chatID>/<string:errorMsg>")
@app.route("/telegram/sendMessage/<string:chatID>/<string:appointmentDate>/<string:appointmentTime>/<string:clinicName>")
def sendMessage(chatID, appointmentDate=None, appointmentTime=None, clinicName=None, errorMsg=None):
    if (errorMsg != None):
        text = "Hello! There is issue creating your appointment. " + errorMsg

    else:
        text = "Hello! Your appointment at " + clinicName + " on " + appointmentDate + ", " + appointmentTime + " is confirmed. "

    sendMessageLink = "https://api.telegram.org/bot945490371:AAEzLBScwecjy55XQUwREN1n6tXCPGF8I0M/sendMessage?chat_id=" + chatID + "&text=" + text

    # return str(sendMessageLink), 200

    try:
        r = requests.get(sendMessageLink)
        
        return jsonify({"status":True, "message": "Message sent"}), 201

    except requests.exceptions.RequestException as e:
        print(e)

        return jsonify({"status":False, "message": e}), 400


@app.route("/telegram/getChatID/<string:TelegramHandle>")
def getChatID(TelegramHandle):
    chatID = UserChatID.query.filter_by(TelegramHandle = TelegramHandle).first()
    result = "Not Found"

    if chatID:
        result = chatID.json()['ChatID']
        return jsonify({"status": True, "message": result})

    else:
        return jsonify({"status": False, "message": result})
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4646, debug=True)

