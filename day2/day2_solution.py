import math


def parse_input(input_file: str) -> list[dict[str:int]]:
    with open(input_file) as raw_measurements:
        measurements = [
            measurement.strip().split("x")
            for measurement in raw_measurements.readlines()
        ]
    measurement_maps = []
    for measurement in measurements:
        measurement_map = {}
        measurement_map["l"] = int(measurement[0])
        measurement_map["w"] = int(measurement[1])
        measurement_map["h"] = int(measurement[2])
        measurement_maps.append(measurement_map)
    return measurement_maps


def get_sides(measurement_map: dict[str:int], material: str) -> list[int]:
    if material == "ribbon":
        return [measurement_map["l"], measurement_map["w"], measurement_map["h"]]
    return [
        measurement_map["l"] * measurement_map["w"],
        measurement_map["w"] * measurement_map["h"],
        measurement_map["h"] * measurement_map["l"],
    ]


def calculate_material_footage(sides: list[int], material: str) -> int:
    double_sides = 2 * sum(sides)
    if material == "paper":
        return double_sides + min(sides)
    return math.prod(sides) + double_sides - 2 * max(sides)


def calculate_all_material_footage(input_file: str, material: str) -> int:
    if not isinstance(material, str):
        raise TypeError(f"Expected material to be a string, but got {type(material)}")

    if material not in ["paper", "ribbon"]:
        raise ValueError(f"Expected material to be paper or ribbon, but got {material}")

    measurement_maps = parse_input(input_file)
    overall_footage = 0

    for measurement_map in measurement_maps:
        sides = get_sides(measurement_map, material)
        overall_footage += calculate_material_footage(sides, material)

    return overall_footage


if __name__ == "__main__":
    print(
        calculate_all_material_footage("day2/day2_inputs/day2_final_input.txt", "paper")
    )
    print(
        calculate_all_material_footage(
            "day2/day2_inputs/day2_final_input.txt", "ribbon"
        )
    )
