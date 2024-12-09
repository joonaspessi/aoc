def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return input_data


def part_1(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/2023/dayXX.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    xxx
    """
    assert part_1(input_data) == 0


def test__part1():
    input_data = read_input("inputs/2023/day1.txt")
    assert part_1(input_data) == 0


def test__part2_sample():
    input_data = """
    xxx
    """
    assert part_2(input_data) == 0


def test__part2():
    input_data = read_input("inputs/2023/day1.txt")
    assert part_2(input_data) == 0
