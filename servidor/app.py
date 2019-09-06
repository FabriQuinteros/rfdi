# -*- coding: utf-8 -*-
import serial, time
from flask import Flask, render_template, jsonify, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import ResponseForm
from config import Config


app = Flask("pepito")
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models



arduino = None

preguntas = [
    {
        'pregunta': '¿Cuantas horas al dia usas el celular?',
        'respuestas': [
            'Mas de 8hs al día',
            '5hs a 6hs al día',
            '4hs al día',
            'Menos de 3hs al día'
        ]   
    },
    {
        'pregunta': '¿Cuantas horas le dedicas a las redes sociales?',
        'respuestas': [
            'Más de 5hs al día',
            'Entre 4hs a 5hs al día',
            '3hs al día',
            'Menos de 3hs al día'
        ]   
    },
    {
        'pregunta': '¿Antes de dormir usas el celular?',
        'respuestas': [
            'Sí',
            'No',
        ]   
    },
    {
        'pregunta': '¿Las tecnologias juegan un papel importante en tu vida?',
        'respuestas': [
            'Sí',
            'No',
        ]   
    },

    
]


@app.route('/')
def hello():
    return redirect('/pregunta/0')

@app.route('/pregunta/<id_pregunta>', methods=["GET", "POST"])
def hello2(id_pregunta):
    print "Id pregunta : %s"%id_pregunta
    id_pregunta = int(id_pregunta)
    if id_pregunta < 0 or id_pregunta >= len(preguntas):
        return abort(404)
    
    form = ResponseForm()
    if form.validate_on_submit():
        r = models.Respuesta(pregunta=id_pregunta, respuesta=form.respuesta.data)
        db.session.add(r)
        db.session.commit()
        id_pregunta = id_pregunta + 1
        if id_pregunta >= 4:
            return redirect('/')
        else: 
            return redirect('/pregunta/%i'%id_pregunta)

    pregunta = preguntas[id_pregunta]
    respuestas = [x.decode('utf8') for x in pregunta['respuestas']]
    return render_template("pregunta.html", pregunta = pregunta['pregunta'].decode('utf8'), respuestas = respuestas, id_pregunta=id_pregunta, form=form)


@app.route('/stats/')
def stats():
    respuestas1 = []
    respuestas2 = []
    respuestas3 = []
    respuestas4 = []
    for i in range(1, 5):
        cant_respuestas = len(models.Respuesta.query.filter(models.Respuesta.pregunta==0).filter(models.Respuesta.respuesta==i).all())
        respuestas1.append(cant_respuestas)
    
    respuestas2 = []
    for i in range(1, 5):
        cant_respuestas = len(models.Respuesta.query.filter(models.Respuesta.pregunta==1).filter(models.Respuesta.respuesta==i).all())
        respuestas2.append(cant_respuestas)

    for i in range(1, 3):
        cant_respuestas = len(models.Respuesta.query.filter(models.Respuesta.pregunta==2).filter(models.Respuesta.respuesta==i).all())
        respuestas3.append(cant_respuestas)

    for i in range(1, 3):
        cant_respuestas = len(models.Respuesta.query.filter(models.Respuesta.pregunta==3).filter(models.Respuesta.respuesta==i).all())
        respuestas4.append(cant_respuestas)



    return render_template("stats.html", respuestas1=respuestas1)


def dame_respuestas(id_pregunta):
    Res




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