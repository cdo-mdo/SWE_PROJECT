from app.app import create_app  # Import create_app from app.py
from app.extensions.database import db
from app.api.models import Car
from seed import seed_cars

app = create_app()  # Create an instance of the Flask app

# Ensure tables exist
with app.app_context():
    db.create_all()

    # Check if the database is empty and seed data
    # if not Car.query.first():
    #     print("Seeding database...")
    #     seed_cars(2) # write two cars to mysql


if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app
