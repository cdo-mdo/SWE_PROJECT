from sqlalchemy import and_

from app.api.models import Car

def get_available_cars(pickup_location, dropoff_location):
    """
    Fetch available cars for the given pickup and dropoff locations.
    """

    cars = Car.query.filter(
        and_(
            Car.pickup_location.ilike(pickup_location),
            Car.dropoff_location.ilike(dropoff_location),
            Car.availability == True
        )
    ).all()

    return cars



    # Mock response with available cars
    # return [
    #     {
    #         "id": 1,
    #         "brand": "Toyota",
    #         "model": "Corolla",
    #         "year": 2022,
    #         "type": "Sedan",
    #         "seats": 5,
    #         "transmission": "Automatic",
    #         "fuel_type": "Petrol",
    #         "price_per_day": 50.00,
    #         "pickup_location": pickup_location,
    #         "dropoff_location": dropoff_location,
    #         "availability": True,
    #         "image_url": "https://example.com/car1.jpg"
    #     },
    #     {
    #         "id": 2,
    #         "brand": "Honda",
    #         "model": "Civic",
    #         "year": 2021,
    #         "type": "Sedan",
    #         "seats": 5,
    #         "transmission": "Manual",
    #         "fuel_type": "Diesel",
    #         "price_per_day": 45.00,
    #         "pickup_location": pickup_location,
    #         "dropoff_location": dropoff_location,
    #         "availability": True,
    #         "image_url": "https://example.com/car2.jpg"
    #     }
    # ]
