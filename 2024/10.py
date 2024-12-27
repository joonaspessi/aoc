INPUT_FILE = "inputs/2024/dayX.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    rows = []
    for line in input_data.strip().split("\n"):
        row = list(line.strip())
        rows.append(row)

    return rows


def part_1(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
    assert part_1(input_data) == 0


# def test__part1():
#     input_data = read_input(INPUT_FILE)
#     assert part_1(input_data) == 0


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0
