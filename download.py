import urllib
import urllib2

from BeautifulSoup import BeautifulSoup as bs

def get_backgrounds():
    base = 'http://www.thefoxisblack.com/category/the-desktop-wallpaper-project/page/%s/'
    for x in range(0, 40):
        get_images_from_page(base % (x + 1))

def get_images_from_page(url):
    html = fetchurl(url)
    soup = bs(html)
    print soup
    for link in soup.findAll('a'):
        href = link['href']
        if '-1440x900' in href:
            print 'Downloading %s' % href
            urllib.urlretrieve(href, '/Users/bgleitzman/Desktop/fox_backgrounds%s' % href[href.rfind('/'):])

def fetchurl(url):
    response = urllib2.urlopen(url)
    return response.read()

if __name__ == '__main__':
    get_backgrounds()
