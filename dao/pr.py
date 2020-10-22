from global_var import db


class PR(db.Model):
    __tablename__ = 'pr'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    pid = db.Column(db.Integer, db.ForeignKey('parking_spot_information.id'), nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey('resident_information.id'), nullable=False)
