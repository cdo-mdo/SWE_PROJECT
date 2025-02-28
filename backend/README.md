## Install
```
python3 -m venv env
pip3 install -r requirements
python3 run.py
```

## Backend Folder Structures
```
/backend/
│── /app/                  # Main application package
│   │── /api/              # API-related modules
│   │   │── __init__.py
│   │   │── routes.py      # Route definitions
│   │   │── controllers.py # Business logic
│   │   │── models.py      # Database models (SQLAlchemy)
│   │   │── schemas.py     # Request/response validation (Marshmallow)
│   │   │── services.py    # Business logic and services
│   │   │── utils.py       # Utility/helper functions
│   │
│   │── /config/           # Configuration files
│   │   │── __init__.py
│   │   │── config.py      # App settings (e.g., dev, prod, test)
│   │
│   │── /extensions/       # Flask extensions
│   │   │── __init__.py
│   │   │── database.py    # Database setup
│   │   │── cache.py       # Caching setup (e.g., Redis)
│   │   │── jwt.py         # JWT authentication setup
│   │
│   │── /blueprints/       # API Blueprints for modularity
│   │   │── __init__.py
│   │   │── auth.py        # Authentication routes
│   │   │── users.py       # User-related routes
│   │
│   │── /tests/            # Unit and integration tests
│   │   │── __init__.py
│   │   │── test_users.py
│   │   │── test_auth.py
│   │
│   │── __init__.py
│   │── app.py             # Application entry point
│
│── /migrations/           # Database migrations (Alembic/Flask-Migrate)
│── /venv/                 # Virtual environment (optional)
│── .env                   # Environment variables
│── requirements.txt       # Python dependencies
│── run.py                 # Script to start the app
│── README.md              # Project documentation
```