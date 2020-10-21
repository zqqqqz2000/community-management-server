from flask.blueprints import Blueprint

from service.property.delete_resident import delete_residents as delete_residents_api
from service.property.login import property_login
from flask import request
from flask import session
from service.property.add_resident import add_resident as add_resident_api
from service.property.get_resident import get_all_resident as get_all_resident_api
from utils.decorator import login_check
from global_var import s

property_management = Blueprint('property', __name__, url_prefix='/property')


@property_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if property_login(username, password):
        token = s.dumps({'username': username}).decode("ascii")
        session['login'] = True
        return {'success': True, 'token': token}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@property_management.route('/add_resident', methods=['POST'])
@login_check
def add_resident(username):
    data = request.get_json(silent=True)
    if username:
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
@login_check
def get_all_resident(username):
    if username:
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
@login_check
def delete_residents(username):
    if username:
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
