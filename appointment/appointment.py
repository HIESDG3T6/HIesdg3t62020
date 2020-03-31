from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json
import pika
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/appointment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Appointment(db.Model):
    __tablename__ = 'appointment'

    # NEED TO ADD IN DB.ForeignKey('databasename.columnname')
    AID = db.Column(db.Integer, nullable= True)
    customerID = db.Column(db.String(10), primary_key = True)
    clinicID = db.Column(db.String(10), nullable= False)
    doctorID = db.Column(db.String(10), nullable= False)
    appointmentDate = db.Column(db.Date, primary_key = True)
    appointmentTime = db.Column(db.Time, primary_key = True)

    def __init__(self, AID, customerID, clinicID, doctorID, appointmentDate, appointmentTime):
        self.AID = AID
        self.customerID = customerID
        self.clinicID = clinicID
        self.doctorID = doctorID
        self.appointmentDate = appointmentDate
        self.appointmentTime = appointmentTime

    def json(self):
        return {
            "AID": self.AID,
            "customerID" : self.customerID,
            "clinicID" : self.clinicID,
            "doctorID" : self.doctorID,
            "appointmentDate" : self.appointmentDate.__str__(),
            "appointmentTime" : self.appointmentTime.__str__()
        }

# TO BE DONE
# SCRIPT TO DELETE THE APPOINTMENTS DAILY #

@app.route("/appointment", methods=['POST'])
def create_appointment():
    status = 201

    appointment_input = request.json
    # why get_json() doesn't work here?

    customerID = appointment_input['customerID']
    clinicID = appointment_input['clinicID']
    doctorID = appointment_input['doctorID']
    appointmentDate = appointment_input['appointmentDate']
    appointmentTime = appointment_input['appointmentTime']

    # return jsonify(msg), 201

    appointment = Appointment(**appointment_input)

    if (Appointment.query.filter_by(customerID = customerID, appointmentDate = appointmentDate, appointmentTime = appointmentTime).first()):
        status = 400
        msg = "You have an existing appointment on " + appointmentDate + ", " + appointmentTime
        return jsonify({"status": status, "message": msg}), status

    if (Appointment.query.filter_by(clinicID = clinicID, appointmentDate = appointmentDate, appointmentTime = appointmentTime).first()):
        status = 400
        msg = "Your chosen slot on " + appointmentDate + ", " + appointmentTime + " is taken. Please try another timeslot."
        return jsonify({"status": status, "message": msg}), status

    if status == 201:
        try:
            db.session.add(appointment)
            db.session.commit()

        except Exception as e:
            status = 500
            return jsonify({"status": status, "message":e}), status #"An error occured creating the book."

        if status == 201:
                result = appointment.json()
                return jsonify(result), 201

    return jsonify(appointment.json()), 201

# @app.route("/numOfAppointment")
# def numOfAppointment():
#     key = request.args.get('clinicID','')

#     return key
#     # result = Appointment.query.filter_by(clinicID = clinicID, appointmentDate = appointmentDate, appointmentTime = appointmentTime)


@app.route("/get-appointment/<string:customerID>")
def getAllAppointment(customerID):
    # COULD POSSIBLY DO A SORT BEFORE RETURNING
    return jsonify({"appointments": [appointment.json() for appointment in Appointment.query.filter_by(customerID = customerID)]})

@app.route("/get-clinic-appointment/<string:clinicID>")
def getClinicAppointment(clinicID):
    # COULD POSSIBLY DO A SORT BEFORE RETURNING
    return jsonify({"appointments": [appointment.json() for appointment in Appointment.query.filter_by(clinicID = clinicID)]})



if __name__ == '__main__':
    app.run(port=4444, debug=True)

# ATTEMPT FOR AMQP KIV!!!!!!!!!!!!!
    # def send_appointment(appointment_input):
    #     hostname = "localhost"  #"http://localhost:15672"
    #     port = 5672

    #     connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    #     channel = connection.channel()

    #     exchangename = "appointment_topic"
    #     channel.exchange_declare(exchange=exchangename, exchange_type='topic')

    #     message = json.dumps(order, default=str)

    #     if "status" in order:
    #         #Call for the notification service and inform the patient that
    #             # He/She has an appointment made at the same timing
    #             # The appointment slot is full

    #         pass
        
    #     else:
    #         # corrid = str(uuid.uuid4())
    #         # row = {"customerID" : appointment_input["customerID"], "correlation_id": corrid}
    #         # csvheaders = ["customerID", "correlation_id", "status"]

    #         # with open("corrids.csv", "a+", newline='') as corrid_file: # 'with' statement in python auto-closes the file when the block of code finishes, even if some exception happens in the middle
    #         #     csvwriter = csv.DictWriter(corrid_file, csvheaders)
    #         #     csvwriter.writerow(row)

    #         # replyqueuename = "appointment.reply"

    #         channel.queue_declar(queue='clinic', durable=True)
    #         channel.queue_bind(exchange=exchangename, queue='clinic', routing_key='appointment.book')
    #         channel.basic_publish(exchange=exchangename, routing_key="appointment.book", body=message,
    #                                 properties=pika.BasicProperties(delivery_mode = 2,                                                        
    #                                 )
    #                             )
            
    #         print("Order sent to Clinic")

    #     connection.close()

