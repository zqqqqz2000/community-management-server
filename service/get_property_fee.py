from dao.property_fee_information import PropertyFeeInformation
from dao.house_information import HouseInformation
from typing import *

from dao.resident_information import ResidentInformation
from dao.rh import RH
from global_var import db


def get_all_property_fee() -> List[Dict[str, Union[int, str]]]:
    property_fees: List[Tuple[PropertyFeeInformation, str, str]] = db.session.query(
        PropertyFeeInformation,
        HouseInformation.building_number,
        HouseInformation.room_number
    ).filter(
        PropertyFeeInformation.hid == HouseInformation.id
    ).all()
    return [{
        'building_number': building_num,
        'room_number': room_num,
        'date': property_fee.date.strftime('%Y-%M-%d'),
        'pay_date': property_fee.pay_date.strftime('%Y-%M-%d') if property_fee.ispay else "未支付",
        'pay_amount': property_fee.pay_amount,
        'is_pay': '已支付' if property_fee.ispay else '未支付',
        'order_number': property_fee.order_number
    } for property_fee, building_num, room_num in property_fees]


def get_property_fee(hid: int) -> List[Dict[str, Union[int, str]]]:
    property_fees: List[Tuple[PropertyFeeInformation, str, str]] = db.session.query(
        PropertyFeeInformation,
        HouseInformation.building_number,
        HouseInformation.room_number
    ).filter(
        PropertyFeeInformation.hid == HouseInformation.id,
        PropertyFeeInformation.hid == hid
    ).all()
    return [{
        'id': property_fee.id,
        'building_number': building_num,
        'room_number': room_num,
        'date': property_fee.date.strftime('%Y-%M-%d'),
        'pay_date': property_fee.pay_date.strftime('%Y-%M-%d') if property_fee.ispay else "未支付",
        'pay_amount': property_fee.pay_amount,
        'is_pay': '已支付' if property_fee.ispay else '未支付',
        'order_number': property_fee.order_number
    } for property_fee, building_num, room_num in property_fees]


def get_property_fee_from_username(username: str) -> List[Dict[str, Union[int, str]]]:
    property_fees: List[Tuple[PropertyFeeInformation, str, str]] = db.session.query(
        PropertyFeeInformation,
        HouseInformation.building_number,
        HouseInformation.room_number
    ).filter(
        PropertyFeeInformation.hid == HouseInformation.id,
        PropertyFeeInformation.hid == RH.hid,
        RH.rid == ResidentInformation.id,
        ResidentInformation.username == username
    ).all()
    return [{
        'id': property_fee.id,
        'building_number': building_num,
        'room_number': room_num,
        'date': property_fee.date.strftime('%Y-%M-%d'),
        'pay_date': property_fee.pay_date.strftime('%Y-%M-%d') if property_fee.ispay else "未支付",
        'pay_amount': property_fee.pay_amount,
        'is_pay': '已支付' if property_fee.ispay else '未支付',
        'order_number': property_fee.order_number
    } for property_fee, building_num, room_num in property_fees]
