from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/insurance_claim'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

# create another refund table to store reply from refund for payment UI
class Refund(db.Model):
    __tablename__ = 'refund'

    Corrid = db.Column(db.Integer, nullable=False,primary_key=True)
    ClaimID = db.Column(db.Integer, nullable=True)
    Status = db.Column(db.Integer,nullable=True)
    Approval_url = db.Column(db.String(10000),nullable=True)
    
    def __init__(self, Corrid, ClaimID, Status, Approval_url):
        self.Corrid = Corrid
        self.ClaimID = ClaimID
        self.Status = Status
        self.Approval_url = Approval_url

    # return an insurance item as a JSON object
    def json(self):
        
        return {
            'Corrid': self.Corrid, 'ClaimID': self.ClaimID, 'Status': self.Status, 'Approval_url': self.Approval_url}


# ================================== For Refund Table ============================================

# create refund record to refund table
@app.route("/refund/<string:Corrid>", methods=['POST'])
def create_refund_record(Corrid):
    if (Refund.query.filter_by(Corrid=Corrid).first()):
        return jsonify({"message": "An record with corrid '{}' already exists.".format(Corrid)}), 400

    data = request.get_json()
    record = Refund(Corrid, **data)
   
    try:
        db.session.add(record)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the refund record."}), 500

    return jsonify(record.json()), 201

# add 
@app.route("/refund/<string:Corrid>/", methods=['POST'])
def update_refund_record(Corrid):
    refund = Refund.query.filter_by(Corrid=Corrid).first()
    data = request.get_json()
    refund.Status = data.Status
    refund.Approval_url = data.Approval_url
    try:
        db.session.commit()
        
    except:
        return jsonify({"message": "An error occurred updating the refund record."}),500


    return jsonify(refund.json()),201
    #return jsonify(claim.json()),201


@app.route("/refund/<string:ClaimID>")
def find_url_by_ClaimID(ClaimID):
    record = Refund.query.filter_by(ClaimID=ClaimID).first()
    # url = record['Approval_url']

    if record:
        return jsonify(record.json())
    return jsonify({"message": "Arroval URL record not found."}), 404


if __name__ == '__main__':
    app.run(port=5001, debug=True)

