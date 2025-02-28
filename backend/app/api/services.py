from app.api.models import Car

def get_available_cars(pickup_location, dropoff_location):
    """
    Fetch available cars for the given pickup and dropoff locations.
    """

    return Car.query.filter_by(
        pickup_location=pickup_location,
        dropoff_location=dropoff_location,
        availability=True
    ).all()
