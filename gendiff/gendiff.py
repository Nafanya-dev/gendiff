from . get_data import get_data
from . get_diff import get_diff
from .format.stylish import get_stylish_line
from .format.plain import get_plain_line


def generate_diff(first_file, second_file, format_name='stylish'):
    formater = {
        'stylish': get_stylish_line,
        'plain': get_plain_line,
    }
    res_file1 = get_data(first_file)
    res_file2 = get_data(second_file)
    diff = get_diff(res_file1, res_file2)
    result = formater[format_name](diff)
    return result
