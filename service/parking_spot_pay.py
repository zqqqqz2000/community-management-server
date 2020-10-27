from dao.parking_spot_pay_information import ParkingSpotPayInformation
from dao.resident_information import ResidentInformation
from global_var import db
import datetime


def parking_spot_pay(bill_id: int, username: str) -> bool:
    query_res: ParkingSpotPayInformation = ParkingSpotPayInformation.query.filter_by(id=bill_id).first()
    r: ResidentInformation = ResidentInformation.query.filter_by(username=username).first()
    if query_res.ispay:
        return False
    query_res.ispay = True
    query_res.pay_date = datetime.datetime.now().date()
    query_res.handle_rid = r.id
    db.session.commit()
    return True
