# Entry point for the Flask app

# create create_pp from app to instantiate app and run it.

from app import create_app

app = create_app()

if (__name__ == "__main__"):
    app.run(debug=True)