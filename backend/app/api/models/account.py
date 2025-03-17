from app.extensions.database import db
from enum import Enum


class ROLE(Enum):
    USER = "USER"
    STUDENT = "STUDENT"
    ADMIN = "ADMIN"


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    role = db.Column(db.Enum(ROLE), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    person = db.relationship("Person", backref="account", uselist=False)
