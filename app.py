from flask import Flask , render_template, make_response, jsonify, Response
from flask_restful import Api, Resource, reqparse
import random
from display import display

app = Flask(__name__)
api = Api(app)
meatProbeDisplays = display()
parser = reqparse.RequestParser()
parser.add_argument('number', type=int)

class MeatProbe(Resource):
    def get(self):
        return make_response(render_template('index.html'))
    def put(self):
        args = parser.parse_args()
        number = args['number']
        return {'number': number}
    def number(self):
        number = random.randint(1, 100)
        return number
class Data(Resource):
    def get(self):
        number = random.randint(1, 100)
        meatProbeDisplays.drawDisplay(number,(number+1))
        return jsonify({'number':number})
api.add_resource(MeatProbe, '/')
api.add_resource(Data,'/number')


if __name__ == '__main__':
    print("here")
    app.run(debug=True, host='192.168.1.16', port=5000)