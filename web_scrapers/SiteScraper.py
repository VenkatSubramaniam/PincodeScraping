# from urllib.request import urlopen as op
from bs4 import BeautifulSoup as soup
import subprocess


class SiteScraper:

    def __init__(self):
        pass


    @staticmethod
    def get_site_soup(url):
        html = get_site_html(url)
        page_soup = soup(html, "html.parser")
        return page_soup


# Loads the html
def get_site_html(url):
    # page_html = op(url).read()
    # feels like REALLLY bad design :'(
    # using it because internet security is hard to hack through, and curl gets me the html without any issues.
    page_html = subprocess.check_output(['curl', url])
    return page_html
