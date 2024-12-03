from flask import Flask
from app.routes import profesor_bp, alumno_bp, asignatura_bp, curso_bp, matricula_bp # Import all blueprints
from app.repositories import Database  # Import Database class

db = Database(host='localhost', user='root', password='', database='universidad_2')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mi_clave_secreta'
    app.register_blueprint(profesor_bp, url_prefix='/profesor')
    db.connect()


    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.close()

    return app