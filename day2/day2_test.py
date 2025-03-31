import pytest
from day2.day2_solution import (
    parse_input,
    calculate_all_material_footage,
    get_sides,
    calculate_material_footage,
)
from typing import Callable, Any
from test_fixtures import mock_file_with_multiple_lines


def test_parse_input(mock_file_with_multiple_lines: Callable):
    # Arrange
    input_data = ["1x2x3", "4x5x6"]
    mock_file_with_multiple_lines(input_data)
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


@pytest.mark.parametrize("material", [5, None, 3.2, ["paper"], {"type": "ribbon"}])
def test_incorrect_material_type_raises_error(
    material: Any, mock_file_with_multiple_lines: Callable
):

    # Arrange
    mock_file_with_multiple_lines()

    # Act
    with pytest.raises(TypeError) as err:
        calculate_all_material_footage("input_file.txt", material)

    # Assert
    assert (
        str(err.value) == f"Expected material to be a string, but got {type(material)}"
    ), "Expected error not raised"


def test_incorrect_material_raises_error(mock_file_with_multiple_lines: Callable):
    # Arrange
    mock_file_with_multiple_lines()

    # Act
    with pytest.raises(ValueError) as err:
        calculate_all_material_footage("input_file.txt", "something else")

    # Assert
    assert (
        str(err.value)
        == f"Expected material to be paper or ribbon, but got something else"
    ), "Expected error not raised"


@pytest.mark.parametrize(
    "material, expected_sides", [("paper", [6, 12, 8]), ("ribbon", [2, 3, 4])]
)
def test_get_sides(material: str, expected_sides: list[int]):
    # Arrange
    measurement_map = {"l": 2, "w": 3, "h": 4}

    # Act
    actual_sides = get_sides(measurement_map, material)

    # Assert
    assert actual_sides == expected_sides


@pytest.mark.parametrize("material, expected_footage", [("paper", 20), ("ribbon", 34)])
def test_calulate_material_footage(material: str, expected_footage: list[int]):
    # Arrange
    sides = [2, 3, 4]

    # Act
    actual_footage = calculate_material_footage(sides, material)

    # Assert
    assert actual_footage == expected_footage, (
        f"Expected {material} footage to be {expected_footage} but got {actual_footage}"
    )


@pytest.mark.parametrize(
    "input_data, material, expected_footage",
    [
        (["2x3x4"], "paper", 58),
        (["1x1x10"], "paper", 43),
        (["2x3x4"], "ribbon", 34),
        (["1x1x10"], "ribbon", 14),
    ],
)
def test_part_calculate_all_material_footage(
    input_data: list[str],
    material: str,
    expected_footage: int,
    mock_file_with_multiple_lines: Callable,
):
    # Arrange
    mock_file_with_multiple_lines(input_data)

    # Act
    actual_footage = calculate_all_material_footage("input_file.txt", material)

    # Assert
    assert actual_footage == expected_footage, (
        f"Expected {expected_footage} for {input_data} {material} but got {actual_footage}"
    )
