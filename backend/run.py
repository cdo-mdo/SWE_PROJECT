from app.app import create_app  # Import create_app from app.py

app = create_app()  # Create an instance of the Flask app

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app
