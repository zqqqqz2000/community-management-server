from flask.blueprints import Blueprint
from typing import *

from service.add_parking_spot import add_parking_spot_user as add_parking_spot_user_api
from service.add_parking_spot import add_parking_spot as add_parking_spot_api
from service.delete_parking_spot import delete_parking_spot_user_pr
from service.delete_resident import delete_residents as delete_residents_api
from service.login import property_login
from service.delete_parking_spot import delete_parking_spot as delete_parking_spot_api
from flask import request
from service.add_resident import add_resident as add_resident_api
from service.get_resident import get_all_resident as get_all_resident_api
from service.get_parking_spot import get_all_spot
from utils.token import with_token, tokenize
from service.get_parking_spot import get_parking_spot as get_parking_spot_api

property_management = Blueprint('property', __name__, url_prefix='/property')


@property_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if property_login(username, password):
        token = tokenize({'username': username, 'role': 'property'})
        return {'success': True, 'token': token}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@property_management.route('/add_resident', methods=['POST'])
@with_token
def add_resident(token_data: Dict):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'property':
        username = data['username']
        password = data['password']
        phone_number = data['phone_number']
        name = data['name']
        job = data['job']
        add_resident_api(username, password, phone_number, name, job)
        return {'success': True}
    else:
        return {'success': False, 'info': 'Please login first'}


@property_management.route('/get_all_resident', methods=['POST'])
@with_token
def get_all_resident(token_data: Dict):
    if token_data and token_data['role'] == 'property':
        return {
            'success': True,
            'residents': get_all_resident_api()
        }
    else:
        return {
            'success': False,
            'info': 'Please login first.'
        }


@property_management.route('/delete_residents', methods=['POST'])
@with_token
def delete_residents(token_data: Optional[Dict]):
    if token_data and token_data['role'] == 'property':
        data = request.get_json(silent=True)
        residents_ids = data['residents_id']
        delete_residents_api(residents_ids)
        return {
            'success': True
        }
    else:
        return {
            'success': False,
            'info': 'Please login first.'
        }


@property_management.route('/get_parking_spot', methods=['POST'])
@with_token
def get_parking_spot(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'property':
        return {'success': True, 'parking_spot': get_parking_spot_api(data['username'])}
    else:
        return {'success': False, 'info': 'Please login first'}


@property_management.route('/add_parking_spot_user', methods=['POST'])
@with_token
def add_parking_spot_user(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'property':
        username = data['username']
        parking_spot_number = data['parking_spot_number']
        license_ = data['license']
        try:
            if add_parking_spot_user_api(username, parking_spot_number, license_):
                return {'success': True}
            else:
                return {'success': False, 'info': 'user error'}
        except Exception as ignore:
            return {'success': False, 'info': 'Duplicate license or spot number'}


@property_management.route('/delete_parking_spot_pr', methods=['POST'])
@with_token
def delete_parking_spot_pr(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'property':
        id_ = data['id']
        delete_parking_spot_user_pr(id_)
        return {'success': True}
    else:
        return {'success': False, 'info': 'user error'}


@property_management.route('/get_all_parking_spot', methods=['POST'])
@with_token
def get_all_parking_spot(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    if token_data and token_data['role'] == 'property':
        return {'success': True, 'parking_spots': get_all_spot()}
    else:
        return {'success': False, 'info': 'user error'}


@property_management.route('/delete_parking_spot', methods=['POST'])
@with_token
def delete_parking_spot(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    try:
        if token_data and token_data['role'] == 'property':
            id_ = data['id']
            delete_parking_spot_api(id_)
            return {'success': True}
        else:
            return {'success': False, 'info': 'user error'}
    except Exception as ignore:
        return {'success': False, 'info': 'this parking spot has been used by resident.'}


@property_management.route('/add_parking_spot', methods=['POST'])
@with_token
def add_parking_spot(token_data: Optional[Dict]):
    data = request.get_json(silent=True)
    try:
        if token_data and token_data['role'] == 'property':
            parking_spot_number = data['parking_spot_number']
            license_ = data['license']
            add_parking_spot_api(parking_spot_number, license_)
            return {'success': True}
        else:
            return {'success': False, 'info': 'user error'}
    except Exception as ignore:
        return {'success': False, 'info': 'this parking spot has been used by resident.'}
