from flask import Flask
from flask_jwt_extended import JWTManager
from routes import bp as routes_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
