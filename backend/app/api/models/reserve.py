from app.extensions.database import db
from enum import Enum


class RESERVE_STATUS(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_cost = db.Column(db.Float)
    reserve_status = db.Column(db.Enum(RESERVE_STATUS), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
