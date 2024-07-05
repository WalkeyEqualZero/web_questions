import requests
import json

# print(requests.get('https://walkey.pythonanywhere.com/api/quests/1').json())
js = ("{'001': {'text': 'Лох?', 'answers':"
      " {'да!': '002', 'нет': '003'}, 'image': ''}, '002':"
      " {'text': 'А вчера?', 'answers': {'да!': '004', 'нет':"
      " '005'}, 'image': ''}, '003': {'text': 'ужас', 'answers': {}, 'image': ''},"
      " '004': {'text': 'Молодец', 'answers': {}, 'image': ''}, '005': {'text': 'плохо', 'answers': {}, 'image': ''}}")
# js = js.replace("'", '"')
print(js)


print(requests.post('https://walkey.pythonanywhere.com/api/add', json=js).text)
