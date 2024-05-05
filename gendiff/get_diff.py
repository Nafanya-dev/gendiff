def get_diff(file1, file2):
    old_keys = list(file1.keys())
    new_keys = list(file2.keys())
    keys = sorted(set(old_keys + new_keys))
    result = {}

    for key in keys:
        old_value = file1.get(key)
        new_value = file2.get(key)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            result[key] = {'type': 'nested',
                           'value': get_diff(old_value, new_value)}
        elif key in old_keys and key not in new_keys:
            result[key] = {'type': 'removed', 'value': old_value}
        elif key in new_keys and key not in old_keys:
            result[key] = {'type': 'add', 'value': new_value}
        elif old_value == new_value:
            result[key] = {'type': 'unchanged', 'value': new_value}
        else:
            result[key] = {'type': 'changed', 'old_value': old_value,
                           'new_value': new_value}
    return result
