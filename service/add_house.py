from dao.house_information import HouseInformation
from global_var import db


def add_house(building_number: str, room_number: str, area: float, family_size: int):
    h = HouseInformation(
        building_number=building_number,
        room_number=room_number,
        area=area,
        family_size=family_size,
        maintenance_balance=0
    )
    db.session.add(h)
    db.session.commit()
