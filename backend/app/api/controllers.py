from flask import jsonify
from app.api.services import fetch_car_types, get_available_cars


def get_car_types():
    car_types = fetch_car_types()
    return jsonify({"car_types": car_types})


def find_cars(request_data):
    """
    Process user request and fetch available cars.
    """
    pickup_location = request_data.get("pickup_location")
    dropoff_location = request_data.get("dropoff_location")
    start_date = request_data.get("start_date")
    start_time = request_data.get("start_time")
    end_date = request_data.get("end_date")
    end_time = request_data.get("end_time")

    cars = get_available_cars(pickup_location, dropoff_location)

    car_list = [
        {
            "id": car.id,
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "type": car.type,
            "seats": car.seats,
            "transmission": car.transmission,
            "fuel_type": car.fuel_type,
            "price_per_day": car.price_per_day,
            "pickup_location": car.pickup_location,
            "dropoff_location": car.dropoff_location,
            "availability": car.availability,
            "image_url": car.image_url,
        }
        for car in cars
    ]

    response = {
        "cars": car_list,
        "rental_period": {
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
        },
    }

    return jsonify(response)
