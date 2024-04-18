from . get_data import get_data
from . get_diff import get_diff
from .format.stylish import get_stylish_line


def generate_diff(first_file, second_file, format = 'stylish'):
    res_file1 = get_data(first_file)
    res_file2 = get_data(second_file)
    diff = get_diff(res_file1, res_file2)
    result = get_stylish_line(diff)
    return result
