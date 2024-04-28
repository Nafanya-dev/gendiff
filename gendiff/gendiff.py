from . get_data import get_data
from . get_diff import get_diff
from .format.stylish import get_stylish_line
from .format.plain import get_plain_line
from .format.json_format import get_json_line

FORMATER = {
    'stylish': get_stylish_line,
    'plain': get_plain_line,
    'json': get_json_line,
}


def generate_diff(first_file, second_file, format_name='stylish'):
    res_file1 = get_data(first_file)
    res_file2 = get_data(second_file)
    diff = get_diff(res_file1, res_file2)
    result = FORMATER[format_name](diff)
    return result
