from global_var import db


class ParkingSpotInformation(db.Model):
    __tablename__ = 'parking_spot_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parking_spot_num = db.Column(db.String(10), nullable=False, unique=True)
    license = db.Column(db.String(20), nullable=False, unique=True)
