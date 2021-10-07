from flask import Flask

app = Flask(__name__)

from app import routes
from app import user_routes
from app import admin_routes
from app import database