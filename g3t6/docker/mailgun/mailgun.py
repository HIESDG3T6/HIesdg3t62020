from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from os import environ

import json
import pika
import datetime
import json
from datetime import date

app = Flask(__name__)
CORS(app)


def send_alert_message(info):
	return requests.post(
        "https://api.mailgun.net/v3/sandbox2ba83bb738204aa1ace26f86872c85d7.mailgun.org/messages",
        auth=("api", <APIKEY>),
        data={"from": "Alert admin <postmaster@sandbox2ba83bb738204aa1ace26f86872c85d7.mailgun.org>",
        "to": "Jon <jonathanlee.2018@smu.edu.sg>",
            "subject": "Appointment confirmed",
            "template": "alert",
            "h:X-Mailgun-Variables": info})


def send_billing_message(info):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox2ba83bb738204aa1ace26f86872c85d7.mailgun.org/messages",
		auth=("api", <APIKEY>),
		data={"from": "Mailgun Sandbox <postmaster@sandbox2ba83bb738204aa1ace26f86872c85d7.mailgun.org>",
			"to": "jiamin <jonathanlee.2018@smu.edu.sg>",
			"subject": "Billing - for your immediate attention",
			"template": "billing",
			"h:X-Mailgun-Variables": info})

@app.route("/appointmentemail", methods=['POST'])
def send_appt_email():
    status = 201

    email_input = request.json
    


    customerID = email_input['customerID']
    clinicID = email_input['clinicID']
    doctorID = email_input['doctorID']
    appointmentDate = email_input['appointmentDate']
    appointmentTime = email_input['appointmentTime']
    
    data = {"name": customerID, "date": appointmentDate, "time": appointmentTime, "clinic": clinicID}
    info = json.dumps(data)
    send_alert_message(info)
    return 'OK'


@app.route("/paymentemail", methods=["POST"])
def send_pay_email():
    status = 201

    pay_email_input = request.json

    AID = str(pay_email_input['AID'])
    Medication = pay_email_input['Medication']
    BillAmount = str(pay_email_input['BillAmount'])
    ClaimAmount = str(pay_email_input['ClaimAmount'])

    today = date.today()
    today = today.strftime("%d/%m/%Y")

    data = {"aid": AID, "date": today, "bill": BillAmount, "claim": ClaimAmount, "medication": Medication}
    info = json.dumps(data)
    send_billing_message(info)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)