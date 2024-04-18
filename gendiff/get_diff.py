def get_diff(file1, file2):
    old_keys = list(file1.keys())
    new_keys = list(file2.keys())
    keys = sorted(set(old_keys + new_keys))
    result = {}

    for key in keys:
        old_value = check_value(file1.get(key))
        new_value = check_value(file2.get(key))

        if type(old_value) == dict and type(new_value) == dict:
            result[key] = {'desc': 'nested', 'value': get_diff(old_value, new_value)}
        elif key in old_keys and key not in new_keys:
            result[key] = {'desc': 'removed', 'value': old_value}
        elif key in new_keys and key not in old_keys:
            result[key] = {'desc': 'add', 'value': new_value}
        elif key in new_keys and key in old_keys:
            if old_value == new_value:
                result[key] = {'desc': 'unchanged', 'value': new_value}
            else:
                result[key] = {'desc': 'changed',
                               'old_value': old_value,
                               'new_value': new_value}
    return result


def check_value(value):
    result = value
    if type(value) == bool:
        string_value = str(value)
        result = string_value[0].lower() + string_value[1:]
    return result