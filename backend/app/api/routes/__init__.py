from flask import Blueprint
from .car_route import car_bp
from .car_type_route import cartype_bp

api_bp = Blueprint("api", __name__)
api_bp.register_blueprint(car_bp, url_prefix="/cars")
api_bp.register_blueprint(cartype_bp, url_prefix="/cartypes")
