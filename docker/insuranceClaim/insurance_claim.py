import json
import sys
import os
import random
import datetime
import requests

# Communication patterns:
# Use a message-broker with 'direct' exchange to enable interaction
import pika
import uuid
import csv

# ------ ----- ----- ----- ----- ----- ----- insurance claim microservices HTTP ------ ----- ----- ----- ----- ----- ----- 
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Insurance_Claim(db.Model):
    __tablename__ = 'insurance_claim'

    ClaimID = db.Column(db.Integer, nullable=True,primary_key=True)
    PatientID = db.Column(db.String(64),nullable=False)
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

@app.route("/claims/create/", methods=['POST'])
def create_claim():
    # When adding data to the database, the ClaimDate format will be '2020-01-30 14:01:00'
    # When you use get to get the data from database, the ClaimDate format 'Mon, 27 Jan 2020 12:01:00 GMT'
    data = request.get_json()
    claim = Insurance_Claim(**data)
   
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
        
    except:
        return jsonify({"message": "An error occurred updating the insurance claim."}),500
    send_claim(claim.json())

    return jsonify(claim.json()),201
    #return jsonify(claim.json()),201



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
    # print(message)


    # if the claim is approved and open => notify refund service
    if claim['RefundStatus'] == "Approved" and claim['ClaimStatus'] == "Open":

        # Prepare the correlation id and reply_to queue and do some record keeping
        # Keep the corrid into refund table under claim database
        
        corrid = str(uuid.uuid4())
        row = {"ClaimID": claim['ClaimID'], "reply_Status": "none", "Approval_url": "none"}
        headers={"content-type": "application/json"}
        
        service_url = "http://127.0.0.1:5001/refund/"+corrid

        r = requests.post(service_url, json=row, headers=headers)
        #print(r.text)
        print('post corrid')
        print(corrid)
        
    
        # prepare the channel and send a message to Refund
        replyqueuename = "refund.reply"


        channel.queue_declare(queue='refund', durable=True) # make sure the queue used by Refund exist and durable

        channel.queue_bind(exchange=exchangename, queue='refund', routing_key='refund.claim') # make sure the queue is bound to the exchange

        channel.basic_publish(exchange=exchangename, routing_key="refund.claim", body=message,
            properties=pika.BasicProperties(delivery_mode = 2, # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange, which are ensured by the previous two api calls)
                reply_to=replyqueuename, # replyqueuename set the reply queue which will be used as the routing key for reply messages 
                correlation_id=corrid # set the correlation id for easier matching of replies
            )
        )
        print("Claim sent to refund service.")
    
    # close the connection to the broker
    connection.close()
    receiveReply()


# receive the reply from refund.reply
def receiveReply():

    # default username / password to the borker are both 'guest'
    hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
    port = 5672 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
        # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
        # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
    channel = connection.channel()

    exchangename="claim_direct"
    channel.exchange_declare(exchange=exchangename, exchange_type='direct')


    # prepare a queue for receiving messages
    channelqueue = channel.queue_declare(queue="refund.reply", durable=True) # 'durable' makes the queue survive broker restarts so that the messages in it survive broker restarts too
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='refund.reply') # bind the queue to the exchange via the key

    # set up a consumer and start to wait for coming messages
    channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    channel.basic_consume(queue=queue_name, on_message_callback=reply_callback)
    channel.start_consuming()
    
def reply_callback(channel, method, properties, body): 
    print("Received an reply from Refund Service: ")
    print(body)
    reply = json.loads(body)
    
    print("reply corrid is")
    print(properties.correlation_id)

    #after receive the message, stop the loop
    headers={"content-type": "application/json"}

    channel.basic_ack(delivery_tag=method.delivery_tag)
    channel.stop_consuming()
    
    update_url = 'http://127.0.0.1:5001/refund/'+properties.correlation_id +'/'

    r = requests.post(update_url, json=reply, headers=headers)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003, debug=True)


