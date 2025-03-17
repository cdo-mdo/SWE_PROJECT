from app.extensions.database import db


class Rates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
