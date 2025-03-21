from flask import Blueprint, request
from app.extensions.jwt import role_required
from app.api.controllers.rate_controller import (
    get_rates,
    create_rate,
    update_rate,
    delete_rate,
)

rate_bp = Blueprint("rates", __name__)


@rate_bp.route("/", methods=["GET"])
def get_all_rates():
    return get_rates()


@rate_bp.route("/<int:rate_id>", methods=["GET"])
def get_rate(rate_id):
    return get_rates(rate_id)


@rate_bp.route("/", methods=["POST"])
@role_required("ADMIN")
def add_rate():
    request_data = request.get_json()
    return create_rate(request_data)


@rate_bp.route("/<int:rate_id>", methods=["PUT"])
@role_required("ADMIN")
def modify_rate(rate_id):
    request_data = request.get_json()
    return update_rate(rate_id, request_data)


@rate_bp.route("/<int:rate_id>", methods=["DELETE"])
@role_required("ADMIN")
def remove_rate(rate_id):
    return delete_rate(rate_id)
