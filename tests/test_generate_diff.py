from gendiff import generate_diff
import pytest


@pytest.fixture
def flat_files():
    paths = {
        'first_path_json': 'tests/fixtures/file1.json',
        'second_path_json': 'tests/fixtures/file2.json',
        'first_path_yml': 'tests/fixtures/file1.yml',
        'second_path_yml': 'tests/fixtures/file2.yml',
        'check_flat_json': open('tests/fixtures/check_json.txt').read(),
        'check_flat_yml': open('tests/fixtures/check_yml.txt').read()
    }
    return paths


@pytest.fixture
def deep_files():
    paths = {
        'first_path_yaml': 'tests/fixtures/file1.yaml',
        'second_path_yaml': 'tests/fixtures/file2.yaml',
        'check_deep_yaml_stylish': open('tests/fixtures/check_yaml_stylish.txt').read(),
        'check_deep_yaml_plain': open('tests/fixtures/check_yaml_plain.txt').read(),
        'check_json_format': open('tests/fixtures/check_json_format.txt').read()
    }
    return paths


def test_generate_diff(flat_files, deep_files):
    result_flat_stylish_json = generate_diff(flat_files['first_path_json'], flat_files['second_path_json'])
    result_flat_stylish_yml = generate_diff(flat_files['first_path_yml'], flat_files['second_path_yml'])
    assert result_flat_stylish_json == flat_files['check_flat_json']
    assert result_flat_stylish_yml == flat_files['check_flat_yml']

    result_deep_yaml_stylish = generate_diff(deep_files['first_path_yaml'], deep_files['second_path_yaml'])
    assert result_deep_yaml_stylish == deep_files['check_deep_yaml_stylish']

    result_deep_yaml_plain = generate_diff(deep_files['first_path_yaml'], deep_files['second_path_yaml'], 'plain')
    assert result_deep_yaml_plain == deep_files['check_deep_yaml_plain']

    result_json_format = generate_diff(deep_files['first_path_yaml'], deep_files['second_path_yaml'], 'json')
    assert result_json_format == deep_files['check_json_format']
