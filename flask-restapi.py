from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import requests
import urllib.parse
import re
from bs4 import BeautifulSoup
app =  Flask(__name__)
api = Api(app)

class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type = str)
        args = parser.parse_args()

        title = args['title']

        url = urllib.parse.quote(title)
        html = requests.get(
            'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + url).text
        soup = BeautifulSoup(html, 'html.parser')

        song_lyrics = str(soup.select('.text_expand span[class*=_text]'))
        cleaned_lyrics = re.sub('(<([^>]+)>)', '\n', song_lyrics, 0).strip()
        return {'lyrics': cleaned_lyrics}

api.add_resource(RegistUser, '/user')
if __name__ =='__main__':
    app.run(debug=True)
