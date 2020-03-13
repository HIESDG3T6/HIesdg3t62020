# insurance claim microservices HTTP
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/insurance_claim'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Insurance_Claim(db.Model):
    __tablename__ = 'insurance_claim'

    ClaimID = db.Column(db.Integer, nullable=False,primary_key=True)
    PatientID = db.Column(db.Integer,nullable=False)
    ClinicName = db.Column(db.String(64),nullable=False)
    
    ClaimDate = db.Column(db.DateTime,nullable=False)
    Medicine = db.Column(db.String(640))
    BillAmount = db.Column(db.Float(precision=2), nullable=False)
    ClaimedAmount = db.Column(db.Float(precision=2), nullable=False)
    
    ClaimStatus = db.Column(db.String(64), nullable=False)
    RefundStatus = db.Column(db.String(64), nullable=False)



    def __init__(self, ClaimID, PatientID, ClinicName, ClaimDate,Medicine,BillAmount,ClaimedAmount,ClaimStatus,RefundStatus):
        self.ClaimID = ClaimID
        self.PatientID = PatientID
        self.ClinicName = ClinicName
        self.ClaimDate = ClaimDate
        self.Medicine = Medicine
        self.BillAmount = BillAmount
        self.ClaimedAmount = ClaimedAmount
        self.ClaimStatus = ClaimStatus
        self.RefundStatus = RefundStatus
    # return an insurance item as a JSON object
    def json(self):
        
        return {
            'ClaimID': self.ClaimID, 'PatientID': self.PatientID, 'ClinicName': self.ClinicName, 
            'ClaimDate': self.ClaimDate, 'Medicine': self.Medicine, 'BillAmount': self.BillAmount, 
            'ClaimedAmount': self.ClaimedAmount,'ClaimStatus': self.ClaimStatus, 'RefundStatus': self.RefundStatus}

@app.route("/claims")
def get_all():
    return jsonify({"insurance_claims": [claims.json() for claims in Insurance_Claim.query.all()]})

@app.route("/claims/<string:ClaimID>", methods=['POST'])
def create_claim(ClaimID):
    if (Insurance_Claim.query.filter_by(ClaimID=ClaimID).first()):
        return jsonify({"message": "An insurance claim with ClaimID '{}' already exists.".format(ClaimID)}), 400
    # When adding data to the database, the ClaimDate format will be '2020-01-30 14:01:00'
    # When you use get to get the data from database, the ClaimDate format 'Mon, 27 Jan 2020 12:01:00 GMT'
    data = request.get_json()
    claim = Insurance_Claim(ClaimID, **data)
   
    try:
        db.session.add(claim)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the insurance claim."}), 500

    return jsonify(claim.json()), 201


@app.route("/claims/<string:ClaimID>")
def find_by_ClaimID(ClaimID):
    claim = Insurance_Claim.query.filter_by(ClaimID=ClaimID).first()
    if claim:
        return jsonify(claim.json())
    return jsonify({"message": "Insurance Claim not found."}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    



# insurance claim microservices AMQP

import json
import sys
import os
import random
import datetime

import pika
import uuid

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Claim(Base):
    __tablename__ = 'insurance_claim'
    ClaimID = Column(String, nullable=False,primary_key=True)
    PatientID = Column(String,nullable=False)
    ClinicName = Column(String,nullable=False)
    
    ClaimDate = Column(String,nullable=False)
    Medicine = Column(String(640))
    BillAmount = Column(String, nullable=False)
    ClaimedAmount = Column(String, nullable=False)
    
    ClaimStatus = Column(String(64), nullable=False)
    RefundStatus = Column(String(64), nullable=False)


    def __init__(self, ClaimID, PatientID, ClinicName, ClaimDate,Medicine,BillAmount,ClaimedAmount,ClaimStatus,RefundStatus):
        self.ClaimID = ClaimID
        self.PatientID = PatientID
        self.ClinicName = ClinicName
        self.ClaimDate = ClaimDate
        self.Medicine = Medicine
        self.BillAmount = BillAmount
        self.ClaimedAmount = ClaimedAmount
        self.ClaimStatus = ClaimStatus
        self.RefundStatus = RefundStatus

    # return an insurance item as a JSON object
    def json(self):
        return {
            'ClaimID': self.ClaimID, 'PatientID': self.PatientID, 'ClinicName': self.ClinicName, 
            'ClaimDate': self.ClaimDate, 'Medicine': self.Medicine, 'BillAmount': self.BillAmount, 
            'ClaimedAmount': self.ClaimedAmount,'ClaimStatus': self.ClaimStatus, 'RefundStatus': self.RefundStatus}


#connect to mysql database mamp's psw is root, if using windows, pls remove the psw
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/insurance_claim')
DBSession = sessionmaker(bind=engine)

# instantiate a session
""" session = DBSession()
claims = session.query(Claim).all()
for each in claims:
    print('name:',each.ClinicName)
print(claims) """


