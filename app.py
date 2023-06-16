from flask import Flask , render_template, make_response, jsonify, Response
from flask_restful import Api, Resource, reqparse
import random ,time, threading , queue
import busio
from board import SCL, SDA
from display import display

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('number', type=int)

# set up i2c devices
i2c = busio.I2C(SCL, SDA)
meatProbeDisplays = display(i2c=i2c)
probeTempsQueue = queue.Queue()
number1 = 0
number2 = 0
lock = threading.Lock()
updateRate = 5
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
                   yield 'data: %s,%s\n\n' % (number1, number2)
                   time.sleep(5)                
                
                
        return Response(get_numbers(), mimetype='text/event-stream')
def displayProbeValues():
    global number1
    global number2
    global updateRate
    with lock:
        while True:
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 100)
            meatProbeDisplays.drawDisplay(number1,number2)
            probeTempsQueue.put((number1, number2))
            time.sleep(updateRate)
# Start the background thread when the application starts
thread = threading.Thread(target=displayProbeValues)
thread.daemon = True
thread.start()
api.add_resource(MeatProbe, '/')
api.add_resource(dataStream, '/send_numbers')

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.16', port=5000)