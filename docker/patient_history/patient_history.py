#patient history service for retrival and update of patient history via HTTP
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/patient_history'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Patient_history(db.Model):
    __tablename__ = 'patient_history'
 
    PID = db.Column(db.String(100))
    AID = db.Column(db.String(100), primary_key=True)
    Medication = db.Column(db.String(100), nullable=True)
    BillAmount = db.Column(db.String(100), nullable=True)
    ClaimAmount = db.Column(db.String(100), nullable=True)
 
    def __init__(self, PID, AID, Medication, BillAmount, ClaimAmount):
        self.PID = PID
        self.AID = AID
        self.Medication = Medication
        self.BillAmount = BillAmount
        self.ClaimAmount = ClaimAmount

 
    def json(self):
        return {"PID": self.PID, "AID": self.AID, "Medication": self.Medication, "BillAmount": self.BillAmount, "ClaimAmount": self.ClaimAmount}

# get all 
@app.route("/patient_history")
def get_all():
    # query for clinic alone
	return jsonify({"patient_history": [patient_history.json() for patient_history in Patient_history.query.all()]})
    
#get patient history with patient ID
@app.route("/patient_history/<string:PID>")
def find_by_PID(PID):
    history = Patient_history.query.filter_by(PID=PID).all()
    # result = []
    if history:
        # for ahistory in history:
        #     result.append(ahistory.json())
        return jsonify({"patient_history": [patient_history.json() for patient_history in Patient_history.query.filter_by(PID = PID)]})
    return jsonify({"message": "Patient History not found."}), 404
  
@app.route("/patient_history/<string:PID>/", methods=['POST'])
def create_history(PID):
    if (Patient_history.query.filter_by(PID=PID).first()):
        return jsonify({"message": "An patient history already exists."}), 400

    data = request.get_json()
    history = Patient_history(PID, **data)
   
    try:
        db.session.add(history)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the patient history."}), 500

    return jsonify(history.json()), 201


if __name__ == '__main__': # if it is the main program you run, then start flask
    # with docker
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0',port=5008, debug=True) #to allow the file to be named other stuff apart from app.py
    # debug=True; shows the error and it will auto restart
