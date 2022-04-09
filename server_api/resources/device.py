from __future__ import division
from flask_restful import Resource, reqparse
from itsdangerous import base64_encode

# Devices
devices = []
class DeviceRegister(Resource):
    parser = reqparse.RequestParser()
    parse_fields = ['device_alias', 'device_model']

    for i in parse_fields:
        parser.add_argument(
            f'{i}',
            type=str,
            required=True
            help=f'The {i} field cannot be blank!'
        )
    
    def post(self):
        data = DeviceRegister.parser.parse_args()
        global devices

        device_name = data['device_alias'] + "_" + str(base64_encode(data['device_alias'] + data['device_model']))
        
        # Check if it exists on DB

        # Create if doesn't and return device name to be used later



        
