CHARS = {'removed': '-', 'add': '+', 'unchanged': ' '}


def get_stylish_line(data, count_spaces=2):
    result = ''
    spaces = ' ' * count_spaces
    for key, d in data.items():
        status = (d.get('status', 'unchanged') if
                  isinstance(d, dict) else
                  'unchanged')
        value = ((d['old_value'], d['new_value']) if
                 status == 'changed' else
                 d.get('value', d) if isinstance(d, dict) else d)
        res_string = ''

        if status == 'nested':
            res_string = (f"{spaces}  {key}: "
                          f"{get_stylish_line(value, count_spaces + 4)}")
        elif status == 'changed':
            first_value = (get_stylish_line(value[0], count_spaces + 4) if
                           isinstance(value[0], dict) else
                           value[0])
            second_value = (get_stylish_line(value[1], count_spaces + 4) if
                            isinstance(value[1], dict) else
                            value[1])

            first_end_trans = '\n' if first_value == value[0] else ''
            second_end_trans = '\n' if second_value == value[1] else ''

            res_string = (f"{spaces}{CHARS['removed']} {key}: "
                          f"{first_value}{first_end_trans}"
                          f"{spaces}{CHARS['add']} {key}: "
                          f"{second_value}{second_end_trans}")
        else:
            open_value = (get_stylish_line(value, count_spaces + 4) if
                          isinstance(value, dict) else
                          value)

            end_char = ('\n' if open_value == value else '')
            res_string = (f"{spaces}{CHARS[status]} "
                          f"{key}: {open_value}{end_char}")
        result += res_string
    end_spaces = ' ' * (count_spaces - 2)
    end_transfer = '' if count_spaces == 2 else '\n'
    return '{\n' + result + f'{end_spaces}' + '}' + f'{end_transfer}'
