from app.api.models.car_type import CarType, db


def fetch_car_types(car_type_id=None):
    if car_type_id:
        car_type = CarType.query.get(car_type_id)
        return car_type.to_dict() if car_type else None
    car_types = CarType.query.all()
    return [car_type.to_dict() for car_type in car_types]


def add_car_type(request_data):
    new_car_type = CarType(
        type=request_data["type"],
        make=request_data["make"],
        year=request_data["year"],
    )
    db.session.add(new_car_type)
    db.session.commit()
    return new_car_type.to_dict()


def edit_car_type(car_type_id, request_data):
    car_type = CarType.query.get(car_type_id)
    if not car_type:
        return None

    car_type.type = request_data.get("type", car_type.type)
    car_type.make = request_data.get("make", car_type.make)
    car_type.year = request_data.get("year", car_type.year)

    db.session.commit()
    return car_type.to_dict()


def remove_car_type(car_type_id):
    car_type = CarType.query.get(car_type_id)
    if not car_type:
        return False
    db.session.delete(car_type)
    db.session.commit()
    return True
