#!/usr/bin/env python
# coding: utf-8

import requests as r
from PIL import Image
from bs4 import BeautifulSoup

host = 'https://www.spaceweather.com/'
target_url = host
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = r.session()
res = rs.get(target_url, headers=headers)
res.encoding=('utf8')
soup = BeautifulSoup(res.text, 'html.parser')

image_url = soup.find(class_='dailySunTitleText').img['src']
image_url = host + image_url
img = Image.open(r.get(image_url, stream = True).raw)

date = soup.find(class_='dailySunTitleText').text.split(' ')[2:]
fname = '_'.join(date) + 'sun_of_day.gif'
img.save(fname)
