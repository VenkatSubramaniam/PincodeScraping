from SiteScraper import SiteScraper


class PostOffice(SiteScraper):

    def __init__(self, url):
        super().__init__(url)


    # To be filled in to check the validity of the pincode on the page
    # Temporarily returning false as default
    # unnecessary?
    # def is_valid_pincode(pincode):
    #     return True

    def get_soup(self, pincode):
        my_url = self.url+pincode +"/"
        return SiteScraper.get_site_soup(my_url)

#Gets the name of the district once given a valid post office URL whose
#pincode has not yet been captured.
    def get_district(self, pincode):
        my_soup = self.get_soup(pincode)
        full_table = my_soup.findAll("table", {"class": "table"})
        if len(full_table)==1:
            return None
        for table in full_table:
            #feels gimmicky but if the table has "post office" at the beginning, it follows a particular format.
            if table.getText().split("\n")[1].split(":")[0]=='Post Office':
                return table.getText().split("\n")[4].split(":")[1].strip()



office = PostOffice("http://www.citypincode.co.in/")
print(office.get_district("560000"))

