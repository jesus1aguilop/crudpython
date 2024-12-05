from flask import Flask
from app.routes.profesor import profesor_bp
from app.routes.alumno import alumno_bp
from app.routes.asignatura import asignatura_bp 
from app.routes.curso import curso_bp 
from app.routes.matricula import matricula_bp
from app.routes.auth import auth_bp
from app.extensions import db_connection
from app.extensions import session

def create_app():
    app = Flask(__name__)

    # Configuracion de la aplicacion
    app.config.from_pyfile('config.py')
    
    # Conectar a la base de datos
    db_connection.get_connection()
    
    # Inicializa Flask-Session
    session.init_app(app)

    # Registrar blueprints
    app.register_blueprint(profesor_bp)
    app.register_blueprint(alumno_bp)
    app.register_blueprint(asignatura_bp)
    app.register_blueprint(curso_bp)
    app.register_blueprint(matricula_bp)
    app.register_blueprint(auth_bp)

    return app
