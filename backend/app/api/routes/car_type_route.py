from flask import Blueprint, request
from app.extensions.jwt import role_required
from app.api.controllers.car_type_controller import (
    get_car_types,
    create_car_type,
    update_car_type,
    delete_car_type,
)

cartype_bp = Blueprint("cartypes", __name__)


@cartype_bp.route("/", methods=["GET"])
def get_all_car_types():
    return get_car_types()


@cartype_bp.route("/<int:car_type_id>", methods=["GET"])
def get_car_type(car_type_id):
    return get_car_types(car_type_id)


@cartype_bp.route("/", methods=["POST"])
@role_required("ADMIN")
def add_car_type():
    request_data = request.get_json()
    return create_car_type(request_data)


@cartype_bp.route("/<int:car_type_id>", methods=["PUT"])
@role_required("ADMIN")
def modify_car_type(car_type_id):
    request_data = request.get_json()
    return update_car_type(car_type_id, request_data)


@cartype_bp.route("/<int:car_type_id>", methods=["DELETE"])
@role_required("ADMIN")
def remove_car_type(car_type_id):
    return delete_car_type(car_type_id)
