import pytest
from unittest.mock import mock_open, patch
from day2_solution import (
    parse_input,
    calculate_wrapping_paper_footage,
    calculate_ribbon_footage,
    calculate_footage,
)
from typing import Callable, Generator, Any


@pytest.fixture
def mock_file() -> Generator[Callable]:
    with patch("builtins.open", mock_open()) as mock_raw_data:

        def _set_mock_data(input_data: str = "data"):
            mock_raw_data.return_value.readlines.return_value = input_data

        yield _set_mock_data


def test_parse_input(mock_file: Callable):
    # Arrange
    input_data = ["1x2x3", "4x5x6"]
    mock_file(input_data)
    expected_parsed_data = [
        {"l": 1, "w": 2, "h": 3},
        {"l": 4, "w": 5, "h": 6},
    ]

    # Act
    actual_parsed_data = parse_input("input_file.txt")

    # Assert
    assert actual_parsed_data == expected_parsed_data, (
        f"Expected {expected_parsed_data} for {input_data} but got {actual_parsed_data}"
    )


@pytest.mark.parametrize(
    "input_data, expected_footage",
    [
        (["2x3x4"], 58),
        (["1x1x10"], 43),
    ],
)
def test_part_1_solution(input_data: str, expected_footage: int, mock_file: Callable):
    # Arrange
    mock_file(input_data)

    # Act
    actual_footage = calculate_wrapping_paper_footage("input_file.txt")

    # Assert
    assert actual_footage == expected_footage, (
        f"Expected {expected_footage} for {input_data} but got {actual_footage}"
    )


@pytest.mark.parametrize(
    "input_data, expected_footage",
    [
        (["2x3x4"], 34),
        (["1x1x10"], 14),
    ],
)
def test_part_2_solution(input_data: str, expected_footage: int, mock_file: Callable):
    # Arrange
    mock_file(input_data)

    # Act
    actual_footage = calculate_ribbon_footage("input_file.txt")

    # Assert
    assert actual_footage == expected_footage, (
        f"Expected {expected_footage} for {input_data} but got {actual_footage}"
    )


@pytest.mark.parametrize("material", [5, None, 3.2, ["paper"], {"type": "ribbon"}])
def test_incorrect_material_type_raises_error(material: Any, mock_file: Callable):
    # TODO - add type error exception
    # Arrange
    mock_file()

    # Act
    with pytest.raises(TypeError) as err:
        calculate_footage("input_file.txt", material)

    # Assert
    assert f"Expected material to be a string, but got {type(material)}" == str(
        err.value
    ), "Expected error not raised"


def test_incorrect_material_raises_error(mock_file: Callable):
    # Arrange
    mock_file()

    # Act
    with pytest.raises(ValueError) as err:
        calculate_footage("input_file.txt", "something else")

    # Assert
    assert f"Expected material to be paper or ribbon, but got something else" == str(
        err.value
    ), "Expected error not raised"


# @pytest.mark.parametrize(
#     "input_data, expected_footage",
#     [
#         ("2x3x4", 58),
#         ("1x1x10", 43),
#     ],
# )
# def test_part_1_solution_refactored(input_data: str, expected_footage: int):
#     with patch("builtins.open", mock_open(read_data=input_data)):
#         actual_footage = calculate_footage("input_file.txt", "paper")
#     assert actual_footage == expected_footage, (
#         f"Expected {expected_footage} for {input_data} but got {actual_footage}"
#     )
