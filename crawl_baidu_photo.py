"""
这是一个爬取百度图片的程序，根据搜索词下载百度图片
"""
import requests
import re
import os

"""初始化爬取百度图片网址"""
URL_INIT_FIRST = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='

"""爬取搜索到的前十张图片"""
CRAWL_COUNT = 10

"""得到图片的url"""
def get_photo_urls(url):
    try:
        html = requests.get(url)
        html.encoding = 'utf-8'
        html = html.text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)[:10]
    return pic_urls

"""根据地址下载图片"""
def down_photo(photo_url,keyword):
    for i, pic_url in enumerate(photo_url):
        try:
            pic = requests.get(pic_url, timeout=15)
            if not os.path.isdir("static/img/" + keyword):
                os.mkdir("static/img/" + keyword)
            string = 'static/img/' + keyword + '/' + keyword + '_' + str(i + 1) + '.jpg'
            with open(string, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue

"""根据keyword下载"""
def down_by_keyword(keyword):
    url = URL_INIT_FIRST + keyword
    photo_urls = get_photo_urls(url)
    all_photo_urls = []
    for i in photo_urls:
        all_photo_urls.append(i)
    down_photo(list(set(all_photo_urls)),keyword)


