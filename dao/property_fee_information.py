from global_var import db


class PropertyFeeInformation(db.Model):
    __tablename__ = "property_fee_information"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hid = db.Column(db.Integer, db.ForeignKey('house_information.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    pay_date = db.Column(db.Date, nullable=True)
    pay_amount = db.Column(db.Float, nullable=False)
    ispay = db.Column(db.Integer, nullable=False)
    handle_rid = db.Column(db.Integer, db.ForeignKey('resident_information.id'), nullable=True)
    order_number = db.Column(db.String(32), nullable=True)
    db.CheckConstraint('pay_date >= date', name='check_pay_date')
    db.CheckConstraint('pay_amount > 0', name='check_pay_amount_positive')
