from dao.house_information import HouseInformation
from typing import *


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
