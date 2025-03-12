from app.api.models.car import Car, db


def fetch_cars(car_id=None):
    if car_id:
        car = Car.query.get(car_id)
        return car.to_dict() if car else None
    cars = Car.query.all()
    return [car.to_dict() for car in cars]


def add_car(request_data):
    new_car = Car(
        license_plate=request_data["license_plate"],
        mileage=request_data.get("mileage", 0),
        status=request_data.get("status", "AVAILABLE"),
        car_type_id=request_data["car_type_id"],
    )
    db.session.add(new_car)
    db.session.commit()
    return new_car.to_dict()


def edit_car(car_id, request_data):
    car = Car.query.get(car_id)
    if not car:
        return None

    car.license_plate = request_data.get("license_plate", car.license_plate)
    car.mileage = request_data.get("mileage", car.mileage)
    car.status = request_data.get("status", car.status)
    car.car_type_id = request_data.get("car_type_id", car.car_type_id)

    db.session.commit()
    return car.to_dict()


def remove_car(car_id):
    car = Car.query.get(car_id)
    if not car:
        return False
    db.session.delete(car)
    db.session.commit()
    return True
