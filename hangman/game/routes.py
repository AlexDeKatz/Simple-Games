from hangman.game.controller import *
from hangman.game import game_inst

@game_inst.get('/game')
def load_game():
    return load_game_controller()

@game_inst.get('/game/help/<string:word>')
def get_help(word):
    return get_help_controller(word)

