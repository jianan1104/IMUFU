#!/usr/bin/env python
# coding: utf-8
import requests as r
from PIL import Image
from bs4 import BeautifulSoup

host = 'https://apod.nasa.gov/apod/'
target = 'astropix.html'
target_url = host + target
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = r.session()
res = rs.get(target_url, headers=headers)
res.encoding=('utf8')
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.title.string
image_url = soup.find('img')['src']
image_url = host + image_url
img = Image.open(r.get(image_url, stream = True).raw)

date = soup.p.p.text.strip()
date = date.replace(' ', '_')
fname = date + '_moon_of_day.jpg'
img.save(fname)
