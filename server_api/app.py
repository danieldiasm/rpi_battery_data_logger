from flask import Flask
from flask_restful import Api

# Local Imports
from db import database
from resources.device import DeviceRegister
from resources.status import Status, StatusList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
api.add_resource(Status, '/status/<string:device_name>')
api.add_resource(StatusList, '/statuslist')
api.add_resource(DeviceRegister, '/devicer-register')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
