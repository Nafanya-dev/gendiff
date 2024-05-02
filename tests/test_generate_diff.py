from gendiff import generate_diff
import pytest


PATH_FILE1_YAML = 'tests/fixtures/file1.yaml'
PATH_FILE2_YAML = 'tests/fixtures/file2.yaml'

STYLISH_PATH = 'tests/fixtures/check_yaml_stylish.txt'
PLAIN_PATH = 'tests/fixtures/check_yaml_plain.txt'
JSON_PATH = 'tests/fixtures/check_json_format.txt'


@pytest.mark.parametrize(
    'path_file1, path_file2, check_file_path, format',
    [
        (PATH_FILE1_YAML, PATH_FILE2_YAML, STYLISH_PATH, 'stylish'),
        (PATH_FILE1_YAML, PATH_FILE2_YAML, PLAIN_PATH, 'plain'),
        (PATH_FILE1_YAML, PATH_FILE2_YAML, JSON_PATH, 'json'),
    ]
)
def test_generate_diff(path_file1, path_file2, check_file_path, format):
    result = generate_diff(path_file1, path_file2, format)

    with open(check_file_path) as check_file:
        assert result == check_file.read()
