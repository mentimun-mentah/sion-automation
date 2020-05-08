from flask import Flask
from services.config import Production

app = Flask(__name__)
app.config.from_object(Production)

from services.resources.sion.route import sions
app.register_blueprint(sions)
