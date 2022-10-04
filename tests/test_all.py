"""JSON files diff test."""
from gendiff.generate_diff import generate_diff
import tests.expected as expected


def test_diff_json():
    actual = generate_diff('./tests/fixtures/file1.json',
                           './tests/fixtures/file2.json')
    assert actual == expected.DIFF_JSON

def test_diff_yaml():
    actual = generate_diff('./tests/fixtures/file1.yaml',
			   './tests/fixtures/file2.yaml')
    assert actual == expected.DIFF_YAML

def test_diff_yml():
    actual = generate_diff('./tests/fixtures/file1.yml',
			   './tests/fixtures/file2.yml')
    assert actual == expected.DIFF_YML
