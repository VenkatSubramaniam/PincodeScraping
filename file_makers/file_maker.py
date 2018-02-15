
def make_state_pin_map(filename):
    """Uses the given filename to recreate the state_pin_map.csv, in case there needs to be a more comprehensive list.
    This is also just to show how the original file was created."""
    pin_list = []
    f = open(filename, "r")
    for line in f:
        all_pins = line.split(",")
        pin_list.append(all_pins[0])
    f.close()

    pin_dict = dict()
    for pin in pin_list:
        if pin[:3] in pin_dict:
            pin_dict[pin[:3]].append(pin[3:])
        else:
            pin_dict[pin[:3]] = [pin[3:]]

    f = open("data/state_pin_map.csv", "w")

    for prefix in pin_dict:
        f.write(prefix+",")
        for suffix in pin_dict[prefix]:
            f.write(suffix+",")
        f.write("\n")
    f.close()
