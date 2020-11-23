from global_var import db


class HouseInformation(db.Model):
    __tablename__ = 'house_information'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    building_number = db.Column(db.String(5))
    room_number = db.Column(db.String(5))
    area = db.Column(db.Float)
    family_size = db.Column(db.Integer)
    maintenance_balance = db.Column(db.Float)
    db.UniqueConstraint(building_number, room_number, name='check_position_unique')
    db.CheckConstraint('area > 0', name='check_area_positive')
    db.CheckConstraint('family_size >= 0', name='check_family_size_positive')
    db.CheckConstraint('maintenance_balance >= 0', name='check_maintenance_balance_positive')
