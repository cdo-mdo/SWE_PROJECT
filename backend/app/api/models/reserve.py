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
    car = db.relationship("Car", backref="reserves")
    account = db.relationship("Account", backref="reserves")

    def to_dict(self):
        return {
            "id": self.id,
            "total_cost": self.total_cost,
            "reserve_status": self.reserve_status.value,
            "car_id": self.car_id,
            "account_id": self.account_id,
            "car": self.car.to_dict() if self.car else None,
            "account": self.account.to_dict() if self.account else None,
        }
