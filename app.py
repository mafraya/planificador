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
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
