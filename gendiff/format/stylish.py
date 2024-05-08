CHARS = {'removed': '-', 'add': '+', 'unchanged': ' '}


def get_stylish_line(data, deep=1):
    result = ''
    for key, d in data.items():
        type_ = (d.get('type', 'unchanged') if
                 isinstance(d, dict) else
                 'unchanged')
        values = ((d['old_value'], d['new_value']) if
                  type_ == 'changed' else
                  d.get('value', d) if isinstance(d, dict) else d)
        res_string = ''

        if type_ == 'nested':
            value = get_stylish_line(values, deep + 1)
            res_string = build_peak(value, key, ' ', deep)
        elif type_ == 'changed':
            first_value = build_value((get_stylish_line(values[0],
                                       deep + 1) if
                                       isinstance(values[0], dict) else
                                       values[0]))
            second_value = build_value((get_stylish_line(values[1],
                                        deep + 1) if
                                        isinstance(values[1], dict) else
                                        values[1]))

            res_string = build_peak(first_value, key, CHARS['removed'],
                                    deep) + build_peak(second_value,
                                                       key, CHARS['add'],
                                                       deep)
        else:
            value = build_value((get_stylish_line(values, deep + 1) if
                                isinstance(values, dict) else
                                values))

            res_string = build_peak(value, key, CHARS[type_], deep)
        result += res_string

    end_spaces = ' ' * (4 * (deep - 1))
    return '{\n' + result + f'{end_spaces}' + '}'


def build_peak(value, key, type_char, deep):
    couint_spaces = 4 * (deep - 1) + 2
    spaces = ' ' * couint_spaces
    end_char = '' if isinstance(value, dict) else '\n'
    return f"{spaces}{type_char} {key}: {value}{end_char}"


def build_value(value):
    result = value
    if isinstance(value, bool):
        string_value = str(value)
        result = string_value[0].lower() + string_value[1:]
    if value is None:
        result = 'null'
    return result
