def floor_finder(input_file: str) -> int:
    with open(input_file) as raw_input:
        input_instructions = raw_input.read().strip()
    up = input_instructions.count("(")
    down = input_instructions.count(")")
    return up - down


def basement_character_finder(input_file: str) -> int:
    with open(input_file) as raw_input:
        input_instructions = raw_input.read().strip()
    current_floor = 0
    for position, bracket in enumerate(input_instructions):
        if bracket == "(":
            current_floor += 1
        else:
            current_floor -= 1
        if current_floor == -1:
            return position + 1


if __name__ == "__main__":
    print(floor_finder("day1/day1_inputs/day1_final_input.txt"))
    print(basement_character_finder("day1/day1_inputs/day1_final_input.txt"))
