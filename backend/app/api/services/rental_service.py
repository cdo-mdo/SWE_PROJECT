from app.api.models.rental import Rental, db


def fetch_rentals(rental_id=None):
    if rental_id:
        rental = Rental.query.get(rental_id)
        return rental.to_dict() if rental else None
    rentals = Rental.query.all()
    return [rental.to_dict() for rental in rentals]


def add_rental(request_data):
    new_rental = Rental(
        start_time=request_data["start_time"],
        end_time=request_data["end_time"],
        pickup_location=request_data["pickup_location"],
        dropoff_location=request_data["dropoff_location"],
        rental_agreement=request_data.get("rental_agreement", ""),
        rental_status=request_data["rental_status"],
        car_id=request_data["car_id"],
        account_id=request_data["account_id"],
    )
    db.session.add(new_rental)
    db.session.commit()
    return new_rental.to_dict()


def edit_rental(rental_id, request_data):
    rental = Rental.query.get(rental_id)
    if not rental:
        return None

    rental.price = request_data.get("price", rental.price)
    rental.start_time = request_data.get("start_time", rental.start_timte)
    rental.end_time = request_data.get("end_time", rental.end_time)
    rental.pickup_location = request_data.get("pickup_location", rental.pickup_location)
    rental.dropoff_location = request_data.get(
        "dropoff_location", rental.dropoff_location
    )
    rental.rental_agreement = request_data.get(
        "rental_agreement", rental.rental_agreement
    )
    rental.rental_status = request_data.get("rental_status", rental.rental_status)
    rental.car_id = request_data.get("car_id", rental.car_id)
    rental.account_id = request_data.get("account_id", rental.account_id)

    db.session.commit()
    return rental.to_dict()


def remove_rental(rental_id):
    rental = Rental.query.get(rental_id)
    if not rental:
        return False
    db.session.delete(rental)
    db.session.commit()
    return True
