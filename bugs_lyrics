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
        html = requests.get('https://music.bugs.co.kr/search/integrated?q=' + url).text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.select('.lyrics .title a')
        artist = soup.select('.lyrics .artist a')
        titles = []
        artists = []
        numbers = []
        for i in range(0, 5):
            numbers.append(soup.select('tr .lyrics a')[i]['href'])

        for i in title:
            titles.append(i.text)

        print('----------------------')
        for i in artist:
            artists.append(i.text)
        return {'result': {'titles': titles, 'artists': artists, 'numbers': numbers }}

api.add_resource(RegistUser, '/user')
if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
