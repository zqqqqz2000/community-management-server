from typing import *
from dao.parking_spot_information import ParkingSpotInformation
from dao.resident_information import ResidentInformation
from dao.pr import PR
from global_var import db


def get_parking_spot(username: str) -> List[Dict]:
    spots: List[ParkingSpotInformation] = ParkingSpotInformation.query.filter(
        ResidentInformation.username == username,
        ResidentInformation.id == PR.rid,
        PR.pid == ParkingSpotInformation.id
    ).all()
    return [
        {
            'id': spot.id,
            'parking_spot_number': spot.parking_spot_num,
            'license': spot.license
        } for spot in spots
    ]


def get_all_spot() -> List[Dict]:
    spots: List[ParkingSpotInformation] = ParkingSpotInformation.query.filter().all()
    return [
        {
            'id': spot.id,
            'parking_spot_number': spot.parking_spot_num,
            'license': spot.license
        } for spot in spots
    ]
