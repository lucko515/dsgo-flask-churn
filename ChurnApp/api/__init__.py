from flask import Blueprint

bp = Blueprint("api", __name__)

from ChurnApp.api import routes
