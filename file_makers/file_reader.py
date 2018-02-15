
def get_state_to_pin_map():
    """Reads state_pin_map.csv to construct the required map, and returns the dictionary."""
    state_map = dict()
    with open("data/state_pin_map.csv") as f:
        line = f.readline()
        while line:
            line_list = line.split(",")
            state_map[line_list[0]] = line_list[1:]
    return state_map

