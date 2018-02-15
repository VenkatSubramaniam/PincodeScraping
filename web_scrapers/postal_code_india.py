from web_scrapers.SiteScraper import SiteScraper

class PostalCodeIndia(SiteScraper):

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
        for table in full_table:
            #feels gimmicky but it follows a particular format.
            return table.getText().split("\n")[0].split("District:")[1].split("State")[0].strip().lower()
