from flask import jsonify
from flask_jwt_extended import create_access_token
from app.api.services.account_service import (
    do_login_account,
    do_register_account,
    fetch_accounts,
    add_account,
    edit_account,
    remove_account,
)


def login_account(request_data):
    username = request_data.get("username")
    password = request_data.get("password")

    account = do_login_account(username)

    if account and account.check_password(password):
        access_token = create_access_token(
            identity=str(account.id), additional_claims={"role": account.role.name}
        )
        return jsonify(access_token=access_token), 200

    return jsonify(msg="Invalid username or password"), 401


def register_account(request_data):
    if do_register_account(request_data):
        return jsonify(msg="User created"), 201
    return jsonify(msg="User already exists"), 409


def get_accounts(account_id=None):
    if account_id:
        account = fetch_accounts(account_id)
        if not account:
            return jsonify({"error": "account not found"}), 404
        return jsonify(account)

    accounts = fetch_accounts()
    return jsonify({"accounts": accounts})


def create_account(request_data):
    account = add_account(request_data)
    return jsonify(account), 201


def update_account(account_id, request_data):
    updated_account = edit_account(account_id, request_data)
    if not updated_account:
        return jsonify({"error": "account not found"}), 404
    return jsonify(updated_account)


def delete_account(account_id):
    success = remove_account(account_id)
    if not success:
        return jsonify({"error": "account not found"}), 404
    return jsonify({"message": "account deleted successfully"})
