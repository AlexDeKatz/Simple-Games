from flask import Response
from hangman import app
from hangman.game.utility import *
import requests
import json

def load_game_controller() -> Response:
    get_word_url = f"http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=5&maxLength=15&limit=1&api_key={app.config['RANDOM_WORD_API_KEY']}"
    try:
        resp = requests.get(get_word_url)
        if resp.status_code != 200:
            raise Exception('Could not fetch word')
        word = resp.json()[0].get('word', None)
        # word = "Captured"        
        if word is None:
            raise Exception('Could not fetch word')
        get_meaning = get_help_controller(word)
        if get_meaning.status_code==404:
            return load_game_controller()
    except Exception as e:
        return Response(json.dumps({'error':str(e)}), status=400, mimetype='application/json')
    else:
        hashed_word = encrypt_message(word)
        return Response(json.dumps({'data':hashed_word}), status=200, mimetype='application/json')


def get_help_controller(word: str) -> Response:
    get_meaning_url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}'
    try:
        meaning = requests.get(get_meaning_url)
        if meaning.status_code != 200:
            return Response(json.dumps(meaning.json()),status=meaning.status_code,mimetype='application/json')
        print(meaning.json())
        data = word_result_parser(meaning.json()[0])
    except Exception as e:
        return Response(json.dumps({'error':"Could not get Help"}), status=400, mimetype='application/json')
    else:
        return Response(json.dumps({'data':data}), status=400, mimetype='application/json')
