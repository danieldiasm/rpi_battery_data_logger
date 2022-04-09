from flask_restful import Resource, reqparse

class Status(Resource):

    # Setup parser
    parser = reqparse.RequestParser()
    
    parse_fields = ['time','status']

    for i in parse_fields:
        parser.add_argument(
            f'{i}',
            type=str,
            required=True
            help=f'The {i} field cannot be blank!'
        )

    def get(self, device_name):
        # It returns the status of device in approximate given hour
        pass

    def post(self, device_name):
        # Adds a status entry on the DB
        pass

class StatusList(Resource):
    def get(self, name):
        # This should list all the statuses for his name (no pagination for now...)
        pass
