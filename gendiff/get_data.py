from gendiff.parser import parse


def get_data(path):
    format = path.split('.')[1]
    with open(path) as data:
        return parse(data, format)
