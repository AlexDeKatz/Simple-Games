def word_result_parser(word_data):
    result = {}
    result['phonetics'] = word_data.phonetics[0]
    result['meanings'] = [{'definition': data.get('definition', None), 'example': data.get(
        'example', None)} for data in word_data.get('meanings', {}).get('definitions', None)]
    return result
