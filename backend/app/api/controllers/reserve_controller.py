from flask import jsonify
from app.api.services.reserve_service import (
    fetch_reserves,
    add_reserve,
    edit_reserve,
    remove_reserve,
)


def get_reserves(reserve_id=None):
    if reserve_id:
        reserve = fetch_reserves(reserve_id)
        if not reserve:
            return jsonify({"error": "reserve not found"}), 404
        return jsonify(reserve)

    reserves = fetch_reserves()
    return jsonify({"reserves": reserves})


def create_reserve(request_data):
    reserve = add_reserve(request_data)
    return jsonify(reserve), 201


def update_reserve(reserve_id, request_data):
    updated_reserve = edit_reserve(reserve_id, request_data)
    if not updated_reserve:
        return jsonify({"error": "reserve not found"}), 404
    return jsonify(updated_reserve)


def delete_reserve(reserve_id):
    success = remove_reserve(reserve_id)
    if not success:
        return jsonify({"error": "reserve not found"}), 404
    return jsonify({"message": "reserve deleted successfully"})
