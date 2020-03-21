# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

# utanetのurlを入れる
url = 'https://www.uta-net.com/song/167259'
fileName = url.split("/")[4]

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

elms = soup.select("#flash_area")

all_string = ""

for elm in elms:
   all_string += "\n" + elm.text
with open("data/" + fileName + '.txt', 'w') as f:
    f.write(all_string)
