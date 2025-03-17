import random
from faker import Faker
from werkzeug.security import generate_password_hash
from datetime import timedelta
from app.app import create_app
from app.extensions.database import db
from app.api.models.car import Car
from app.api.models.car_type import CarType
from app.api.models.person import Person
from app.api.models.account import Account, ROLE
from app.api.models.reserve import Reserve, RESERVE_STATUS
from app.api.models.rental import Rental, RENTAL_STATUS

fake = Faker()


def seed_data(n=2):
    """Seed the database with fake car data."""
    app = create_app()
    with app.app_context():
        for _ in range(n):
            car_types = CarType(
                type=fake.random.choice(["Sedan", "SUV", "Truck", "Convertible"]),
                make=random.choice(
                    ["Toyota", "Hyundai", "BMW", "Subaru", "Mercedes benz"]
                ),
                year=random.choice([2025, 2026]),
            )
            db.session.add(car_types)
        db.session.commit()

        car_types = [car_type.id for car_type in CarType.query.all()]
        for _ in range(n):
            cars = Car(
                license_plate=fake.license_plate(),
                mileage=random.choice([5, 10]),
                status=random.choice(["AVAILABLE", "RENTED", "MAINTENANCE"]),
                car_type_id=random.choice(car_types),
            )

            db.session.add(cars)

        for _ in range(n):
            person = Person(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                dob=fake.date_of_birth(minimum_age=18, maximum_age=80),
                ssn=fake.unique.ssn(),
                passport=fake.unique.passport_number(),
                phone=fake.unique.phone_number(),
                email=fake.unique.email(),
                street=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zip=fake.zipcode(),
            )
            db.session.add(person)
            db.session.flush()  # Ensure person ID is available

            # Create account with a random role
            username = f"{person.first_name.lower()}{random.randint(100, 999)}"
            password = generate_password_hash("password123")
            role = random.choice(list(ROLE))

            account = Account(
                username=username,
                password_hash=password,
                role=role,
                person_id=person.id,
            )
            db.session.add(account)

        db.session.commit()

        ## RESERVE
        accounts = [account.id for account in Account.query.all()]
        cars = [car.id for car in Car.query.all()]

        if not accounts or not cars:
            print("No accounts or cars available in the database.")
            return

        for _ in range(n):
            reservation = Reserve(
                total_cost=round(random.uniform(50, 500), 2),
                reserve_status=random.choice(list(RESERVE_STATUS)),
                account_id=random.choice(accounts),
                car_id=random.choice(cars),
            )
            db.session.add(reservation)

        ## Rental
        for _ in range(n):
            start_time = fake.date_time_between(start_date="-1y", end_date="now")
            end_time = (
                start_time + timedelta(days=random.randint(1, 10))
                if random.random() > 0.5
                else None
            )
            rental = Rental(
                start_time=start_time,
                end_time=end_time,
                pickup_location=fake.address(),
                dropoff_location=fake.address(),
                rental_agreement=fake.text(max_nb_chars=200),
                rental_status=random.choice(list(RENTAL_STATUS)),
                account_id=random.choice(accounts),
                car_id=random.choice(cars),
            )
            db.session.add(rental)

        db.session.commit()

        print(f"✅ {n} fake data added to the database!")


if __name__ == "__main__":
    seed_data(1)  # Insert 1 fake cars
