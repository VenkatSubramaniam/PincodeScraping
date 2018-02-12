from PostOffice import PostOffice
import pandas as pd

office = PostOffice("http://www.citypincode.co.in/")

state_list = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30", "31", "32", "33", "34", "36", "37", "38", "39", "40", "41",
     "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "56", "57", "58", "59", "60", "61", "63", "64", "67", "68", "69", "70", "71", "72", "73", "74", "75",
     "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "92"]


pin_map = dict()
x=0
f = open("pin_codes.csv", "r")
for line in f:
    list = line.split(",")
    pin_map[list[0]] =list[1]
f.close()
print("number in shubh =", len(pin_map))


#
# The following commented code is entirely unnecessary as it has been executed and it has been found that everything in the official record of
# pincodes has already been captured in our dataset. It has been left here as a PoC.
#
# old_pins = pd.read_csv("official_india_pin_codes.csv")
#
# old_set = set()
# for y in x["pincode"]:
#     old_set.add(str(y))
# print("number in official=", len(arr))
#
# print("if len(pin_map)==len(old_set.union(pin_map.keys(), then everything in old_set is already captured in pin_map.")
# print("if true, ^ : ", len(pin_map)==len(old_set.union(pin_map.keys()
#



# does_not_exist=0
# already_captured=0
# newly_captured=0


# false_pincodes = []
#
# for i in state_list:
#     for j in range(10000):
#         pincode = str(j)
#         while len(pincode)<4:
#             pincode = '0' + pincode
#         pincode = i + pincode
#         if pincode not in pin_map:
#             district = office.get_district(pincode)
#             if district!=None:
#                 pin_map[pincode] = district
#                 newly_captured+=1
#                 print("newly_captured =", newly_captured)
#             else: #needs to be moved down as more stuff is let in
#                 does_not_exist+=1
#                 false_pincodes.append(pincode)
#                 print("does_not_exist =", does_not_exist)
#         else:
#             already_captured+=1
#             print("already_captured =", already_captured)

# old_pin_codes = pd.read_csv("pin_codes.csv")


# creating the csv file:
# filename = "pincodes.csv"
# f = open(filename, "w")
# headers = "pincode,district_name,state_name\n"
# f.write(headers)
# for pin in pin_map:
#     f.write(pin+"," +pin_map[pin]+"\n")
# f.close()

# creating the false_pincode csv file:
# filename = "false_pincodes.csv"
# f = open(filename, "w")
# header = "pincode\n"
# f.write(header)
# for pin in false_pincodes:
#   f.write(pin+'\n')
# f.close()
