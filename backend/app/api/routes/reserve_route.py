from flask import Blueprint, request
from app.extensions.jwt import role_required
from app.api.controllers.reserve_controller import (
    get_reserves,
    create_reserve,
    update_reserve,
    delete_reserve,
)

reserve_bp = Blueprint("reserves", __name__)


# @role_required("ADMIN")
@reserve_bp.route("/", methods=["GET"])
def get_all_reserves():
    return get_reserves()


@role_required(["ADMIN", "USER", "STUDENT"])
@reserve_bp.route("/<int:reserve_id>", methods=["GET"])
def get_reserve(reserve_id):
    return get_reserves(reserve_id)


@reserve_bp.route("/", methods=["POST"])
@role_required(["ADMIN", "USER", "STUDENT"])
def add_reserve():
    request_data = request.get_json()
    return create_reserve(request_data)


@reserve_bp.route("/<int:reserve_id>", methods=["PUT"])
@role_required(["ADMIN", "USER", "STUDENT"])
def modify_reserve(reserve_id):
    request_data = request.get_json()
    return update_reserve(reserve_id, request_data)


@reserve_bp.route("/<int:reserve_id>", methods=["DELETE"])
@role_required("ADMIN")
def remove_reserve(reserve_id):
    return delete_reserve(reserve_id)
