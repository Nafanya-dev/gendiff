def get_stylish_line(data):
    chars = {'removed': '-',
             'add': '+',
             'unchanged': ' '}

    result = '{\n'
    for key, d in data.items():
        desc = d['desc']
        value = ((d['old_value'], d['new_value']) if
                 desc == 'changed' else
                 d['value'])
        res_string = ''
        if desc == 'nested':
            res_string = get_stylish_line(value)
            desc = 'unchanged'
        elif desc == 'changed':
            res_string = (f"  {chars['removed']} {key}: {value[0]}\n"
            f"  {chars['add']} {key}: {value[1]}\n")
        else:
            res_string = f"  {chars[desc]} {key}: {value}\n"
        result += res_string
    return result + '}\n'
