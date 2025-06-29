from db import db
import json

class TrainingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20))
    numero_sesion = db.Column(db.String(10))
    tipo_dia = db.Column(db.String(20))
    duracion = db.Column(db.Integer)
    observaciones = db.Column(db.Text)
    data_json = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "numeroSesion": self.numero_sesion,
            "tipoDia": self.tipo_dia,
            "duracion": self.duracion,
            "observaciones": self.observaciones,
            "datos": json.loads(self.data_json)
        }
