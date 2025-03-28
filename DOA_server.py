from flask import Flask, render_template, jsonify
import usb.core
import usb.util
import time
from tuning import Tuning

app = Flask(__name__)

# Initialize the USB sensor
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
Mic_tuning = None
if dev:
    Mic_tuning = Tuning(dev)
    print("Sensor device found.")
else:
    print("Sensor device not found.")

@app.route('/')
def index():
    return render_template('sonar_counter_clockwise.html')

@app.route('/update')
def update():
    if Mic_tuning:
        # Get the sensor value from the Tuning instance
        sensor_value = Mic_tuning.direction
    else:
        sensor_value = "N/A"
    return jsonify({'data': sensor_value})

if __name__ == '__main__':
    # Make the server available externally on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
