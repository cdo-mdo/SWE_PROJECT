import random
from faker import Faker
from app.app import create_app
from app.extensions.database import db
from app.api.models import Car, CarType

fake = Faker()


def seed_cars(n=2):
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

        db.session.commit()
        print(f"✅ {n} fake cars added to the database!")


if __name__ == "__main__":
    seed_cars(1)  # Insert 1 fake cars
