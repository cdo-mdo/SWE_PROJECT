from app.api.models.reserve import Reserve, db


def fetch_reserves(reserve_id=None):
    if reserve_id:
        reserve = Reserve.query.get(reserve_id)
        return reserve.to_dict() if reserve else None
    reserves = Reserve.query.all()
    return [reserve.to_dict() for reserve in reserves]


def add_reserve(request_data):
    new_reserve = Reserve(
        price=request_data["price"],
    )
    db.session.add(new_reserve)
    db.session.commit()
    return new_reserve.to_dict()


def edit_reserve(reserve_id, request_data):
    reserve = Reserve.query.get(reserve_id)
    if not reserve:
        return None

    reserve.price = request_data.get("price", reserve.price)

    db.session.commit()
    return reserve.to_dict()


def remove_reserve(reserve_id):
    reserve = Reserve.query.get(reserve_id)
    if not reserve:
        return False
    db.session.delete(reserve)
    db.session.commit()
    return True
