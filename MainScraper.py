from WebScrapers.post_office import PostOffice
from WebScrapers.postal_code_india import PostalCodeIndia
from WebScrapers.pin_net import PinNet
import atexit
# import pandas as pd

office = PostOffice("http://www.citypincode.co.in/")
postal = PostalCodeIndia("https://www.postalcodeindia.com/")
net = PinNet("https://pincode.net.in/")

state_list = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30", "31", "32", "33", "34", "36", "37", "38", "39", "40", "41","42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "56", "57", "58", "59", "60", "61", "63", "64", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "92"]


pin_map = dict()
f = open("data/pin_codes.csv", "r")
for line in f:
    list = line.split(",")
    pin_map[list[0]] =list[1].lower()
f.close()


#
# The following commented code is entirely unnecessary as it has been executed and it has been found that everything in the official record of
# pincodes has already been captured in our dataset. It has been left here as a PoC.
#
# old_pins = pd.read_csv("official_india_pin_codes.csv") #received from https://data.gov.in/catalog/all-india-pincode-directory
#
# old_set = set()
# for y in x["pincode"]:
#     old_set.add(str(y))
# print("number in official=", len(arr))
#
# print("if len(pin_map)==len(old_set.union(pin_map.keys(), then everything in old_set is already captured in pin_map.")
# print("if true, ^ : ", len(pin_map)==len(old_set.union(pin_map.keys()
#

last_checked = int(open("data/last_checked").readline())

f = open("data/my_pin_codes.csv", "a")
f_closed = False
false_pins = open("data/false_pincodes.csv", "a")
false_pins_closed = False


@atexit.register
def exit_handler():
    open("data/last_checked", "w").write(str(last_checked))
    print("Program stopped at pin code:", last_checked)
    f.close()
    false_pins.close()


try:
    for i in state_list:
        for j in range(last_checked, 10000):
            last_checked += 1
            pin_code = str(j)
            while len(pin_code)<4:
                pin_code = '0' + pin_code
            pin_code = i + pin_code
            print("Currently checking:", pin_code)
            if pin_code not in pin_map:
                # first check at citypincode.co.in
                district = office.get_district(pin_code)
                if district is None:
                    # second check at postalcodeindia.com
                    # This site is probably the best but there are too many issues because it's protected by cloudflare
                    district = postal.get_district(pin_code)

                    if district is None:
                        # third check at pincode.in.net
                        district = net.get_district(pin_code)
                # checked everywhere, if district has now been set, then write it to the file.
                if district is not None:
                    # Making the (not so bold) assumption here that not many new pin codes (if at all)
                    # are going to be found, and therefore we will be easily able to fill in the state in the csv.
                    f.write(pin_code + "," + district + "\n")
                else:
                    false_pins.write(pin_code + "\n")

#I know this is bad style but I'm preparing for any possible eventuality
except:
    exit_handler()

if not f_closed:
    f.close()
if not false_pins_closed:
    false_pins.close()