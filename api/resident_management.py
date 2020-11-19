from flask.blueprints import Blueprint
from typing import *

from service.add_maintenance import add_maintenance
from service.add_resident import add_resident
from service.get_house import get_house_from_resident_username
from service.get_maintenance import get_maintenance_from_username
from service.get_parking_spot_pay import get_parking_spot_pay_all_from_username
from service.get_property_fee import get_property_fee_from_username
from service.login import resident_login
from flask import request
from service.get_parking_spot import get_parking_spot
from service.get_resident import get_resident
from service.parking_spot_pay import parking_spot_pay
from service.property_fee_pay import property_fee_pay
from utils.token import with_token
from global_var import s

resident_management = Blueprint('resident', __name__, url_prefix='/resident')


@resident_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if resident_login(username, password):
        token = s.dumps({'username': username, 'role': 'resident'}).decode("ascii")
        return {'success': True, 'token': token}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@resident_management.route('/get_resident_info', methods=['POST'])
@with_token
def get_resident_info(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        u_info: Dict[str, str] = get_resident(token_data['username'])
        return {'success': True, 'u_info': u_info}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/update_resident_info', methods=['POST'])
@with_token
def update_resident_info(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        add_resident(
            data['username'],
            data['password'],
            data['phone_number'],
            data['name'],
            data['job']
        )
        return {'success': True}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/get_parking_spots', methods=['POST'])
@with_token
def get_parking_spots(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        return {'success': True, 'parking_spots': get_parking_spot(username)}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/get_parking_spots_pay', methods=['POST'])
@with_token
def get_parking_spots_pay(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        return {'success': True, 'parking_spots_pay': get_parking_spot_pay_all_from_username(username)}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/pay_parking_spot', methods=['POST'])
@with_token
def pay_parking_spot(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        pid: int = data['bill_id']
        username: str = token_data['username']
        if parking_spot_pay(pid, username):
            return {'success': True}
        else:
            return {'success': False, 'info': 'bill has been pay'}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/get_houses', methods=['POST'])
@with_token
def get_houses(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        return {'success': True, 'houses': get_house_from_resident_username(username)}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/get_property_fee', methods=['POST'])
@with_token
def get_property_fee(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        return {'success': True, 'property_fees': get_property_fee_from_username(username)}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/pay_property_fee', methods=['POST'])
@with_token
def pay_property_fee(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        pid = data['pid']
        if property_fee_pay(pid, username):
            return {'success': True}
        else:
            return {'success': False, 'info': 'Has been pay.'}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/apply_maintenance', methods=['POST'])
@with_token
def apply_maintenance(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        apply = data['apply']
        add_maintenance(
            apply['hid'],
            apply['apply_date'],
            apply['comment'],
            apply['from_balance']
        )
        return {'success': True}
    else:
        return {'success': False, 'info': 'Please login first'}


@resident_management.route('/get_maintenance', methods=['POST'])
@with_token
def get_maintenance(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'resident':
        username: str = token_data['username']
        return {'success': True, 'maintenance': get_maintenance_from_username(username)}
    else:
        return {'success': False, 'info': 'Please login first'}
