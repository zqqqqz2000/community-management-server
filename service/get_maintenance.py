from dao.maintenance_information import MaintenanceInformation
from dao.house_information import HouseInformation
from dao.rh import RH
from dao.resident_information import ResidentInformation
from global_var import db
from datetime import date
from typing import *


def get_maintenance():
    m: List[Tuple[MaintenanceInformation, str, str]] = db.session.query(
        MaintenanceInformation,
        HouseInformation.building_number,
        HouseInformation.room_number
    ).all()
    return [{
        'id': maintenance.id,
        'building_num': building_number,
        'room_number': room_number,
        'apply_date': str(maintenance.apply_date),
        'fix_date': str(maintenance.fix_date),
        'fix_number': maintenance.fix_number,
        'pay_amount': maintenance.pay_amount,
        'comment': maintenance.comment,
        'from_balance': maintenance.from_balance,
        'status': 0 if not maintenance.pay_amount else 1
    } for maintenance, building_number, room_number in m]


def get_maintenance_from_username(username: str):
    m: List[Tuple[MaintenanceInformation, str, str]] = db.session.query(
        MaintenanceInformation,
        HouseInformation.building_number,
        HouseInformation.room_number
    ).filter(
        ResidentInformation.username == username,
        RH.rid == ResidentInformation.id,
        RH.hid == MaintenanceInformation.hid,
        RH.hid == HouseInformation.id
    ).all()
    return [{
        'id': maintenance.id,
        'building_num': building_number,
        'room_number': room_number,
        'apply_date': str(maintenance.apply_date),
        'fix_date': str(maintenance.fix_date),
        'fix_number': maintenance.fix_number,
        'pay_amount': maintenance.pay_amount,
        'comment': maintenance.comment,
        'from_balance': maintenance.from_balance,
        'status': 0 if not maintenance.pay_amount else 1
    } for maintenance, building_number, room_number in m]
