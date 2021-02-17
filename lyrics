import requests
import urllib.parse
import re
from bs4 import BeautifulSoup

answer = input("제목 입력:")
url = urllib.parse.quote(answer)
html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=' + url).text
soup = BeautifulSoup(html, 'html.parser')

song_lyrics = str(soup.select('.text_expand span[class*=_text]'))
cleaned_lyrics = re.sub('(<([^>]+)>)', '\n', song_lyrics, 0).strip()

print(cleaned_lyrics)
