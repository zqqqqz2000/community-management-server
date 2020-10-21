from flask import Flask
from flask import session
from flask_cors import CORS
from random import randint

app = Flask(__name__)
app.secret_key = str(randint(1000000000, 9999999999))
CORS(app, resources=r'/*', supports_credentials=True)


@app.route('/')
def hello_world():
    session['fuck'] = '10'
    return 'Hello World!'


@app.route('/test')
def test():
    print(session['fuck'])
    return 'ffff'


if __name__ == '__main__':
    app.run()
