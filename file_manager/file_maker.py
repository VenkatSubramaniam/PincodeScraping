from file_manager.file_reader import get_state_to_pin_map
from os import listdir

def make_state_pin_map():
    """Uses the given filename to recreate the state_pin_map.csv, in case there needs to be a more comprehensive list.
    This is also just to show how the original file was created.

    Args:
        filename (str): The name of the file from which state_pin_map.csv will get created.

    Returns:
        Nothing
    """
    pin_list = []
    f = open("pin_codes.csv", "r")
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
        f.write(prefix)
        for suffix in pin_dict[prefix]:
            f.write(","+suffix)
        f.write("\n")
    f.close()

def make_max_min_state_map():
    my_map = get_state_to_pin_map()
    req_map = dict()
    for state in my_map:
        req_map[state] = (min(my_map[state]), max(my_map[state]))
    f = open("data/max_min_map.csv", "w")

    for prefix in req_map:
        f.write(prefix+","+req_map[prefix][0]+","+req_map[prefix][1]+"\n")

    f.close()


def record_error(prefix, suffix):
    """Records the position in the unfortunate event of the process crashing.

    Args:
        prefix (str): The first three digits, representing the key.
        suffix (str): The last three digits, completing each pin code.

    Returns:
        Nothing
    """
    error = "errors/error_record_"
    print("process that was running for pin prefix", prefix,
          "crashed and needs to be restarted at index number", suffix + ".")
    with open(error + prefix + ".csv", "w") as f:
        f.write(suffix)


def record_new_pins(pin_code, district):
    with open("/file_manager/data/my_new_codes.csv", "a") as f:
        f.write(pin_code+","+district+"\n")
    with open("my_new_codes.csv", "a") as f:
        f.write(pin_code+","+district+"\n")


def record_finish(prefix):
    error = "errors/error_record_"
    with open(error + prefix + ".csv", "w") as f:
        f.write("1000")


def reset():
    for filename in listdir("."):
        if filename.endswith(".csv"):
            with open(filename, "w") as f:
                f.write("0")
