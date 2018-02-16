
def get_state_to_pin_map():
    """Reads state_pin_map.csv to construct the required map, and returns the dictionary."""
    state_map = dict()
    with open("file_manager/data/state_pin_map.csv") as f:  # Remove "file_manager/" when used from within this package.
        # line = f.readline()
        # while line:
        #     line_list = line.split(",")
        #     state_map[line_list[0]] = line_list[1:]
        #     line = f.readline()
        for line in f:
            line_list = line.strip().split(",")
            state_map[line_list[0]] = line_list[1:]
    return state_map


def get_max_min_for_state():
    """Returns the corresponding max and min points for each triplet
     prefix in the form of a prefix to tuple dictionary."""
    req_map = dict()
    with open("file_manager/data/max_min_map.csv") as f:  # Remove the file_manager when being used within this package
        for line in f:
            line_list = line.strip().split(",")
            req_map[line_list[0]] = (line_list[1], line_list[2])
    return req_map


def get_pin_list(prefix, state_to_pin_map):
    suffixes = state_to_pin_map[prefix]
    pin_list = []
    for suffix in suffixes:
        pin_code = prefix+suffix
        pin_list.append(pin_code)
    return pin_list



