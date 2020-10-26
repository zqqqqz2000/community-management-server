from global_var import db


class ParkingSpotPayInformation(db.Model):
    __tablename__ = "parking_spot_pay_information"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('parking_spot_information.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    pay_date = db.Column(db.Date, nullable=True)
    pay_amount = db.Column(db.Float, nullable=False)
    handle_rid = db.Column(db.Integer, db.ForeignKey('resident_information.id'), nullable=True)
    ispay = db.Column(db.Integer, nullable=False)
