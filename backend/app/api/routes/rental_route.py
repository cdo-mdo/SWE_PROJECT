from flask import Blueprint, request
from app.extensions.jwt import role_required
from app.api.controllers.rental_controller import (
    get_rentals,
    create_rental,
    update_rental,
    delete_rental,
)

rental_bp = Blueprint("rentals", __name__)


# @role_required("ADMIN")
@rental_bp.route("/", methods=["GET"])
def get_all_rentals():
    return get_rentals()


@role_required(["ADMIN", "USER", "STUDENT"])
@rental_bp.route("/<int:rental_id>", methods=["GET"])
def get_rental(rental_id):
    return get_rentals(rental_id)


@rental_bp.route("/", methods=["POST"])
@role_required(["ADMIN", "USER", "STUDENT"])
def add_rental():
    request_data = request.get_json()
    return create_rental(request_data)


@rental_bp.route("/<int:rental_id>", methods=["PUT"])
@role_required(["ADMIN", "USER", "STUDENT"])
def modify_rental(rental_id):
    request_data = request.get_json()
    return update_rental(rental_id, request_data)


@rental_bp.route("/<int:rental_id>", methods=["DELETE"])
@role_required("ADMIN")
def remove_rental(rental_id):
    return delete_rental(rental_id)
