from global_var import db


class RH(db.Model):
    __tablename__ = 'rh'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer, db.ForeignKey('resident_information.id'))
    hid = db.Column(db.Integer, db.ForeignKey('house_information.id'))
