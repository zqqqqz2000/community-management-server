from flask import Flask
from flask_cors import CORS
from api.property_management import property_management
from global_var import db
import config

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*', supports_credentials=True)


def development_init():
    # development sql init
    from dao.resident_information import ResidentInformation
    from dao.property_management_information import PropertyManagementInformation


def init():
    app.register_blueprint(property_management)


development_init()
init()

with app.app_context():
    db.init_app(app=app)
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run()
