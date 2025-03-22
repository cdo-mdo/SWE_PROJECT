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
    car = db.relationship("Car", backref="accounts")
    account = db.relationship("Account", backref="accounts")

    def to_dict(self):
        return {
            "id": self.id,
            "start_date": self.start_time,
            "end_date": self.end_time,
            "pickup_location": self.pickup_location,
            "dropoff_location": self.dropoff_location,
            "rental_agreement": self.rental_agreement,
            "rental_status": self.rental_status.value,
            "car_id": self.car_id,
            "account_id": self.account_id,
            "car": self.car.to_dict() if self.car else None,
            "account": self.account.to_dict() if self.account else None,
        }
