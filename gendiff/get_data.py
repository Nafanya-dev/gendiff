import json


def get_data(path):
    data = open(path)
    extensions = {'json' : parse_json}
    key = path.split('.')[1]
    return extensions[key](data)


def parse_json(data):
    result = json.load(data)
    return result
