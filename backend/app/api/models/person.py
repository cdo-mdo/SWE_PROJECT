from app.extensions.database import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    dob = db.Column(db.DateTime)
    ssn = db.Column(db.String(20))
    passport = db.Column(db.String(20))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip = db.Column(db.String(10))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "ssn": self.ssn,
            "passport": self.passport,
            "phone": self.phone,
            "email": self.email,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
        }
