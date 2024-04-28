import json


def get_json_line(diff):
    return json.dumps(diff, indent=4)
