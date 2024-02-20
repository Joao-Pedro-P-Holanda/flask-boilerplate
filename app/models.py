from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()

def config_db(app):
    db.init_app(app)
    app.db = db
    with app.app_context():
        db.create_all()


class Person(db.Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
