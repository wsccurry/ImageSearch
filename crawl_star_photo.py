"""根据百度图片爬取具体的内地明星照片"""

import crawl_baidu_photo
from bs4 import BeautifulSoup
import urllib.request
import os

"""漫漫看网站的内地明星花名册"""
STAR_URL = 'http://www.manmankan.com/dy2013/mingxing/neidi/#'

"""得到各个明星的名字并将其作为关键字在百度图片查询下载到本地"""
f = urllib.request.urlopen(STAR_URL)
response = f.read()
soup = BeautifulSoup(response,'html.parser')
star_names = set()
for k in soup.find_all('a'):
    if '.shtml'in k['href'] and k.string!=None:
        star_names.add(k.string)
star_names = list(star_names)

"""
for name in star_names:
    crawl_baidu_photo.down_by_keyword(name)
"""

"""还没下载完，下载完后删掉此代码，将上面的代码注释去掉"""
files = os.listdir("static/img/")
for name in star_names:
    if name not in files:
        crawl_baidu_photo.down_by_keyword(name)
