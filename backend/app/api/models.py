from app.extensions.database import db
from datetime import datetime
from enum import Enum


class Role(Enum):
    USER = "USER"
    STUDENT = "STUDENT"
    ADMIN = "ADMIN"


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.DateTime)
    ssn = db.Column(db.String(20))
    passport = db.Column(db.String(20))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip = db.Column(db.String(10))


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    person = db.relationship("Person", backref="account", uselist=False)


class Customer(Person):
    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    student_id = db.Column(db.String(20))


class Employee(Person):
    id = db.Column(db.Integer, db.ForeignKey("person.id"), primary_key=True)
    role = db.Column(db.Enum(Role))


class CarType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    make = db.Column(db.String(50))
    year = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "type": self.type, "make": self.make, "year": self.year}


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)
    mileage = db.Column(db.Integer)
    status = db.Column(db.String(20), default="AVAILABLE")
    car_type_id = db.Column(db.Integer, db.ForeignKey("car_type.id"))
    car_type = db.relationship("CarType", backref="cars")


class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    total_cost = db.Column(db.Float)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))


class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    pickup_location = db.Column(db.String(100))
    dropoff_location = db.Column(db.String(100))
    rental_agreement = db.Column(db.String(255))
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(50))
    transaction_id = db.Column(db.String(50), unique=True)
    reserve_id = db.Column(db.Integer, db.ForeignKey("reserve.id"))


class MaintenanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_maintenance_date = db.Column(db.DateTime, default=datetime.utcnow)
    next_maintenance_date = db.Column(db.DateTime)
    maintenance_cost = db.Column(db.Float)
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"))


class Repair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repair_date = db.Column(db.DateTime, default=datetime.utcnow)
    problem = db.Column(db.String(255))
    total_cost = db.Column(db.Float)
    maintenance_record_id = db.Column(
        db.Integer, db.ForeignKey("maintenance_record.id")
    )
