
def find_error_point(prefix):
    error = int(open("error_record_"+prefix+".csv").readline())
    return error


if __name__ == '__main__':
    print(find_error_point("275"))
