from flask import Response
from hangman import logger,app
from hangman.game.utility import word_result_parser
import requests
import json

def load_game_controller() -> Response:
    get_word_url = f"http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=5&maxLength=15&limit=1&api_key={app.config['RANDOM_WORD_API_KEY']}"
    try:
        resp = requests.get(get_word_url)
        if resp.status_code != 200:
            raise Exception('Could not fetch word')
        print(resp.json())
        logger.info("Hello world")
        word = resp.json()[0].get('word', None)
        print(word)
        if word is None:
            raise Exception('Could not fetch word')
    except Exception as e:
        print("Error: ",e)
        return Response(json.dumps({'error':str(e)}), status=400, mimetype='application/json')
    else:
        return Response(json.dumps({'data':word}), status=200, mimetype='application/json')


def get_help_controller(word: str) -> Response:
    get_meaning_url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}'
    try:
        meaning = requests.get(get_meaning_url)
        if meaning.status_code != 200:
            raise Exception('Could not fetch help')
        print(meaning.json())
        data = word_result_parser(meaning.json()[0])
    except Exception as e:
        return Response(json.dumps({'error':str(e)}), status=400, mimetype='application/json')
    else:
        return Response(json.dumps({'data':data}), status=400, mimetype='application/json')
