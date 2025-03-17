from datetime import datetime
from app.extensions.database import db
from enum import Enum


class RENTAL_STATUS(Enum):
    OPEN = "OPEN"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    pickup_location = db.Column(db.String(100))
    dropoff_location = db.Column(db.String(100))
    rental_agreement = db.Column(db.String(255))
    rental_status = db.Column(db.Enum(RENTAL_STATUS), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
