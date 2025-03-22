from flask import jsonify
from app.api.services.rental_service import (
    fetch_rentals,
    add_rental,
    edit_rental,
    remove_rental,
)


def get_rentals(rental_id=None):
    if rental_id:
        rental = fetch_rentals(rental_id)
        if not rental:
            return jsonify({"error": "rental not found"}), 404
        return jsonify(rental)

    rentals = fetch_rentals()
    return jsonify({"rentals": rentals})


def create_rental(request_data):
    rental = add_rental(request_data)
    return jsonify(rental), 201


def update_rental(rental_id, request_data):
    updated_rental = edit_rental(rental_id, request_data)
    if not updated_rental:
        return jsonify({"error": "rental not found"}), 404
    return jsonify(updated_rental)


def delete_rental(rental_id):
    success = remove_rental(rental_id)
    if not success:
        return jsonify({"error": "rental not found"}), 404
    return jsonify({"message": "rental deleted successfully"})
