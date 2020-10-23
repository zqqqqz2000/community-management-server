from typing import *
from dao.pr import PR
from dao.parking_spot_information import ParkingSpotInformation
from global_var import db
from dao.parking_spot_information import ParkingSpotInformation


def delete_parking_spot_user_pr(pid_: int) -> NoReturn:
    pr: PR = PR.query.filter(
        PR.pid == ParkingSpotInformation.id,
        ParkingSpotInformation.id == pid_
    ).first()
    if pr:
        db.session.delete(pr)
    db.session.commit()


def delete_parking_spot(id_: int) -> NoReturn:
    p: ParkingSpotInformation = ParkingSpotInformation.query.filter_by(id=id_).first()
    if p:
        db.session.delete(p)
    db.session.commit()
