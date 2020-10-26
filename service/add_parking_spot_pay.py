from dao.parking_spot_pay_information import ParkingSpotPayInformation
from dao.parking_spot_information import ParkingSpotInformation
from typing import *
from datetime import date
from global_var import db


def add_parking_spot_pay_all(price: float, date_: date):
    parking_spot_infos: List[ParkingSpotInformation] = ParkingSpotInformation.query.filter().all()
    parking_spot_pays_info: List[ParkingSpotPayInformation] = []
    for parking_spot_info in parking_spot_infos:
        parking_spot_pays_info.append(
            ParkingSpotPayInformation(
                pid=parking_spot_info.id,
                date=date_,
                pay_amount=price,
                ispay=0
            )
        )
    db.session.add_all(parking_spot_pays_info)
    db.session.commit()
