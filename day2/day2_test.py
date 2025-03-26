import pytest
from unittest.mock import mock_open, patch
from day2_solution import parse_input, calculate_wrapping_paper_footage


def test_parse_input():
    input_data = "1x2x3\n4x5x6"
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual_parsed_data = parse_input("input_file.txt")
    expected_parsed_data = [
        {"l": 1, "w": 2, "h": 3},
        {"l": 4, "w": 5, "h": 6},
    ]
    assert actual_parsed_data == expected_parsed_data, (
        f"Expected {expected_parsed_data} for {input_data} but got {actual_parsed_data}"
    )


@pytest.mark.parametrize(
    "input_data, expected_footage",
    [
        ("2x3x4", 58),
        ("1x1x10", 43),
    ],
)
def test_part_1_solution(input_data: str, expected_footage: int):
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual_footage = calculate_wrapping_paper_footage("input_file.txt")
    assert actual_footage == expected_footage, (
        f"Expected {expected_footage} for {input_data} but got {actual_footage}"
    )
