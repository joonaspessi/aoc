from collections import deque


INPUT_FILE = "inputs/2024/day7.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    parsed = []
    for line in input_data.strip().split("\n"):
        data = line.strip().split(":")
        result = int(data[0].strip())
        operands = [int(x) for x in data[1].strip().split()]
        parsed.append({"target": result, "operands": operands})

    return parsed


def backtrack(curr_index, operands, result, target):
    if curr_index == len(operands):
        return result == target

    if backtrack(curr_index + 1, operands, result + operands[curr_index], target):
        return True
    if backtrack(curr_index + 1, operands, result * operands[curr_index], target):
        return True
    return False


def part_1(input_data: str) -> int:
    data = parse(input_data)  # noqa
    result = 0
    for d in data:
        if backtrack(0, d["operands"], 0, d["target"]):
            result += d["target"]

    return result


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    """
    assert part_1(input_data) == 3749


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 0


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0
