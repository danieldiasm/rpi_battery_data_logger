from flask_restful import Resource, reqparse

class DeviceRegister(Resource):
    parser = reqparse.RequestParser()
    parse_fields = ['device_name','device_type','device_model']

    for i in parse_fields:
        parser.add_argument(
            f'{i}',
            type=str,
            required=True
            help=f'The {i} field cannot be blank!'
        )
    
    def post(self):
        data = DeviceRegister.parser.parse_args()

        # TODO Insert logic for register a device on de DB, depends on Model logic
        # Here goes the logic which lookup if the device is already 
        # existent and refuses to create that again returning an error.

        # Here goes the logic that creates the device and return the inserted data.
