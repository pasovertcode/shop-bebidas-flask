from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(app.config)
app.secret_key = os.urandom(24)

from app import routes
from app import user_routes
from app import admin_routes
from app import database