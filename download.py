import urllib
import urllib2

from BeautifulSoup import BeautifulSoup as bs

MAX_PAGES = 50


def get_backgrounds():
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
            urllib.urlretrieve(href, 'fox_backgrounds%s' % href[href.rfind('/'):])


def fetchurl(url):
    response = urllib2.urlopen(url)
    return response.read()


if __name__ == '__main__':
    get_backgrounds()
