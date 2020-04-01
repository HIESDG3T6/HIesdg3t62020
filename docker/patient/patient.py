from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import update
from os import environ

# # Communication patterns:
# # Use a message-broker with 'direct' exchange to enable interaction
# # Use a reply-to queue and correlation_id to get a corresponding reply
# import pika
# # If see errors like "ModuleNotFoundError: No module named 'pika'", need to
# # make sure the 'pip' version used to install 'pika' matches the python version used.
# import uuid
# import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Patient(db.Model):
    __tablename__ = 'Patient'

    patientid = db.Column(db.VARCHAR(255), primary_key=True)
    patientname = db.Column(db.VARCHAR(255), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=True) #for when patient wants to use tele, should we make nullable?
    telehandle = db.Column(db.VARCHAR(100), nullable=True)
    policynum = db.Column(db.VARCHAR(1000), nullable=False)
    username = db.Column(db.VARCHAR(1000), nullable=False)
    pw = db.Column(db.VARCHAR(1000), nullable=False)

    def __init__(self, patientid, patientname, email, telehandle, policynum, username, pw):
        self.patientid = patientid
        self.patientname = patientname
        self.email = email
        self.telehandle = telehandle
        self.policynum = policynum
        self.username = username
        self.pw = pw

    def json(self):
        return {"patientid": self.patientid, "patientname": self.patientname, "email": self.email, "telehandle": self.telehandle, "policynum": self.policynum, "username": self.username, "pw": self.pw}

@app.route("/patient")
def get_all():
	return jsonify({"patients": [patient.json() for patient in Patient.query.all()]})

@app.route("/patient/<string:patientid>")
def find_by_patientid(patientid):
    patient = Patient.query.filter_by(patientid=patientid).first()
    if patient:
        return jsonify(patient.json())
    return jsonify({"message": "Patient not found."}), 404

@app.route("/patient/login/<string:username>")
def find_by_username(username):
    patient = Patient.query.filter_by(username=username).first()
    if patient:
        return jsonify(patient.json())
    return jsonify({"message": "Patient not found."}), 404

@app.route("/patient/<string:patientid>", methods=['POST'])
def create_patient(patientid):
    if (Patient.query.filter_by(patientid=patientid).first()):
        return jsonify({"message": "A patient with PatientID '{}' already exists.".format(patientid)}), 400

    data = request.get_json()
    patient = Patient(patientid, **data)

    try:
        db.session.add(patient)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating patient."}), 500

    return jsonify(patient.json()), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)