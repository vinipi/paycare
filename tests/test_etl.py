from etl import extract_data, transform_data, load_data
import pandas as pd
import logging

def test_extract_data_valid(tmp_path):
    csv_content = """\
        id,name,age,city,salary
        1,John Doe,28,New York,70000
        2,Jane Smith,34,Los Angeles,80000
        """
    # mock a csv file
    csv_file = tmp_path/"test.csv"
    csv_file.write_text(csv_content)

    # Test with a valid CSV file
    data = extract_data(str(csv_file))
    assert data is not None
    assert not data.empty

def test_extract_data_invalid(tmp_path):
    csv_content = """\
        invalid
        """
    # mock a csv file
    csv_file = tmp_path/"test.csv"
    csv_file.write_text(csv_content)

    # Test with a invalid CSV file
    data = extract_data(str(csv_file))
    assert data.empty

def test_transform_data():
    data = pd.DataFrame([
    [1, "John Doe", 28, "New York", 70000],
    [2, "Jane Smith", 34, "Los Angeles", 80000],
    ], columns=["id", "name", "age", "city", "salary"])

    data_cleaned = transform_data(data)
    assert data_cleaned is not None
    assert not data_cleaned.empty
    assert list(data_cleaned.columns) == [
        "id",
        "name",
        "age",
        "city",
        "salary",
        "tax",
        "net_salary",
    ]

def test_load_data(tmp_path):
    csv_content = """id,name,age,city,salary
1,John Doe,28,New York,70000
2,Jane Smith,34,Los Angeles,80000
"""

    data = pd.DataFrame([
    [1, "John Doe", 28, "New York", 70000],
    [2, "Jane Smith", 34, "Los Angeles", 80000],
    ], columns=["id", "name", "age", "city", "salary"])

    output_file = tmp_path/"output_file.csv"
    load_data(data, output_file)
    assert output_file.read_text(encoding="utf-8") == csv_content
    