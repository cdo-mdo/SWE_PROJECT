from flask import jsonify
from app.api.services.car_type import (
    fetch_car_types,
    add_car_type,
    edit_car_type,
    remove_car_type,
)


def get_car_types(car_type_id=None):
    if car_type_id:
        car_type = fetch_car_types(car_type_id)
        if not car_type:
            return jsonify({"error": "Car Type not found"}), 404
        return jsonify(car_type)

    car_types = fetch_car_types()
    return jsonify({"cartypes": car_types})


def create_car_type(request_data):
    car_type = add_car_type(request_data)
    return jsonify(car_type), 201


def update_car_type(car_type_id, request_data):
    updated_car_type = edit_car_type(car_type_id, request_data)
    if not updated_car_type:
        return jsonify({"error": "Car Type not found"}), 404
    return jsonify(updated_car_type)


def delete_car_type(car_type_id):
    success = remove_car_type(car_type_id)
    if not success:
        return jsonify({"error": "Car Type not found"}), 404
    return jsonify({"message": "Car Type deleted successfully"})
