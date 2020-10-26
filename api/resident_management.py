from flask.blueprints import Blueprint
from typing import *

from service.add_resident import add_resident
from service.login import resident_login
from flask import request
from service.get_parking_spot import get_parking_spot
from service.get_resident import get_resident
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
