import paypalrestsdk
from paypalrestsdk import Payout, ResourceNotFound
from paypalrestsdk import Invoice


paypalrestsdk.configure({
    ## merchant
  "mode": "sandbox", # sandbox or live
  "client_id": "AQ9P1S3pslwO9fKMgTc3w_AiXokPpSoTxkhyzAiKxytWttgPQGNpG-rccXLHlMWincbPT9ORlhBiOPl9",
  "client_secret": "EGJvzrlNRwLVBD9am3XJm1RUx__JO6QHhdebmOM-E0bUURCuC6ZgiJ6XeC4NKu4mHCmQWNz0RtTj_dFZ" })



from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
import pika


app=Flask(__name__)

CORS(app)

@app.route('/')
def cancel():
    return 'You have cancelled your payment'

@app.route('/refund/execute',methods=['GET','POST'])
def execute():
    
    # assumption: when the user logged in, we have their paypal account
    print('8')
    paymentId = request.args.get('paymentId')
    payer_id=request.args.get('PayerID')
    print(paymentId)
    payment = paypalrestsdk.Payment.find(paymentId)

    print(payment['transactions'][0]['item_list']['items'][0]['name'])
    claimid = payment['transactions'][0]['item_list']['items'][0]['name']
    if payment.execute({"payer_id": payer_id}):
        print("Payment[%s] execute successfully" % (payment.id))
        result = {'Status':200, 'Message':"Payment[%s] execute successfully"% (payment.id),'claimid':claimid}
        # print(result)
        # need to update the claim as close 
    else:
        print(payment.error)

    

    return 'Your payment has been processed successfully. Thank you for your payment! You may close the page now'

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port=3000,debug=True)