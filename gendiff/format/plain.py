def get_plain_line(data, path=''):
    result = ''
    for key, d in data.items():
        type_ = (d.get('type', 'unchanged') if
                 isinstance(d, dict) else
                 'unchanged')
        values = ((d['old_value'], d['new_value']) if
                  type_ == 'changed' else
                  (d.get('value', d),) if isinstance(d, dict) else (d,))
        values = list(map(lambda v: get_plain_line(v, path + f"{key}.") if
                      isinstance(v, dict) and type_ == 'nested' else
                      build_correct_value(v), values))
        res_string = ''
        if type_ == 'nested':
            res_string += values[0]
        elif type_ != 'unchanged':
            res_string = build_string(values, path, key, type_)
        else:
            continue
        transfer = '\n' if len(result) > 0 else ''
        result += transfer + res_string
    return result


def build_correct_value(value):
    result = f"'{value}'"
    if isinstance(value, dict):
        result = '[complex value]'
    if isinstance(value, bool):
        string_value = str(value)
        result = string_value[0].lower() + string_value[1:]
    if value is None:
        result = 'null'
    if type(value) is int:
        result = value
    return result


def build_string(values, path, key, type_):
    result = "Property "
    if type_ == 'changed':
        old_value = values[0]
        new_value = values[1]
        result += (f"'{path}{key}' was updated. "
                   f"From {old_value} to {new_value}")
    elif type_ == 'add':
        result += (f"'{path}{key}' "
                   f"was added with value: {values[0]}")
    else:
        result += f"'{path}{key}' was removed"
    return result
