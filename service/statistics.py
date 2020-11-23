from global_var import db
from dao.parking_spot_pay_information import ParkingSpotPayInformation
from dao.property_fee_information import PropertyFeeInformation


def get_parking_fee_statistics():
    total = db.session.query(ParkingSpotPayInformation.date, db.func.count('*').label('count')). \
        group_by(ParkingSpotPayInformation.date).all()
    un_pay = db.session.query(ParkingSpotPayInformation.date, db.func.count('*').label('count')). \
        group_by(ParkingSpotPayInformation.date).filter(
        ParkingSpotPayInformation.ispay == 0
    ).all()
    total_dict = {str(date): count for date, count in total}
    un_pay_dict = {str(date): count for date, count in un_pay}
    for date in total_dict:
        if date not in un_pay_dict:
            un_pay_dict[date] = 0
    return total_dict, un_pay_dict


def get_property_fee_statistics():
    total = db.session.query(PropertyFeeInformation.date, db.func.count('*').label('count')). \
        group_by(PropertyFeeInformation.date).all()
    un_pay = db.session.query(PropertyFeeInformation.date, db.func.count('*').label('count')). \
        group_by(PropertyFeeInformation.date).filter(
        PropertyFeeInformation.ispay == 0
    ).all()
    total_dict = {str(date): count for date, count in total}
    un_pay_dict = {str(date): count for date, count in un_pay}
    for date in total_dict:
        if date not in un_pay_dict:
            un_pay_dict[date] = 0
    return total_dict, un_pay_dict
