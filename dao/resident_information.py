from global_var import db


class ResidentInformation(db.Model):
    __tablename__ = 'resident_information'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20))
    name = db.Column(db.String(10))
    job = db.Column(db.String(64))
