from app.extensions.database import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    mileage = db.Column(db.Integer)
    status = db.Column(db.String(20), default="AVAILABLE")
    car_type_id = db.Column(db.Integer, db.ForeignKey("car_type.id"))
    car_type = db.relationship("CarType", backref="cars")

    def to_dict(self):
        return {
            "id": self.id,
            "license_plate": self.license_plate,
            "mileage": self.mileage,
            "status": self.status,
            "car_type_id": self.car_type_id,
        }
