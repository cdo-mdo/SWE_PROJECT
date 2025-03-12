import random
from faker import Faker
from app.app import create_app
from app.extensions.database import db
from app.api.models.car import Car
from app.api.models.car_type import CarType

fake = Faker()


def seed_data(n=2):
    """Seed the database with fake car data."""
    app = create_app()
    with app.app_context():
        for _ in range(n):
            car_types = CarType(
                type=random.choice(["Sedan", "SUV", "Truck", "Convertible"]),
                make=random.choice(["Toyota", "Hyundai"]),
                year=random.choice([2025, 2026]),
            )
            db.session.add(car_types)

        for _ in range(n):
            cars = Car(
                license_plate=random.choice(["LDM123", "URT123", "BRS123", "KSM123"]),
                mileage=random.choice([5, 10]),
                car_type_id=random.choice([1, 2]),
            )

            db.session.add(cars)

        db.session.commit()
        print(f"✅ {n} fake data added to the database!")


if __name__ == "__main__":
    seed_data(1)  # Insert 1 fake cars
