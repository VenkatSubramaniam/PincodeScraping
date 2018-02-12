from SiteScraper import SiteScraper


class PinNet(SiteScraper):

    def __init__(self, url):
        super().__init__(url)

    def get_soup(self, pincode):
        my_url = self.url+pincode +"/"
        return SiteScraper.get_site_soup(my_url)

    def get_district(self, pincode):
        my_soup = self.get_soup(pincode)
        full_table = my_soup.findAll("table", {"class": "pincode-details"})
        if len(full_table)==0:
            return None
        return full_table[0].getText().split("\n")[1].split("District:")[1].split("State")[0].lower().strip()