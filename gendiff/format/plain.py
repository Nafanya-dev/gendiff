def get_plain_line(data, path=''):
    result = ''
    for key, d in data.items():
        desc = (d.get('desc', 'unchanged') if
                isinstance(d, dict) else
                'unchanged')
        values = ((d['old_value'], d['new_value']) if
                  desc == 'changed' else
                  (d.get('value', d),) if isinstance(d, dict) else (d,))
        values = list(map(lambda v: get_plain_line(v, path + f"{key}.") if
                      isinstance(v, dict) and desc == 'nested' else
                      '[complex value]' if isinstance(v, dict) else v, values))
        res_string = ''
        if desc == 'nested':
            res_string += values[0]
        elif desc == 'changed':
            old_value = quotes_for_value(values[0])
            new_value = quotes_for_value(values[1])
            res_string += (f"Property '{path}{key}' was updated. "
                           f"From {old_value} to {new_value}\n")
        elif desc == 'add':
            value = quotes_for_value(values[0])
            res_string += (f"Property '{path}{key}' "
                           f"was added with value: {value}\n")
        elif desc == 'removed':
            res_string += f"Property '{path}{key}' was removed\n"
        else:
            continue
        result += res_string
    return result


def quotes_for_value(value):
    result = f"'{value}'"
    if (value == '[complex value]' or value == 'true' or
            value == 'false' or value == 'null'):
        result = value
    return result
