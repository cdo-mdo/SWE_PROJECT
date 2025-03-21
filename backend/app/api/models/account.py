from app.extensions.database import db
from werkzeug.security import generate_password_hash, check_password_hash
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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role.value,
            "person": self.person.to_dict() if self.person else None,
        }
