import pytest
from unittest.mock import mock_open, patch
from day1_solution import floor_finder, basement_character_finder


@pytest.mark.parametrize(
    "input_data, expected_floor",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_part_1_solution(input_data: str, expected_floor: int):
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual_floor = floor_finder("input_file.txt")
    assert actual_floor == expected_floor, (
        f"Expected {expected_floor} for {input_data} but got {actual_floor}"
    )


@pytest.mark.parametrize(
    "input_data, expected_position",
    [(")", 1), ("()())", 5)],
)
def test_part_2_solution(input_data: str, expected_position: int):
    with patch("builtins.open", mock_open(read_data=input_data)):
        actual_position = basement_character_finder("input_file.txt")
    assert actual_position == expected_position, (
        f"Expected {expected_position} for {input_data} but got {actual_position}"
    )
