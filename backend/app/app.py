from flask import Flask
from app.extensions.database import db
from app.config.config import Config
from flask_cors import CORS

from app.api.routes import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})

    # Initialize database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(debug=True)
