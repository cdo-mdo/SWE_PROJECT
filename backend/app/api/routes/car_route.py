from flask import Blueprint, request
from app.extensions.jwt import role_required
from app.api.controllers.car_controller import (
    get_cars,
    create_car,
    update_car,
    delete_car,
)

car_bp = Blueprint("cars", __name__)


@car_bp.route("/", methods=["GET"])
def get_all_cars():
    return get_cars()


@car_bp.route("/<int:car_id>", methods=["GET"])
def get_car(car_id):
    return get_cars(car_id)


@car_bp.route("/", methods=["POST"])
@role_required("ADMIN")
def add_car():
    request_data = request.get_json()
    return create_car(request_data)


@car_bp.route("/<int:car_id>", methods=["PUT"])
@role_required("ADMIN")
def modify_car(car_id):
    request_data = request.get_json()
    return update_car(car_id, request_data)


@car_bp.route("/<int:car_id>", methods=["DELETE"])
@role_required("ADMIN")
def remove_car(car_id):
    return delete_car(car_id)
