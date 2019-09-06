from flask import Flask, render_template, jsonify
import serial, time


app = Flask("pepito")
app.static_folder = 'static'
arduino = serial.Serial('/dev/ttyACM0', 9600,  timeout=1)

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
    rawString = arduino.readline()
    return jsonify(data = rawString)



if __name__ == '__main__':
    app.run()