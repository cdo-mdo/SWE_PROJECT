from sqlalchemy import and_

from app.api.models import (
    Car,
    CarType,
    Rates,
    Customer,
    Employee,
    Reserve,
    Rental,
    Payment,
)


def fetch_cars(pickup_location, dropoff_location):
    cars = Car.query.all()
    return [car.to_dict() for car in cars]


def fetch_car_types():
    carTypes = CarType.query.all()
    return [car.to_dict() for car in carTypes]


def fetch_rates():
    rates = Rates.query.all()
    return [rate.to_dict() for rate in rates]


def fetch_customers():
    customers = Customer.query.all()
    return [customer.to_dict() for customer in customers]


def fetch_empolyees():
    empolyees = Employee.query.all()
    return [empolyee.to_dict() for empolyee in empolyees]


def fetch_reserves():
    reserves = Reserve.query.all()
    return [reserve.to_dict() for reserve in reserves]


def fetch_rentals():
    rentals = Rental.query.all()
    return [rentals.to_dict() for rental in rentals]


def fetch_payments():
    payments = Payment.query.all()
    return [payments.to_dict() for payment in payments]
