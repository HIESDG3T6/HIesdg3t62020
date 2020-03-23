from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# with docker
# from os import environ

app = Flask(__name__)

# with docker
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')

# without docker
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Clinic(db.Model):
    __tablename__ = 'clinic'
 
    clinicName = db.Column(db.String(100), primary_key=True)
    doctorName = db.Column(db.String(100), primary_key=True)
    groupedLocation = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    postalCode = db.Column(db.Integer, nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    contactNumber = db.Column(db.String(15), nullable=False)
    opening = db.Column(db.String(200), nullable=False)
 
    def __init__(clinicName, doctorName, groupedLocation, address, postalCode, specialty, contactNumber, opening):
        self.clinicName = clinicName
        self.doctorName = doctorName
        self.groupedLocation = groupedLocation
        self.address = address
        self.postalCode = postalCode
        self.specialty = specialty
        self.contactNumber = contactNumber
        self.opening = opening
 
    def json(self):
        return {"clinicName": self.clinicName, "doctorName": self.doctorName, "groupedLocation": self.groupedLocation, "address": self.address, "postalCode": self.postalCode, "specialty": self.specialty, "contactNumber": self.contactNumber, "opening": self.opening}



# get all clinics
@app.route("/clinic")
def get_all():
    # query for clinic alone
	return jsonify({"clinic": [clinic.json() for clinic in Clinic.query.all()]})

    # queries for 2 tables
    # opening = db.session.query(ClinicOpening).join(Map, Map.ClinicOpening==ClinicOpening.clinicName).all()
    # clinic = db.session.query(Clinic).join(Map, Clinic.clinicName==Map.clinicName).all()
    # joined = db.session.query(Clinic, ClinicOpening).join(ClinicOpening, Clinic.clinicName==ClinicOpening.clinicName).first()
    # return joined.dumps(joined)
    # query for clinic and opening hours

    # query = db.session.query(Clinic, ClinicOpening).join(Map, Clinic.clinicName==Map.clinicName, Map.ClinicOpening==ClinicOpening.clinicName).all()
    # return jsonify({"clinic": [clinic.json() for clinic in query]})


#get clinics from name
@app.route("/clinic/<string:clinicName>")
def find_by_clinicName(clinicName):
    # clinic = Clinic.query(Clinic).join(ClinicOpening).filter(clinicName.like(f'%{clinicName}%')).all()
    clinic = Clinic.query.filter_by(clinicName=clinicName).all()
    result = []
    if clinic:
        for aClinic in clinic:
            result.append(aClinic.json())
        return jsonify(result)
    return jsonify({"message": "Clinic not found."}), 404

# get clinics by location group
@app.route("/clinic/loc/<string:groupedLocation>")
def find_by_groupedLocation(groupedLocation):
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    groupedLocation = Clinic.query.filter_by(groupedLocation=groupedLocation).order_by(Clinic.clinicName).all()
    result = []

    if groupedLocation:
        for aLocation in groupedLocation:
            result.append(aLocation.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

# get clinics by specialty
@app.route("/clinic/spec/<string:specialty>")
def find_by_specialty(specialty):
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    specialty = Clinic.query.filter_by(specialty=specialty).order_by(Clinic.clinicName).all()
    result = []

    if specialty:
        for aClinic in specialty:
            result.append(aClinic.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

@app.route("/clinic/<string:clinicName>/<string:groupedLocation>/<string:specialty>")
def find_by_all(clinicName, groupedLocation, specialty):
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    clinics = Clinic.query.filter_by(clinicName=clinicName).filter_by(groupedLocation=groupedLocation).filter_by(specialty=specialty).order_by(Clinic.clinicName).all()
    result = []

    if clinics:
        for aClinic in clinics:
            result.append(aClinic.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

@app.route("/clinic/specloc/<string:groupedLocation>/<string:specialty>")
def find_by_spec_loc(groupedLocation, specialty):
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    clinics = Clinic.query.filter_by(groupedLocation=groupedLocation).filter_by(specialty=specialty).order_by(Clinic.clinicName).all()
    result = []

    if clinics:
        for aClinic in clinics:
            result.append(aClinic.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

@app.route("/clinic/nameloc/<string:clinicName>/<string:groupedLocation>")
def find_by_nameloc(clinicName, groupedLocation):
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    clinics = Clinic.query.filter_by(clinicName=clinicName).filter_by(groupedLocation=groupedLocation).order_by(Clinic.clinicName).all()
    result = []

    if clinics:
        for aClinic in clinics:
            result.append(aClinic.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

@app.route("/clinic/namespec/<string:clinicName>/<string:specialty>")
def find_by_namespec(clinicName, specialty):
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    clinics = Clinic.query.filter_by(clinicName=clinicName).filter_by(specialty=specialty).order_by(Clinic.clinicName).all()
    result = []

    if clinics:
        for aClinic in clinics:
            result.append(aClinic.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

if __name__ == '__main__': # if it is the main program you run, then start flask
    # with docker
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(port=5000, debug=True) #to allow the file to be named other stuff apart from app.py
    # debug=True; shows the error and it will auto restart
