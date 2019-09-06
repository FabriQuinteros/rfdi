from app import db

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.Integer, index=True)
    respuesta = db.Column(db.Integer, index=True)
        