import datetime
from global_var import db
from dao.property_fee_information import PropertyFeeInformation
from dao.resident_information import ResidentInformation


def property_fee_pay(pid: int, username: str) -> bool:
    pp: PropertyFeeInformation = PropertyFeeInformation.query.filter(
        PropertyFeeInformation.id == pid
    ).first()
    if pp.ispay:
        return False
    r: ResidentInformation = ResidentInformation.query.filter_by(
        username=username
    ).first()
    pp.ispay = True
    pp.handle_rid = r.id
    pp.pay_date = datetime.datetime.now().date()
    db.session.commit()
    return True
