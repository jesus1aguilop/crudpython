from app import create_app  # Suponiendo que tienes una función 'create_app' en tu 'app.py'

# Crear una instancia de la aplicación
app = create_app()

# Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)  # Puedes activar el modo de depuración si es necesario
