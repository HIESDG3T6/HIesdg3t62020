from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

import json
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Appointment(db.Model):
    __tablename__ = 'appointment'

    # NEED TO ADD IN DB.ForeignKey('databasename.columnname')
    AID = db.Column(db.Integer, nullable= True)
    customerID = db.Column(db.String(10), primary_key = True)
    clinicID = db.Column(db.String(100), nullable= False)
    doctorID = db.Column(db.String(10), nullable= False)
    appointmentDate = db.Column(db.Date, primary_key = True)
    appointmentTime = db.Column(db.Time, primary_key = True)

    def __init__(self, customerID, clinicID, doctorID, appointmentDate, appointmentTime):
        self.AID = None
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

    appointment_input = request.get_json(force = True)
    # why get_json() doesn't work here?

    print(appointment_input)

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
        return jsonify({"message": msg}), 400


    if (Appointment.query.filter_by(clinicID = clinicID, appointmentDate = appointmentDate, appointmentTime = appointmentTime).first()):
        status = 400
        msg = "Your chosen slot on " + appointmentDate + ", " + appointmentTime + " is taken. Please try another timeslot."
        return jsonify({"message": msg}), 400

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

@app.route("/numOfAppointment/<string:clinicID>/<string:appointmentDate>")
def numOfAppointment(clinicID, appointmentDate):

    result = jsonify({"appointments": [appointment.json() for appointment in Appointment.query.filter_by(clinicID = clinicID, appointmentDate = appointmentDate)]})

    return result, 201


@app.route("/get-appointment/<string:customerID>")
def getAllAppointment(customerID):
    # COULD POSSIBLY DO A SORT BEFORE RETURNING
    return jsonify({"appointments": [appointment.json() for appointment in Appointment.query.filter_by(customerID = customerID)]})

@app.route("/get-clinic-appointment/<string:clinicID>")
def getClinicAppointment(clinicID):
    # COULD POSSIBLY DO A SORT BEFORE RETURNING
    return jsonify({"appointments": [appointment.json() for appointment in Appointment.query.filter_by(clinicID = clinicID)]})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)