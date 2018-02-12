from urllib.request import urlopen as op
from bs4 import BeautifulSoup as soup


class SiteScraper:

    def __init__(self, url):
        self.url = url

    @staticmethod
    def get_site_soup(url):
        html = get_site_html(url)
        page_soup = soup(html, "html.parser")
        return page_soup


# TODO
# Temporarily returning true as default
# Check database, see if the pincode is already loaded in the universal database
def pincode_already_captured():
    return False


# Loads the html
def get_site_html(url):
    if not pincode_already_captured():
        page_html = op(url).read()
        return page_html
    else:
        return None
