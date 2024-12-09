def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    parsed = []
    for line in input_data.strip().split("\n"):
        parsed.append([int(ll.strip()) for ll in line.split()])
    return parsed


def is_valid(line):
    increasing = all(
        line[i] < line[i + 1] and (1 <= line[i + 1] - line[i] <= 3)
        for i in range(len(line) - 1)
    )
    decreasing = all(
        line[i] > line[i + 1] and (1 <= line[i] - line[i + 1] <= 3)
        for i in range(len(line) - 1)
    )
    if increasing or decreasing:
        return True


def part_1(input_data: str) -> int:
    data = parse(input_data)
    result = 0
    for line in data:
        if is_valid(line):
            result += 1
    return result


def part_2(input_data: str) -> int:
    data = parse(input_data)
    result = 0
    for line in data:
        for i in range(len(line)):
            new_line = line[:i] + line[i + 1 :]  # noqa
            if is_valid(new_line):
                result += 1
                break
    return result


if __name__ == "__main__":
    input_data = read_input("inputs/2024/day2.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
    assert part_1(input_data) == 2


def test__part1():
    input_data = read_input("inputs/2024/day2.txt")
    assert part_1(input_data) == 202


def test__part2_sample():
    input_data = """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
    assert part_2(input_data) == 4


def test__part2():
    input_data = read_input("inputs/2024/day2.txt")
    assert part_2(input_data) == 271
