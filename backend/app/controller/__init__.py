from flask import Blueprint
from flask_restx import Api
from .coffee import api as coffee_ns


blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="Smart Coffee", version="1.0", description="IoT project for DHBW"
)

api.add_namespace(coffee_ns, path="/coffee")


