from flask import Blueprint
from .car_route import car_bp
from .car_type_route import cartype_bp
from .rate_route import rate_bp
from .account_route import account_bp
from .rental_route import rental_bp
from .reserve_route import reserve_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(car_bp, url_prefix="/cars")
api_bp.register_blueprint(cartype_bp, url_prefix="/cartypes")
api_bp.register_blueprint(rate_bp, url_prefix="/rates")
api_bp.register_blueprint(account_bp, url_prefix="/accounts")
api_bp.register_blueprint(rental_bp, url_prefix="/rentals")
api_bp.register_blueprint(reserve_bp, url_prefix="/reserves")
