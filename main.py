"""App Entrance"""

from flask import Flask
from flask_cors import CORS

from app.routes import page_blueprint
from app.routes.authentication import authentication_blueprint
from app.config.error_handler import register_error_handler

app = Flask(__name__)
CORS(app)

app.register_blueprint(page_blueprint)
app.register_blueprint(authentication_blueprint, url_prefix="/api")


register_error_handler(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
