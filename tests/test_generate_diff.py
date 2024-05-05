from gendiff import generate_diff
import pytest


PATH_FILE1_YAML = 'tests/fixtures/file1.yaml'
PATH_FILE2_YAML = 'tests/fixtures/file2.yaml'

PATH_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_FILE2_JSON = 'tests/fixtures/file2.json'

STYLISH_PATH_YAML = 'tests/fixtures/check_yaml_stylish.txt'
PLAIN_PATH_YAML = 'tests/fixtures/check_yaml_plain.txt'
JSON_PATH_FILES_YAML = 'tests/fixtures/check_json_format.txt'

STYLISH_PATH_JSON = 'tests/fixtures/check_json_files_stylish.txt'
PLAIN_PATH_JSON = 'tests/fixtures/check_json_files_plain.txt'
JSON_PATH_FILES_JSON = 'tests/fixtures/check_json_files_format_json.txt'


@pytest.mark.parametrize(
    'path_file1, path_file2, check_file_path, format',
    [
        (PATH_FILE1_YAML, PATH_FILE2_YAML, STYLISH_PATH_YAML, 'stylish'),
        (PATH_FILE1_YAML, PATH_FILE2_YAML, PLAIN_PATH_YAML, 'plain'),
        (PATH_FILE1_YAML, PATH_FILE2_YAML, JSON_PATH_FILES_YAML, 'json'),
        (PATH_FILE1_JSON, PATH_FILE2_JSON, STYLISH_PATH_JSON, 'stylish'),
        (PATH_FILE1_JSON, PATH_FILE2_JSON, PLAIN_PATH_JSON, 'plain'),
        (PATH_FILE1_JSON, PATH_FILE2_JSON, JSON_PATH_FILES_JSON, 'json'),
    ]
)
def test_generate_diff(path_file1, path_file2, check_file_path, format):
    result = generate_diff(path_file1, path_file2, format)

    with open(check_file_path) as check_file:
        assert result == check_file.read()
