from urllib.request import urlopen as op
from bs4 import BeautifulSoup as soup

class PostOffice:
    url = "http://www.citypincode.co.in/"

    #TODO
    #Temporarily returning false as default
    #Check database, see if the pincode is already loaded in the universal database

    def pincode_already_captured(self):
        return False


    #Loads the html
    def get_site_html(pincode, self):
            if not self.pincode_already_captured:
                myURL = PostOffice.url+pincode
                page_html = op(myURL).read()
                return page_html
            else:
                return None

    #to be filled in to check the validity of the pincode on the page
    #Temorarily returning false as default
    #TODO
    def is_valid_pincode(self):
        return False

#Gets the name of the district once given a valid post office URL whose
#pincode has not yet been captured.
    def getDistrict(self):
        if self.is_valid_pincode():


