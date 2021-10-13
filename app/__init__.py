from flask import Flask


app = Flask(__name__)
app.config.from_object(app.config)
app.secret_key = "1241251asdas"

from app import routes
from app import user_routes
from app import admin_routes
from app import database