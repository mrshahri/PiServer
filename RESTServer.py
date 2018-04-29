from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class MachineStatus(Resource):
    def get(self, machine_id):
        result = {'data': machine_id}
        return jsonify(result)

    def post(self, machine_id):
        result = {'data': machine_id}
        return jsonify(result)

api.add_resource(MachineStatus, '/machines/<machine_id>')

if __name__ == '__main__':
    app.run(port='10090')