CHARS = {'removed': '-', 'add': '+', 'unchanged': ' '}


def get_stylish_line(data, count_spaces=2):
    result = ''
    spaces = ' ' * count_spaces
    for key, d in data.items():
        type_ = (d.get('type', 'unchanged') if
                 isinstance(d, dict) else
                 'unchanged')
        values = ((d['old_value'], d['new_value']) if
                  type_ == 'changed' else
                  d.get('value', d) if isinstance(d, dict) else d)
        res_string = ''

        if type_ == 'nested':
            value = get_stylish_line(values, count_spaces + 4)
            res_string = build_value(value, key, ' ', spaces)
        elif type_ == 'changed':
            first_value = (get_stylish_line(values[0], count_spaces + 4) if
                           isinstance(values[0], dict) else
                           values[0])
            second_value = (get_stylish_line(values[1], count_spaces + 4) if
                            isinstance(values[1], dict) else
                            values[1])

            res_string = (build_value(first_value, key, CHARS['removed'],
                                      spaces) + build_value(second_value,
                                                            key, CHARS['add'],
                                                            spaces))
        else:
            value = (get_stylish_line(values, count_spaces + 4) if
                     isinstance(values, dict) else
                     values)

            res_string = build_value(value, key, CHARS[type_], spaces)
        result += res_string

    end_spaces = ' ' * (count_spaces - 2)
    return '{\n' + result + f'{end_spaces}' + '}'


def build_value(value, key, type_char, spaces):
    result = value
    end_char = '' if isinstance(value, dict) else '\n'

    if isinstance(value, bool):
        string_value = str(value)
        result = string_value[0].lower() + string_value[1:]
    if value is None:
        result = 'null'
    return f"{spaces}{type_char} {key}: {result}{end_char}"
