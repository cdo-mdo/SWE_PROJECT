from flask import jsonify
from app.api.services.rate_service import fetch_rates, add_rate, edit_rate, remove_rate


def get_rates(rate_id=None):
    if rate_id:
        rate = fetch_rates(rate_id)
        if not rate:
            return jsonify({"error": "rate not found"}), 404
        return jsonify(rate)

    rates = fetch_rates()
    return jsonify({"rates": rates})


def create_rate(request_data):
    rate = add_rate(request_data)
    return jsonify(rate), 201


def update_rate(rate_id, request_data):
    updated_rate = edit_rate(rate_id, request_data)
    if not updated_rate:
        return jsonify({"error": "rate not found"}), 404
    return jsonify(updated_rate)


def delete_rate(rate_id):
    success = remove_rate(rate_id)
    if not success:
        return jsonify({"error": "rate not found"}), 404
    return jsonify({"message": "rate deleted successfully"})
