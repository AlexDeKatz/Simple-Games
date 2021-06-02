from hangman.game import game_inst
from flask import Flask
from hangman.logger import get_logger

app = Flask(__name__)
app.config.from_pyfile('../environment.cfg')
app.register_blueprint(game_inst)
logger = get_logger()
