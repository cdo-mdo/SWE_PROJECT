from app.api.models.account import Account, ROLE, db
from app.api.models.person import Person
from werkzeug.security import generate_password_hash


def do_login_account(username):
    account = Account.query.filter_by(username=username).first()
    return account


def do_register_account(request_data):
    username = request_data["username"]
    password = request_data["password"]
    role = request_data.get("role", "USER")

    if Account.query.filter_by(username=username).first():
        return False

    new_user = Account(username=username, role=ROLE[role])
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return True


def fetch_accounts(account_id=None):
    if account_id:
        account = Account.query.get(account_id)
        return account.to_dict() if account else None
    accounts = Account.query.all()
    return [account.to_dict() for account in accounts]


def add_account(request_data):
    person = Person()
    db.session.add(person)
    db.session.flush()
    new_account = Account(
        username=request_data["username"],
        password_hash=generate_password_hash(request_data["password123"]),
        role=request_data.get("role", "USER"),
        person_id=person.id,
    )
    db.session.add(new_account)
    db.session.commit()
    return new_account.to_dict()


def edit_account(account_id, request_data):
    account = Account.query.get(account_id)
    if not account:
        return None

    account.username = request_data.get("username", account.username)
    account.role = request_data.get("role", account.role)
    if "password_hash" in request_data:
        account.password_hash = generate_password_hash(
            request_data.get("password_hash", account.password_hash)
        )

    db.session.commit()
    return account.to_dict()


def remove_account(account_id):
    account = Account.query.get(account_id)
    if not account:
        return False
    db.session.delete(account)
    db.session.commit()
    return True
