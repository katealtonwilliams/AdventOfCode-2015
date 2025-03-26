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


def calculate_wrapping_paper_footage(input_file):
    measurement_maps = parse_input(input_file)
    overall_footage = 0
    for measurement_map in measurement_maps:
        side_1 = measurement_map["l"] * measurement_map["w"]
        side_2 = measurement_map["w"] * measurement_map["h"]
        side_3 = measurement_map["h"] * measurement_map["l"]
        overall_footage += 2 * (side_1 + side_2 + side_3) + min(side_1, side_2, side_3)
    return overall_footage


if __name__ == "__main__":
    print(calculate_wrapping_paper_footage("day2/day2_inputs/day2_final_input.txt"))
