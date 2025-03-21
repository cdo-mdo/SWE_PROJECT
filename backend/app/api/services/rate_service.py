from app.api.models.rate import Rate, db


def fetch_rates(rate_id=None):
    if rate_id:
        rate = Rate.query.get(rate_id)
        return rate.to_dict() if rate else None
    rates = Rate.query.all()
    return [rate.to_dict() for rate in rates]


def add_rate(request_data):
    new_rate = Rate(
        price=request_data["price"],
    )
    db.session.add(new_rate)
    db.session.commit()
    return new_rate.to_dict()


def edit_rate(rate_id, request_data):
    rate = Rate.query.get(rate_id)
    if not rate:
        return None

    rate.price = request_data.get("price", rate.price)

    db.session.commit()
    return rate.to_dict()


def remove_rate(rate_id):
    rate = Rate.query.get(rate_id)
    if not rate:
        return False
    db.session.delete(rate)
    db.session.commit()
    return True
