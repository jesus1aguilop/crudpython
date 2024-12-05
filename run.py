from app import create_app
from flask_session import Session
from app.extensions import db_connection
import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Create an instance of the application
app = create_app()

# Start the server
if __name__ == "__main__":
    try:
        app.run(debug=True)  # You can enable debug mode if necessary
    finally:
        # Check if the db_connection has a close method before calling it
        if hasattr(db_connection, 'close'):
            db_connection.close()
        else:
            print("db_connection does not have a close method.")
