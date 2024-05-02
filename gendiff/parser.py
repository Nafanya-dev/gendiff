import json
import yaml


def parse(data, format):
    EXTENSIONS = {'json': parse_json, 'yaml': parse_yaml, 'yml': parse_yaml}
    return EXTENSIONS[format](data)


def parse_json(data):
    result = json.load(data)
    return result


def parse_yaml(data):
    result = yaml.safe_load(data)
    return result
