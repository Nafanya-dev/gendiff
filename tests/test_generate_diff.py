from gendiff import generate_diff
import pytest


@pytest.fixture
def flat_files():
    first_path = 'tests/fixtures/file1.json'
    second_path = 'tests/fixtures/file2.json'
    return first_path, second_path

def test_generate_diff(flat_files):
    result = generate_diff(flat_files[0], flat_files[1])
    assert result == open('tests/fixtures/check_json.txt').read()