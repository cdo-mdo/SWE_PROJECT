from flask import Blueprint, request
from app.api.controllers import (
    get_cars,
    get_car_types,
    get_customers,
    get_employees,
    get_reserves,
    get_rentals,
    get_payments,
    get_rates,
)

api_bp = Blueprint("api", __name__)


@api_bp.route("/cars", methods=["GET"])
def cars():
    request_data = request.get_json()
    return get_cars(request_data)


@api_bp.route("/car/types", methods=["GET"])
def car_types():
    return get_car_types()


@api_bp.route("/rates", methods=["GET"])
def rates():
    return get_rates()


@api_bp.route("/customers", methods=["GET"])
def customers():
    return get_customers()


@api_bp.route("/employees", methods=["GET"])
def employees():
    return get_employees()


@api_bp.route("/reserves", methods=["GET"])
def reserves():
    return get_reserves()


@api_bp.route("/reserves", methods=["GET"])
def rentals():
    return get_rentals()


@api_bp.route("/payments", methods=["GET"])
def payments():
    return get_payments()
