from hangman import encrptor


def word_result_parser(word_data: dict) -> dict:
    result = {}
    result['phonetics'] = word_data.phonetics[0]
    result['meanings'] = [{'definition': data.get('definition', None), 'example': data.get(
        'example', None)} for data in word_data.get('meanings', {}).get('definitions', None)]
    return result


def encrypt_message(message: str) -> str:
    message_bytes = message.encode('ascii')
    encrypt_data = encrptor.encrypt(message_bytes)
    return encrypt_data.decode('ascii')
