from typing import Tuple


def read_file(filename: str) -> str:
    with open(filename) as f:
        data = f.read()
    return data


def parse_input(input_data: str) -> list[list[str]]:
    input_data = input_data.strip()
    lines = [line.strip() for line in input_data.split("\n")]
    return [list(line) for line in lines]


def create_symbol_lookup(grid: list[list[str]]) -> dict[Tuple[int, int], bool]:
    symbol_lookup = {}
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_lookup[(y, x)] = True
    return symbol_lookup


def create_gear_candidate_lookup(grid: list[list[str]]) -> list[Tuple[int, int]]:
    gear_candidates = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "*":
                gear_candidates.append((y, x))
    return gear_candidates


def create_numbers_and_positions(
    grid: list[list[str]]
) -> list[Tuple[str, list[Tuple[int, int]]]]:
    numbers_and_positions = []
    for y, line in enumerate(grid):
        ongoing_number = ""
        ongoing_number_positions = []
        for x, char in enumerate(line):
            if char.isdigit():
                ongoing_number += char
                ongoing_number_positions.append((y, x))
            elif ongoing_number:
                numbers_and_positions.append((ongoing_number, ongoing_number_positions))
                ongoing_number = ""
                ongoing_number_positions = []
        if ongoing_number:
            numbers_and_positions.append((ongoing_number, ongoing_number_positions))

    return numbers_and_positions


def filter_numbers_with_adjacent_symbols(
    numbers_and_positions: list, symbol_lookup: dict
) -> list[int]:
    numbers_with_adjacent_symbols = []
    for number, positions in numbers_and_positions:
        adjacent_symbols = False
        for y, x in positions:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    if (y + dy, x + dx) in symbol_lookup:
                        adjacent_symbols = True
                        break
                if adjacent_symbols:
                    break
        if adjacent_symbols:
            numbers_with_adjacent_symbols.append(int(number))
    return numbers_with_adjacent_symbols


def is_adjacent(
    positions: list[Tuple[int, int]], gear_candidate: Tuple[int, int]
) -> bool:
    for position in positions:
        y, x = position
        gy, gx = gear_candidate
        if abs(y - gy) <= 1 and abs(x - gx) <= 1:
            return True
    return False


def gear_ratios(
    numbers_and_positions: list[Tuple[str, list[Tuple[int, int]]]],
    gear_candidate_lookup: list[Tuple[int, int]],
) -> list[int]:
    gear_ratios = []
    for gear_candidate in gear_candidate_lookup:
        count = 0
        numbers = []
        for number, positions in numbers_and_positions:
            if is_adjacent(positions, gear_candidate):
                count += 1
                numbers.append(int(number))
        if count == 2:
            gear_ratios.append(numbers[0] * numbers[1])

    return gear_ratios


def part_1(input_data: str) -> int:
    grid = parse_input(input_data)
    symbol_lookup = create_symbol_lookup(grid)
    numbers_and_positions = create_numbers_and_positions(grid)
    numbers_with_adjacent_symbols = filter_numbers_with_adjacent_symbols(
        numbers_and_positions, symbol_lookup
    )
    return sum(numbers_with_adjacent_symbols)


def part_2(input_data: str) -> int:
    grid = parse_input(input_data)
    gear_candidate_lookup = create_gear_candidate_lookup(grid)
    numbers_and_positions = create_numbers_and_positions(grid)
    gears = gear_ratios(numbers_and_positions, gear_candidate_lookup)
    return sum(gears)


def main():
    input_data = read_file("inputs/day3.txt")
    print(f"part 1: {part_1(input_data)}")
    print(f"part 2: {part_2(input_data)}")


if __name__ == "__main__":
    main()


def test__part1_sample():
    input_data = """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """
    assert part_1(input_data) == 4361


def test__part1():
    input_data = read_file("inputs/day3.txt")
    assert part_1(input_data) == 529618


def test__part2_test():
    input_data = """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """
    assert part_2(input_data) == 467835


def test__part2():
    input_data = read_file("inputs/day3.txt")
    assert part_2(input_data) == 77509019
