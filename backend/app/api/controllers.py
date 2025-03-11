from flask import jsonify
from app.api.services import (
    fetch_car_types,
    fetch_cars,
    fetch_rates,
    fetch_customers,
    fetch_empolyees,
    fetch_reserves,
    fetch_rentals,
    fetch_payments,
)


def get_cars(request_data):
    cars = fetch_cars()
    return jsonify({"cars": cars})


def get_car_types():
    car_types = fetch_car_types()
    return jsonify({"cartypes": car_types})


def get_rates():
    rates = fetch_rates()
    return jsonify({"rates": rates})


def get_customers(request_data):
    customers = fetch_customers()
    return jsonify({"customers": customers})


def get_employees(request_data):
    employees = fetch_empolyees()
    return jsonify({"employees": employees})


def get_reserves(request_data):
    reserves = fetch_reserves()
    return jsonify({"reserves": reserves})


def get_rentals(request_data):
    rentals = fetch_rentals()
    return jsonify({"rentals": rentals})


def get_payments(request_data):
    payments = fetch_payments()
    return jsonify({"payments": payments})
