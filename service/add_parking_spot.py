from typing import *
from dao.parking_spot_information import ParkingSpotInformation
from dao.resident_information import ResidentInformation
from dao.pr import PR
from global_var import db


def add_parking_spot_user(username: str, parking_spot_number: str, license_: str) -> bool:
    r: ResidentInformation = ResidentInformation.query.filter_by(username=username).first()
    if not r:
        return False
    p: ParkingSpotInformation = ParkingSpotInformation.query.filter_by(
        parking_spot_num=parking_spot_number,
        license=license_
    ).first()
    if not p:
        p: ParkingSpotInformation = ParkingSpotInformation(parking_spot_num=parking_spot_number, license=license_)
        db.session.add(p)
    db.session.commit()
    pr: PR = PR(pid=p.id, rid=r.id)
    db.session.add(pr)
    db.session.commit()
    return True


def add_parking_spot(parking_spot_number: str, license_: str):
    p: ParkingSpotInformation = ParkingSpotInformation(parking_spot_num=parking_spot_number, license=license_)
    db.session.add(p)
    db.session.commit()
