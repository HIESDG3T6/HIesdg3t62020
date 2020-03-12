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
 
    def __init__(clinicName, doctorName, groupedLocation, address, postalCode, specialty, contactNumber):
        self.clinicName = clinicName
        self.doctorName = doctorName
        self.groupedLocation = groupedLocation
        self.address = address
        self.postalCode = postalCode
        self.specialty = specialty
        self.contactNumber = contactNumber
 
    def json(self):
        return {"clinicName": self.clinicName, "doctorName": self.doctorName, "groupedLocation": self.groupedLocation, "address": self.address, "postalCode": self.postalCode, "specialty": self.specialty, "contactNumber": self.contactNumber}
class ClinicOpening(db.Model):
    __tablename__ = 'clinicOpening'
 
    clinicName = db.Column(db.String(100), primary_key=True)
    openingDays = db.Column(db.String(20), primary_key=True)
    openingHour = db.Column(db.String(10), primary_key=True)
    closingHour = db.Column(db.String(10), nullable=False)
 
    def __init__(clinicName, openingDays, openingHour, closingHour):
        self.clinicName = clinicName
        self.openingDays = openingDays
        self.openingHour = openingHour
        self.closingHour = closingHour
 
    def json(self):
        return {"clinicName": self.clinicName, "openingDays": self.openingDays, "openingHour": self.openingHour, "closingHour": self.closingHour}

# class Map(db.Model):
#     __tablename__ = 'map'
#     clinicName = db.Column(db.String(100), db.ForeignKey('clinic.clinicName'), primary_key=True)
#     ClinicOpening = db.Column(db.String(100), db.ForeignKey('clinicOpening.clinicName'), primary_key=True)

#     def __init__(clinicName, ClinicOpening):
#         self.clinicName = clinicName
#         self.ClinicOpening = ClinicOpening

#     def json(self):
#         return {"clinicName": self.clinicName, "ClinicOpening": self.ClinicOpening}

# get all clinics
@app.route("/clinic")
def get_all():
    # query for clinic alone
	return jsonify({"clinic": [clinic.json() for clinic in Clinic.query.all()]})

    # opening = db.session.query(ClinicOpening).join(Map, Map.ClinicOpening==ClinicOpening.clinicName).all()
    # clinic = db.session.query(Clinic).join(Map, Clinic.clinicName==Map.clinicName).all()
    # joined = db.session.query(Clinic, ClinicOpening).join(ClinicOpening, Clinic.clinicName==ClinicOpening.clinicName).first()
    # return joined.dumps(joined)
    # query for clinic and opening hours

    # query = db.session.query(Clinic, ClinicOpening).join(Map, Clinic.clinicName==Map.clinicName, Map.ClinicOpening==ClinicOpening.clinicName).all()
    # return jsonify({"clinic": [clinic.json() for clinic in query]})


#get clinics from name with %
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
    groupedLocation = Clinic.query.join(ClinicOpening, Clinic.clinicName==ClinicOpening.clinicName).filter_by(groupedLocation=Clinic.groupedLocation).all()
    # if groupedLocation:
    #     return jsonify(groupedLocation.json())

    # groupedLocation = Clinic.query.filter_by(groupedLocation=groupedLocation).all()
    result = []
    return groupedLocation
    if groupedLocation:
        for aLocation in groupedLocation:
            result.append(aLocation.json())
        return jsonify(result)
    return jsonify({"message": "No clinics found."}), 404

# Create clinic
# @app.route("/clinic/<string:clinicName>", methods=['POST'])
# def create_clinic(clinicName):
#     if (Clinic.query.filter_by(clinicName=clinicName).first()):
#         return jsonify({"message": "Clinic '{}' already exists.".format(clinicName)}), 400
 
#     data = request.get_json()
#     clinic = Clinic(clinicName, **data)
 
#     try:
#         db.session.add(clinic)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred creating the clinic."}), 500
 
#     return jsonify(clinic.json()), 201

# Create doctor in clinic
# @app.route("/clinic/<string:doctorName>", methods=['POST'])
# def create_doctor(clinicName, doctorName):
#     if (Clinic.query.filter(clinicName=clinicName).filter(doctorName=doctorName).first()):
#         return jsonify({"message": "Doctor '{doctorName}' already exists in Clinic '{clinicName}.".format(doctorName, clinicName)}), 400
 
#     data = request.get_json()
#     clinic = Clinic(clinicName, **data)
 
#     try:
#         db.session.add(clinic)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred adding the doctor to the clinic."}), 500
 
#     return jsonify(clinic.json()), 201

if __name__ == '__main__': # if it is the main program you run, then start flask
    # with docker
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(port=5000, debug=True) #to allow the file to be named other stuff apart from app.py
    # debug=True; shows the error and it will auto restart
