from flask import Flask , render_template, make_response, jsonify, Response
from flask_restful import Api, Resource, reqparse
import random
from display import display
import time
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
class dataStream(Resource):
    def get(self):
        def get_numbers():
            while True:
                number1 = random.randint(1, 100)
                number2 = random.randint(1, 100)
                meatProbeDisplays.drawDisplay(number1,number2)
                yield 'data: %s,%s\n\n' % (number1, number2)
                print(number1,number2)
                time.sleep(5)
        return Response(get_numbers(), mimetype='text/event-stream')

api.add_resource(MeatProbe, '/')
api.add_resource(dataStream, '/send_numbers')

if __name__ == '__main__':
    print("here")
    app.run(debug=True, host='192.168.1.16', port=5000)