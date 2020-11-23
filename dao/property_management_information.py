from global_var import db


class PropertyManagementInformation(db.Model):
    __tablename__ = 'property_management_information'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
