import json
import sys
import os
import random
import datetime

# Communication patterns:
# Use a message-broker with 'direct' exchange to enable interaction
import pika
import uuid
import csv

# ------ ----- ----- ----- ----- ----- ----- insurance claim microservices HTTP ------ ----- ----- ----- ----- ----- ----- 
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


@app.route("/claims/<string:ClaimID>/", methods=['POST'])
def update_claimstatus(ClaimID):
    claim = Insurance_Claim.query.filter_by(ClaimID=ClaimID).first()
    data = request.get_json()
    claim.RefundStatus = data["RefundStatus"]
    try:
        db.session.commit()
        claim = Insurance_Claim.query.filter_by(ClaimID=ClaimID).first()
        send_claim(claim)
    except:
        return jsonify({"message": "An error occurred updating the insurance claim."}),500
    return jsonify(claim.json()),201



@app.route("/claims/<string:ClaimID>")
def find_by_ClaimID(ClaimID):
    claim = Insurance_Claim.query.filter_by(ClaimID=ClaimID).first()

    if claim:
        return jsonify(claim.json())
    return jsonify({"message": "Insurance Claim not found."}), 404




# ------ ----- ----- ----- ----- ----- ----- insurance claim microservices AMQP ------ ----- ----- ----- ----- ----- ----- 



""" If the claim is just approved by the agent, use this function"""
""" should be used in update_claim status? """ 
def send_claim(claim):
    
    """inform Refund MS as needed"""
    # default username / password to the borker are both 'guest'
    hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
    port = 5672 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
        # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
        # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
    channel = connection.channel()

    exchangename="claim_direct"
    channel.exchange_declare(exchange=exchangename, exchange_type='direct')


    message = json.dumps(claim, default=str) # convert a JSON object to a string



    # if the claim is approved and open => notify refund service
    if claim.RefundStatus == "Approved" and claim.ClaimStatus == "Open":

        # Prepare the correlation id and reply_to queue and do some record keeping
        
        corrid = str(uuid.uuid4())
        row = {"claim_id": claim.ClaimID, "correlation_id": corrid}
        csvheaders = ["claim_id", "correlation_id", "status"]
        with open("corrids.csv", "a+", newline='') as corrid_file: # 'with' statement in python auto-closes the file when the block of code finishes, even if some exception happens in the middle
            csvwriter = csv.DictWriter(corrid_file, csvheaders)
            csvwriter.writerow(row)
        replyqueuename = "refund.reply"

        # prepare the channel and send a message to Refund
        

        channel.queue_declare(queue='refund', durable=True) # make sure the queue used by Refund exist and durable
        channel.queue_bind(exchange=exchangename, queue='refund', routing_key='refund.order') # make sure the queue is bound to the exchange

        channel.basic_publish(exchange=exchangename, routing_key="refund.order", body=message,
            properties=pika.BasicProperties(delivery_mode = 2, # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange, which are ensured by the previous two api calls)
                reply_to=replyqueuename, # set the reply queue which will be used as the routing key for reply messages
                correlation_id=corrid # set the correlation id for easier matching of replies
            )
        )
        print("Claim sent to refund service.")
    
    # close the connection to the broker
    connection.close()




if __name__ == '__main__':
    app.run(port=5000, debug=True)


