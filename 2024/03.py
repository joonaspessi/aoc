import re

INPUT_FILE = "inputs/2024/day3.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def part_1(input_data: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_data)
    return sum([int(x) * int(y) for x, y in matches])


def part_2(input_data: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)"
    matches = re.findall(pattern, input_data)

    enabled = True
    result = 0
    for x, y, do, dont in matches:
        if do:
            enabled = True
        elif dont:
            enabled = False
        else:
            if enabled:
                result += int(x) * int(y)

    return result


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    """
    assert part_1(input_data) == 161


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 167650499


def test__part2_sample():
    input_data = """
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
    """
    assert part_2(input_data) == 48


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 95846796
