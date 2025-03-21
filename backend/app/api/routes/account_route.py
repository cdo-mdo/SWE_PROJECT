from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions.jwt import role_required
from app.api.controllers.account_controller import (
    login_account,
    register_account,
    get_accounts,
    create_account,
    update_account,
    delete_account,
)

account_bp = Blueprint("accounts", __name__)


@account_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@account_bp.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    return login_account(request_data)


@account_bp.route("/register", methods=["POST"])
def register():
    request_data = request.get_json()
    return register_account(request_data)


@account_bp.route("/", methods=["GET"])
@role_required("ADMIN")
def get_all_accounts():
    return get_accounts()


@account_bp.route("/<int:account_id>", methods=["GET"])
@role_required("ADMIN")
def get_account(account_id):
    return get_accounts(account_id)


@account_bp.route("/", methods=["POST"])
@role_required("ADMIN")
def add_account():
    request_data = request.get_json()
    return create_account(request_data)


@account_bp.route("/<int:account_id>", methods=["PUT"])
@role_required("ADMIN")
def modify_account(account_id):
    request_data = request.get_json()
    return update_account(account_id, request_data)


@account_bp.route("/<int:account_id>", methods=["DELETE"])
@role_required("ADMIN")
def remove_account(account_id):
    return delete_account(account_id)
