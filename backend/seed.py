import random
from faker import Faker
from app.app import create_app
from app.extensions.database import db
from app.api.models import Car

fake = Faker()

def seed_cars(n=2):
    """Seed the database with fake car data."""
    app = create_app()
    with app.app_context():
        for _ in range(n):
            car = Car(
                brand=random.choice(["Toyota", "Honda", "Ford", "BMW", "Mercedes"]),
                model=fake.word().capitalize(),
                year=fake.random_int(min=2015, max=2023),
                type=random.choice(["Sedan", "SUV", "Truck", "Convertible"]),
                seats=random.choice([2, 4, 5, 7]),
                transmission=random.choice(["Automatic", "Manual"]),
                fuel_type=random.choice(["Petrol", "Diesel", "Electric", "Hybrid"]),
                price_per_day=round(random.uniform(30, 150), 2),
                pickup_location=random.choice(["San Francisco, CA", "Los Angeles, CA", "New York, NY"]),
                dropoff_location=random.choice(["San Francisco, CA", "Los Angeles, CA", "New York, NY"]),
                availability=True,
                image_url=fake.image_url()
            )
            db.session.add(car)
        
        db.session.commit()
        print(f"✅ {n} fake cars added to the database!")

if __name__ == "__main__":
    seed_cars(1)  # Insert 1 fake cars
