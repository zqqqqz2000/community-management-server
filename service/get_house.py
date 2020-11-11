from dao.house_information import HouseInformation
from typing import *
from global_var import db
from dao.resident_information import ResidentInformation
from dao.rh import RH


def get_houses():
    houses: List[HouseInformation] = HouseInformation.query.filter_by().all()
    return [
        {
            'id': house.id,
            'building_number': house.building_number,
            'room_number': house.room_number,
            'area': house.area,
            'family_size': house.family_size,
            'maintenance_balance': house.maintenance_balance
        }
        for house in houses]


def get_house_from_resident(rid: int):
    houses: List[Tuple[HouseInformation, RH.id]] = db.session.query(
        HouseInformation,
        RH.id
    ).filter(
        RH.rid == rid,
        RH.hid == HouseInformation.id
    ).all()
    return [
        {
            'id': rhid,
            'building_number': house.building_number,
            'room_number': house.room_number,
            'area': house.area,
            'family_size': house.family_size,
            'maintenance_balance': house.maintenance_balance
        }
        for house, rhid in houses]


def get_house_from_resident_username(username: str):
    houses: List[HouseInformation] = HouseInformation.query.filter(
        ResidentInformation.username == username,
        ResidentInformation.id == RH.rid,
        RH.hid == HouseInformation.id
    ).all()
    return [
        {
            'id': house.id,
            'building_number': house.building_number,
            'room_number': house.room_number,
            'area': house.area,
            'family_size': house.family_size,
            'maintenance_balance': house.maintenance_balance
        }
        for house in houses]
