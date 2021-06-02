from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../environment.cfg')

from hangman.logger import get_logger
logger = get_logger()

from hangman.game import game_inst
app.register_blueprint(game_inst)

