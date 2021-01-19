# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:16:52 2021

@author: k1selman

------------------------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup



ht = urlopen('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')

bs = BeautifulSoup(ht.read(), 'html.parser')

print(bs.h3)

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    ht = urlopen('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')
except HTTPError as e:
    print(e)
except URLError as e:
    print("Server could not be found...")
else:
    print("Working fine, proceeding...")
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    
    try:
        data = BeautifulSoup(html.read(), 'html.parser')
        title = data.body.h1
    except AttributeError:
        return None
    return title


title = getTitle('https://en.wikipedia.org/wiki/Main_Page')
if title == None:
    print('Could not find title...')
else:
    print(title)

