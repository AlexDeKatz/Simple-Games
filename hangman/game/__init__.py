from flask import Blueprint
game_inst = Blueprint('game', __name__)

from hangman.game import routes