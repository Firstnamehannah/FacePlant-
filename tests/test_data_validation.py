from linkml.validator import validate_file

SCHEMA_PATH = "src/faceplant/schema/faceplant.yaml"

def test_valid_example_passes():
    report = validate_file("tests/data/valid_example.yaml", SCHEMA_PATH)
    assert not report.results

def test_invalid_example_fails():
    report = validate_file("tests/data/invalid_example.yaml", SCHEMA_PATH)
    assert report.results  # expect violations