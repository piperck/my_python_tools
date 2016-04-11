# coding: utf-8
import requests
import simplejson

url = "http://api.xiachufang.com/v2/recipes/autocomplete-categories.json"
r = requests.get(url)
print r.text



print simplejson.dumps([{'id': 52449, 'name': u'\u4e2d\u5f0f\u65e9\u9910'}, {'id': 52448, 'name': u'\u5feb\u624b\u65e9\u9910'}, {'id': 52450, 'name': u'\u897f\u5f0f\u65e9\u9910'}])