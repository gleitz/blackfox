import os
import requests

from BeautifulSoup import BeautifulSoup as bs

MAX_PAGES = 20
SAVE_DIR = 'fox_backgrounds'

def get_backgrounds():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    base = 'http://www.thefoxisblack.com/category/the-desktop-wallpaper-project/page/%s/'
    for x in range(0, MAX_PAGES):
        get_images_from_page(base % (x + 1))


def get_images_from_page(url):
    html = fetchurl(url)
    soup = bs(html)
    for link in soup.findAll('a'):
        href = link['href']
        if '-1440x900' in href:
            print 'Downloading %s' % href
            r = requests.get(href)
            with open('fox_backgrounds%s' % href[href.rfind('/'):], 'wb') as f:
                f.write(r.content)

def fetchurl(url):
    return requests.get(url).text


if __name__ == '__main__':
    get_backgrounds()
