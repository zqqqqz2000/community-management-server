from dao.parking_spot_pay_information import ParkingSpotPayInformation
from dao.parking_spot_information import ParkingSpotInformation
from dao.resident_information import ResidentInformation
from typing import *
from global_var import db


def get_parking_spot_pay_all_from_pid(pid: int):
    parking_spot_pay_infos: List[
        ParkingSpotPayInformation,
        ResidentInformation.username
    ] = db.session.query(ParkingSpotPayInformation, ResidentInformation.username).filter(
        ParkingSpotInformation.id == pid,
        ParkingSpotInformation.id == ParkingSpotPayInformation.pid
    ).all()
    return [{
        'id': parking_spot_pay_info[0].id,
        'date': parking_spot_pay_info[0].date.strftime('%Y-%M-%d'),
        'pay_date': parking_spot_pay_info[0].pay_date.strftime('%Y-%M-%d') if parking_spot_pay_info[0].ispay else "未支付",
        'pay_amount': parking_spot_pay_info[0].pay_amount,
        'pay_username': parking_spot_pay_info[1] if parking_spot_pay_info[0].ispay else "未支付"
    } for parking_spot_pay_info in parking_spot_pay_infos]
