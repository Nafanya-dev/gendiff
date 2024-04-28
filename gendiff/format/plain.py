def get_plain_line(data, path=''):
    result = ''
    for key, d in data.items():
        status = (d.get('status', 'unchanged') if
                  isinstance(d, dict) else
                  'unchanged')
        values = ((d['old_value'], d['new_value']) if
                  status == 'changed' else
                  (d.get('value', d),) if isinstance(d, dict) else (d,))
        values = list(map(lambda v: get_plain_line(v, path + f"{key}.") if
                      isinstance(v, dict) and status == 'nested' else
                      '[complex value]' if isinstance(v, dict) else v, values))
        res_string = ''
        if status == 'nested':
            res_string += values[0]
        elif status == 'changed':
            old_value = quotes_for_value(values[0])
            new_value = quotes_for_value(values[1])
            res_string += (f"Property '{path}{key}' was updated. "
                           f"From {old_value} to {new_value}")
        elif status == 'add':
            value = quotes_for_value(values[0])
            res_string += (f"Property '{path}{key}' "
                           f"was added with value: {value}")
        elif status == 'removed':
            res_string += f"Property '{path}{key}' was removed"
        else:
            continue
        transfer = '\n' if len(result) > 0 else ''
        result += transfer + res_string
    return result


def quotes_for_value(value):
    result = value
    if (value != '[complex value]' and value != 'true'
        and value != 'false'
        and value != 'null'
            and type(value) is not int):
        result = f"'{value}'"
    return result
