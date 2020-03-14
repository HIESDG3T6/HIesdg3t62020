#patient history service for retrival and update of patient history via HTTP
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/patient_history'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Patient_history(db.Model):
    __tablename__ = 'patient_history'
 
    PID = db.Column(db.Integer, primary_key=True)
    AID = db.Column(db.Integer, primary_key=True)
    clinicName = db.Column(db.String(100), nullable=False)
    Pname = db.Column(db.String(1000), nullable=False)
    contact = db.Column(db.String(1000), nullable=True)
    location = db.Column(db.String(1000), nullable=True)
    treatmentDetails = db.Column(db.String(10000), nullable=True)
 
    def __init__(self, PID, AID, clinicName, Pname, contact, location, treatmentDetails):
        self.PID = PID
        self.AID = AID
        self.clinicName = clinicName
        self.Pname = Pname
        self.contact = contact
        self.location = location
        self.treatmentDetails = treatmentDetails
 
    def json(self):
        return {"Patient ID": self.PID, "Appointment ID": self.AID, "Clinic Name": self.clinicName, "Patient Name": self.Pname, "Contact Number": self.contact, "Location": self.location, "Treatment Details": self.treatmentDetails}

# get all 
@app.route("/patient_history")
def get_all():
    # query for clinic alone
	return jsonify({"patient_history": [patient_history.json() for patient_history in Patient_history.query.all()]})
    
#get patient history with patient ID
@app.route("/patient_history/<string:PID>")
def find_by_PID(PID):
    history = Patient_history.query.filter_by(PID=PID).all()
    result = []
    if history:
        for ahistory in history:
            result.append(ahistory.json())
        return jsonify(result)
    return jsonify({"message": "Patient History not found."}), 404

# get patient history with appointment ID
# @app.route("/patient_history/<string:AID>")
# def find_by_AID(AID):
#     history = Patient_history.query.filter_by(AID=AID).first()
#     if history:
#         return jsonify(history.json())
#     return jsonify({"message": "Appointment History not found."}), 404
    
@app.route("/patient_history/<string:AID>", methods=['POST'])
def create_history(AID):
    if (Patient_history.query.filter_by(AID=AID).first()):
        return jsonify({"message": "An patient history with AppointmentID '{}' already exists.".format(AID)}), 400

    data = request.get_json()
    history = Patient_history(AID, **data)
   
    try:
        db.session.add(history)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the patient history."}), 500

    return jsonify(history.json()), 201


if __name__ == '__main__': # if it is the main program you run, then start flask
    # with docker
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(port=5000, debug=True) #to allow the file to be named other stuff apart from app.py
    # debug=True; shows the error and it will auto restart
