import pandas as pd

'''The following commented code is entirely unnecessary as it has been executed and it has been found that everything in the official record of
pincodes has already been captured in our dataset. It has been left here as a PoC.'''

pin_map = dict()
f = open("data/pin_codes.csv", "r")
for line in f:
    list = line.split(",")
    pin_map[list[0]] =list[1].lower()
f.close()
old_pins = pd.read_csv("data/official_india_pin_codes.csv") #received from https://data.gov.in/catalog/all-india-pincode-directory

old_set = set()
for y in old_pins["pincode"]:
    old_set.add(str(y))
print("number in official=", len(old_set))

print("if len(pin_map)==len(old_set.union(pin_map.keys())), then everything in old_set is already captured in pin_map.")
print("if true, ^ : ", len(pin_map)==len(old_set.union(pin_map.keys())))