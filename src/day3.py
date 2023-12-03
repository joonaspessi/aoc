def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data


def parse_input(input_data):
    input_data = input_data.strip()
    lines = [line.strip() for line in input_data.split("\n")]
    return [list(line) for line in lines]


def create_symbol_lookup(grid, symbol_lookup=None):
    symbol_lookup = {}
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_lookup[(y, x)] = True
    return symbol_lookup


def create_numbers_and_positions(grid):
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
):
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


def part_1(input_data):
    grid = parse_input(input_data)
    symbol_lookup = create_symbol_lookup(grid)
    numbers_and_positions = create_numbers_and_positions(grid)
    numbers_with_adjacent_symbols = filter_numbers_with_adjacent_symbols(
        numbers_and_positions, symbol_lookup
    )
    return sum(numbers_with_adjacent_symbols)


def part_2(input_data):
    pass


def main():
    input_data = read_file("inputs/day3.txt")
    print(f"part 1: {part_1(input_data)}")
    # print(f"part 2: {part_2("inputs/day3.txt")}")


if __name__ == "__main__":
    main()


def test__part1():
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
