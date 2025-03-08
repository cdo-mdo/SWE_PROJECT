from flask import Blueprint, request
from app.api.controllers import get_car_types, find_cars

api_bp = Blueprint("api", __name__)


@api_bp.route("/cars", methods=["POST"])
def get_cars():
    request_data = request.get_json()
    return find_cars(request_data)


@api_bp.route("/car/types", methods=["GET"])
def car_types():
    return get_car_types()
