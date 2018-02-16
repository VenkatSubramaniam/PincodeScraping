from web_scrapers.post_office import PostOffice
from web_scrapers.postal_code_india import PostalCodeIndia
from web_scrapers.pin_net import PinNet
import file_manager.file_reader as fr
import file_manager.file_maker as fm
from multiprocessing import Pool as pl

office = PostOffice()
postal = PostalCodeIndia()
net = PinNet()
state_to_pin_map = fr.get_state_to_pin_map()
max_min_map = fr.get_max_min_for_state()


def exit_handler(prefix, suffix):
    fm.record_error(prefix, suffix)
    print("Program stopped at pin code:", prefix+suffix)


def find_new_pins(prefix):
    my_min_max = max_min_map[prefix]
    pin_list = fr.get_pin_list(prefix, state_to_pin_map)
    suffix = "000"
    print(type(int(my_min_max[1])))
    try:
        try:
            last_checked = int(open("errors/error_record_"+prefix).readline())
        except FileNotFoundError:
            last_checked = int(my_min_max[0])
        for i in range(last_checked, int(my_min_max[1])+50):
            suffix = str(i)
            if len(suffix)>3:
                break
            while len(suffix) < 3:
                suffix = '0' + suffix
            pin_code = prefix + suffix
            print("Currently checking:", pin_code)
            if pin_code not in pin_list:
                # first check at citypincode.co.in
                district = office.get_district(pin_code)
                if district is None: # second check at postalcodeindia.com
                    # This site is probably the best but there are too many issues because it's protected by cloudflare
                    district = postal.get_district(pin_code)
                    if district is None:
                        # third check at pincode.in.net
                        district = net.get_district(pin_code)
                #checked everywhere, if district has now been set, then write it to the file.
                if district is not None:
                    fm.record_new_pins(pin_code, district)
                    # Making the (not so bold) assumption here that not many new pin codes (if at all)
                    # are going to be found, and therefore we will be easily able to fill in the state in the csv.
                    print("found one! It is:", pin_code)
    except:
        exit_handler(prefix, suffix)


if __name__ == '__main__':
    with pl(processes=50) as p:
        p.map(find_new_pins,state_to_pin_map.keys())
