from flask_restful import Api, Resource, reqparse, request
from flask import Flask
import re

app = Flask(__name__)
api = Api(app)


class Sanitize(Resource):


    request_parser = reqparse.RequestParser()

    def checkForSqlInjectChar(inputString):
        return re.search(r'^[a-z0-9A-Z]*$', inputString)

    def post(self):
        data = request.get_json()
        inputString = data['payload']
        if inputString == "":

          return 400
        isSanitized = Sanitize.checkForSqlInjectChar(inputString)
        if isSanitized:
            return {'result': "sanitized"}
        return {'result': "unsanitized"}

api.add_resource(Sanitize, '/v1/sanitized/input')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
