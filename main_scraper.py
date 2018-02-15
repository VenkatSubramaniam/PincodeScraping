from web_scrapers.post_office import PostOffice
from web_scrapers.postal_code_india import PostalCodeIndia
from web_scrapers.pin_net import PinNet
import atexit
from random import randint

office = PostOffice()
postal = PostalCodeIndia()
net = PinNet()

# state_list = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30", "31", "32", "33", "34", "36", "37", "38", "39", "40", "41","42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "56", "57", "58", "59", "60", "61", "63", "64", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "92"]
#
# pin_map = dict()
# f = open("data/pin_codes.csv", "r")
# for line in f:
#     list = line.split(",")
#     pin_map[list[0]] =list[1].lower()
# f.close()
#
#
# last_checked = int(open("data/last_checked").readlines())
#
# f = open("data/my_pin_codes.csv", "a")
# f_closed = False
# false_pins = open("data/false_pincodes.csv", "a")
# false_pins_closed = False
#
#
# @atexit.register
# def exit_handler():
#     open("data/last_checked", "w").write(str(last_checked))
#     print("Program stopped at pin code:", last_checked)
#     f.close()
#     false_pins.close()
#
#
# last_prefix = int(last_checked[0])
# last_suffix = int(last_checked[1])
#
# for state in (state_list[state_list.index(last_prefix):]):
#     null_count = 0
#     for j in range(last_suffix, 10000):
#         last_suffix += 1
#         pin_code = str(j)
#         while len(pin_code)<4:
#             pin_code = '0' + pin_code
#         pin_code = state + pin_code
#         print("Currently checking:", pin_code)
#         if pin_code not in pin_map:
#             # first check at citypincode.co.in
#             district = office.get_district(pin_code)
#             if district is None:
#                 # second check at postalcodeindia.com
#                 # This site is probably the best but there are too many issues because it's protected by cloudflare
#                 district = postal.get_district(pin_code)
#
#                 if district is None:
#                     # third check at pincode.in.net
#                     district = net.get_district(pin_code)
#             # checked everywhere, if district has now been set, then write it to the file.
#             if district is not None:
#                 # Making the (not so bold) assumption here that not many new pin codes (if at all)
#                 # are going to be found, and therefore we will be easily able to fill in the state in the csv.
#                 f.write(pin_code + "," + district + "\n")
#                 print("found one! It is:", pin_code)
#             else:
#                 null_count += 1
#                 false_pins.write(pin_code + "\n")
#             if null_count == 5:
#                 last_suffix += randint(100, 150);  null_count = 0
#             if last_suffix
#
# #I know this is bad style but I'm preparing for any possible eventuality
# # except:
# #     exit_handler()
#
# if not f_closed:
#     f.close()
# if not false_pins_closed:
#     false_pins.close()
#
# # if __name__=='__main__':
# #     atexit.register(exit_handler())
