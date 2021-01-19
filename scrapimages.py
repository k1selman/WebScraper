# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 23:02:10 2021

@author: k1selman
"""

import requests
from bs4 import BeautifulSoup

def getData(url):
    r = requests.get(url)
    return r.text

html = getData("https://en.wikipedia.org/wiki/Main_Page")
s = BeautifulSoup(html, 'html.parser')

for i in s.find_all('img'):
    print(i['src'])