from flask import Blueprint, request, jsonify
from models.session import TrainingSession
from db import db
import json

session_bp = Blueprint("sessions", __name__)

@session_bp.route("/", methods=["GET"])
def get_sessions():
    sessions = TrainingSession.query.all()
    return jsonify([s.to_dict() for s in sessions])

@session_bp.route("/<int:id>", methods=["GET"])
def get_session_by_id(id):
    session = TrainingSession.query.get(id)
    if session:
        return jsonify(session.to_dict())
    return jsonify({"error": "Sesión no encontrada"}), 404

@session_bp.route("/", methods=["POST"])
def create_session():
    data = request.json
    session = TrainingSession(
        fecha=data.get("fecha"),
        numero_sesion=data.get("numeroSesion"),
        tipo_dia=data.get("tipoDia"),
        duracion=data.get("duracionTotal"),
        observaciones=data.get("observaciones"),
        data_json=json.dumps(data)
    )
    db.session.add(session)
    db.session.commit()
    return jsonify(session.to_dict()), 201
