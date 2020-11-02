from datetime import date
from dao.house_information import HouseInformation
from dao.property_fee_information import PropertyFeeInformation
from typing import *
from os import urandom
from global_var import db


def add_property_fee_all(price: float, date_: date):
    try:
        houses: List[HouseInformation] = HouseInformation.query.all()
        for house in houses:
            property_fee = PropertyFeeInformation(
                hid=house.id,
                date=date_,
                pay_amount=price,
                ispay=0,
                order_number=urandom(8).hex()
            )
            db.session.add(property_fee)
        db.session.commit()
        return True
    except Exception as _:
        return False
