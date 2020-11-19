from global_var import db


class MaintenanceInformation(db.Model):
    __tablename__ = 'maintenance_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hid = db.Column(db.Integer, db.ForeignKey('house_information.id'))
    apply_date = db.Column(db.Date)
    fix_date = db.Column(db.Date, nullable=True)
    fix_number = db.Column(db.String(32), nullable=True)
    pay_amount = db.Column(db.Float, nullable=True)
    comment = db.Column(db.String(128))
    from_balance = db.Column(db.Integer, default=0)
