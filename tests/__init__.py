from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app)

# export talisman so tests can import it
__all__ = ['app', 'talisman']
