"""
to create simple api in flask framework
"""
import re
from flask import Flask
from flask_restful import Api, Resource, reqparse, request

APP = Flask(__name__)
API = Api(APP)

class Sanitize(Resource):
    """  to create rest api for http post """
    request_parser = reqparse.RequestParser()

    def check_for_sql_inject_char(input_string):
        """To check for sql inject char for the given input """
        return re.search(r'^[a-z0-9A-Z]*$', input_string)

    def post(self):
        data = request.get_json()
        input_string = data['payload']
        if input_string == "":
            return 'bad request!', 400

        is_sanitized = Sanitize.check_for_sql_inject_char(input_string)
        if is_sanitized:
            return {'result': "sanitized"}
        return {'result': "unsanitized"}


API.add_resource(Sanitize, '/v1/sanitized/input')

if __name__ == '__main__':
    APP.run(port=5000, debug=True)
