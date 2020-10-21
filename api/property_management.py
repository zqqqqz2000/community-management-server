import flask
from flask.blueprints import Blueprint
from service.property.login import property_login
from flask import request
from flask import session
from service.property.add_resident import add_resident as add_resident_api
from service.property.get_resident import get_all_resident as get_all_resident_api

property_management = Blueprint('property', __name__, url_prefix='/property')
# CORS(property_management, resources=r'/*', supports_credentials=True)


@property_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    # sessionid: str = 0 if 'sessionid' not in data else data['sessionid']
    if property_login(username, password):
        session['login'] = True
        return {'success': True, 'sessionid': session.sid}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}


@property_management.route('/add_resident', methods=['POST'])
def add_resident():
    data = request.get_json(silent=True)
    if 'sessionid' in data:
        session.sid = data['sessionid']
    print(session)
    print(session.sid)
    if 'login' in session and session['login']:
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
def get_all_resident():
    if 'login' in session and session['login']:
        return {
            'success': True,
            'residents': get_all_resident_api()
        }
    else:
        return {
            'success': False,
            'info': 'Please login first.'
        }
