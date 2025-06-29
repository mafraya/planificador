from flask import Flask
from flask_cors import CORS
from db import db, init_db
from routes.sessions import session_bp

app = Flask(__name__)
app.config.from_object("config.Config")
CORS(app)

db.init_app(app)
app.register_blueprint(session_bp, url_prefix="/api/sessions")

with app.app_context():
    init_db()
