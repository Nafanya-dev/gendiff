import json
import yaml


def get_data(path):
    EXTENSIONS = {'json': parse_json, 'yaml': parse_yaml, 'yml': parse_yaml}
    data = open(path)
    key = path.split('.')[1]
    return EXTENSIONS[key](data)


def parse_json(data):
    result = json.load(data)
    return result


def parse_yaml(data):
    result = yaml.safe_load(data)
    return result
