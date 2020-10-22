from flask.blueprints import Blueprint
from service.property.login import property_login
from flask import request
from utils.decorator import login_check
from global_var import s

property_management = Blueprint('resident', __name__, url_prefix='/resident')


@property_management.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    username: str = data['username']
    password: str = data['password']
    if property_login(username, password):
        token = s.dumps({'username': username, 'role': 'resident'}).decode("ascii")
        return {'success': True, 'token': token}
    else:
        return {'success': False, 'info': 'username or password incorrect.'}
