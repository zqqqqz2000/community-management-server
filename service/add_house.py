from dao.house_information import HouseInformation
from dao.rh import RH
from dao.resident_information import ResidentInformation
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


def add_rh(rid: int, building_number: str, room_number: str) -> bool:
    h: HouseInformation = HouseInformation.query.filter_by(
        building_number=building_number,
        room_number=room_number
    ).first()
    if not h:
        return False
    rh = RH(rid=rid, hid=h.id)
    db.session.add(rh)
    db.session.commit()
    return True
