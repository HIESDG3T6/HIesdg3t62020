# ------ ----- ----- ----- ----- ----- ----- PayPal API ------ ----- ----- ----- ----- ----- ----- 
import paypalrestsdk
from paypalrestsdk import Payout, ResourceNotFound
from paypalrestsdk import Invoice


paypalrestsdk.configure({
    ## merchant
  "mode": "sandbox", # sandbox or live
  "client_id": "AQ9P1S3pslwO9fKMgTc3w_AiXokPpSoTxkhyzAiKxytWttgPQGNpG-rccXLHlMWincbPT9ORlhBiOPl9",
  "client_secret": "EGJvzrlNRwLVBD9am3XJm1RUx__JO6QHhdebmOM-E0bUURCuC6ZgiJ6XeC4NKu4mHCmQWNz0RtTj_dFZ" })

# ------ ----- ----- ----- ----- ----- ----- Refund microservices AMQP ------ ----- ----- ----- ----- ----- ----- 

import json
import sys
import os
import random
import datetime


import pika


#for postman checking : stripe_base_url = 'https://api.stripe.com'

hostname = '172.17.0.2' # need to install the rabbitmq images (from docker), then get the container's ip address
port = 5672 
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
# Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
# If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
channel = connection.channel()
# set up the exchange if the exchange doesn't exist
exchangename="claim_direct"
channel.exchange_declare(exchange=exchangename, exchange_type='direct')

def receiveClaim():

    # prepare a queue for receiving messages
    channelqueue = channel.queue_declare(queue="refund", durable=True) # 'durable' makes the queue survive broker restarts so that the messages in it survive broker restarts too
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='refund.claim') # bind the queue to the exchange via the key

    # set up a consumer and start to wait for coming messages
    channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    channel.start_consuming() # an implicit loop waiting to receive messages; it doesn't exit by default. Use Ctrl+C in the command window to terminate it.



def callback(channel, method, properties, body): # required signature for the callback; no return
    print("Received an claim log by " + __file__)
    print("Claim Details:")
    print(json.loads(body))
    print() # print a new line feed
    # reply the insurance_claim
    print("Refunding Now...")
    ##result = createRefund(json.loads(body))
    result = create_payment(json.loads(body))
    print(result)

    # prepare the reply message and send it out
    replymessage = json.dumps(result, default=str) # convert the JSON object to a string
    replyqueuename="refund.reply"
    
    channel.queue_declare(queue=replyqueuename, durable=True) 
    channel.queue_bind(exchange=exchangename, queue=replyqueuename, routing_key=replyqueuename)

    channel.basic_publish(exchange=exchangename,
            routing_key=properties.reply_to, # use the reply queue set in the request message as the routing key for reply messages
            body=replymessage, 
            properties=pika.BasicProperties(delivery_mode = 2, # make message persistent (stored to disk, not just memory) within the matching queues; default is 1 (only store in memory)
                correlation_id = properties.correlation_id, # use the correlation id set in the request message
            )
    )
    channel.basic_ack(delivery_tag=method.delivery_tag) # acknowledge to the broker that the processing of the request message is completed



""" def createRefund(claim):

    stripe.api_key = 'sk_test_cO2Ogpe9pGbxUkPX7XT4608p00VqIxakqr'

    ''' later need to change the payment_intent from payment'''
    #create a refund data ; must specify a Charge or a PaymentIntent object
    try:
        response = stripe.Refund.create(payment_intent="pi_1GOxccFFJtJhKnRrJ2nYe8XM")
    except:
        # using test refund json response
        with open('refund.json') as refund_json_file:
            response = json.load(refund_json_file)
        refund_json_file.close()

    if response['status'] == 'succeeded':
        # if the refund is success => notify the admin and patient
        # admin side => use the reply queue 
        message = {'status':response['status'],'message':'Simulation of refund response','claim':claim}
    
    return message
 """
# ------ ----- ----- ----- ----- ----- ----- PayPal API + FLASK ------ ----- ----- ----- ----- ----- ----- 
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app=Flask(__name__)

CORS(app)

  
# for refund
def create_payment(claimbody):
    claim_id = claimbody['ClaimID']
    amount = claimbody['ClaimedAmount']

    status = 201
    result = {}
    print("1")
    #retrieve information  about payment and payment items from the request
    print("2")
    paypalrestsdk.configure({
    ## merchant
        "mode": "sandbox", # sandbox or live
        "client_id": "AQ9P1S3pslwO9fKMgTc3w_AiXokPpSoTxkhyzAiKxytWttgPQGNpG-rccXLHlMWincbPT9ORlhBiOPl9",
        "client_secret": "EGJvzrlNRwLVBD9am3XJm1RUx__JO6QHhdebmOM-E0bUURCuC6ZgiJ6XeC4NKu4mHCmQWNz0RtTj_dFZ" })
    print("3")
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:3000/refund/execute",
            "cancel_url": "http://localhost:3000/"
        },
        "transactions": [
            {
                "item_list": {
                    "items": [
                        {
                            "name":claim_id,
                            "sku": "per claim",
                            "price": amount,
                            "currency": "SGD",
                            "quantity":1
                        }
                    ]
                },
                "amount": {
                    "total": amount,
                    "currency": "SGD"
                },
                "description": "refund description"
            }
        ]  
    })
    print("4")
    if payment.create():
        print("5")
        print(payment)
        try:
            #authorize the payment
            for link in payment.links:
                print("6")
                if link.rel=='approval_url':
                # Convert to str to avoid google appengine unicode issue
                # https://github.com/paypal/rest-api-sdk-python/pull/58
                    print("7")
                    approval_url = str(link.href)
                    print("Redirect for approval: %s" % (approval_url))
            status=200
            message="The payment has been created"
            result={'status':status,"message":message,"approval_url":approval_url,"claimid":claim_id}
            # parsed=urlparse(approval_url)
            # ppid=parse_qs(parsed.query).get('paymentId')[0]
            # print(ppid)
            return result

        except:
            status=500
    else:
        print("e")
        print(payment.error)
        result = {'status':500, "message":"An error occurred when creating the payment", "error":str(payment.error)}
    return result




if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is " + os.path.basename(__file__) + ": processing refund to customer...")
    receiveClaim()
    

