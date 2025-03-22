## Set Up a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

## Install Dependencies
```
pip3 install -r requirements.txt
```

## Run the Setup Script
```
./setup_env.sh
```

## Running the API
```
python3 run.py
```


## Backend Folder Structures
```
/backend/
│── /app/                  # Main application package
│   │── /api/              # API-related modules
│   │   │── routes         # Route definitions
│   │   │── controllers    # Business logic
│   │   │── models         # Database models (SQLAlchemy)
│   │   │── services       # Business logic and services
│   │   │── utils          # Utility/helper functions
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
│── seed.py                # Add data
│── README.md              # Project documentation
```

## An example from client registration to the rental process
### Client register
![client register](https://github.com/cdo-mdo/SWE_PROJECT/blob/main/backend/screenshots/1.register.png?raw=true)
### Client login
![client login](https://github.com/cdo-mdo/SWE_PROJECT/blob/main/backend/screenshots/2.login.png?raw=true)
### Client show cars
![show cars](https://github.com/cdo-mdo/SWE_PROJECT/blob/main/backend/screenshots/3.get_cars.png?raw=true)
### After selecting a car, the client submits their details.
![rental](https://github.com/cdo-mdo/SWE_PROJECT/blob/main/backend/screenshots/4.create_rental.png?raw=true)
