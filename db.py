from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    from models.session import TrainingSession
    db.create_all()
