# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

print('J-LyricのURLを入力してください')

url = input()

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

elms = soup.select("#Lyric")

for elm in elms:
    print(elm.text)
