import serial, time
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask("pepito")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

arduino = None


@app.route('/')
def hello():
    return render_template("main.html")

@app.route('/pregunta2')
def hello2():
    return render_template("pregunta2.html")

@app.route('/pregunta3')
def hello3():
    return render_template("pregunta3.html")

@app.route('/pregunta4')
def hello4():
    return render_template("pregunta4.html")


@app.route('/serial-data')
def serial_data():
    rawString = ''
    if arduino != None:
        rawString = arduino.readline()
    return jsonify(data = rawString)



if __name__ == '__main__':
    try:
        arduino = serial.Serial('/dev/ttyACM0', 9600,  timeout=1)
    except serial.serialutil.SerialException:
        print "ERROR: no se pudo abrir puerto /dev/ttyACM0"
    app.run()