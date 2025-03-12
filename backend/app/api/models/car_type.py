from app.extensions.database import db


class CarType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    make = db.Column(db.String(50))
    year = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "type": self.type, "make": self.make, "year": self.year}
