from app.extensions.database import db


class Rate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "price": self.price}
