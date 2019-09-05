from flask import Flask, render_template, jsonify
import serial, time

app = Flask("pepito")
app.static_folder = 'static'
arduino = serial.Serial('/dev/ttyACM0', 9600,  timeout=1)

@app.route('/')
def hello():
    return render_template("main.html")

@app.route('/hola')
def hello2():
    return "ajksdhkasjhdkjhaskjdh"


@app.route('/serial-data')
def serial_data():
    rawString = arduino.readline()
    return jsonify(data = rawString)



if __name__ == '__main__':
    app.run()