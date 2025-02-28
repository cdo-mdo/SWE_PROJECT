from app.extensions.database import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    transmission = db.Column(db.String(50), nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    pickup_location = db.Column(db.String(100), nullable=False)
    dropoff_location = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.Boolean, default=True)
    image_url = db.Column(db.String(255), nullable=True)