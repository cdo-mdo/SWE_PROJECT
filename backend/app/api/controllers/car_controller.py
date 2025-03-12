from flask import jsonify
from app.api.services.car_service import fetch_cars, add_car, edit_car, remove_car


def get_cars(car_id=None):
    if car_id:
        car = fetch_cars(car_id)
        if not car:
            return jsonify({"error": "Car not found"}), 404
        return jsonify(car)

    cars = fetch_cars()
    return jsonify({"cars": cars})


def create_car(request_data):
    car = add_car(request_data)
    return jsonify(car), 201


def update_car(car_id, request_data):
    updated_car = edit_car(car_id, request_data)
    if not updated_car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(updated_car)


def delete_car(car_id):
    success = remove_car(car_id)
    if not success:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"message": "Car deleted successfully"})
