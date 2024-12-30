import re
from sympy import solve
from sympy.abc import a, b

INPUT_FILE = "inputs/2024/day13.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    data = []
    for chunk in input_data.strip().split("\n\n"):
        # parse all numbers with regex
        numbers = re.findall(r"\d+", chunk)
        numbers = list(map(int, numbers))
        data.append(numbers)
    return data


def solve_eq(ax, ay, bx, by, px, py):
    equations = [a * ax + b * bx - px, a * ay + b * by - py]
    solutions = solve(equations, a, b, dict=True)
    for solution in solutions:
        if solution[a].is_integer and solution[b].is_integer:
            return int(solution[a]) * 3 + int(solution[b])
    return 0


def part_1(input_data: str) -> int:
    data = parse(input_data)
    result = 0
    for d in data:
        ax, ay, bx, by, px, py = d
        result += solve_eq(ax, ay, bx, by, px, py)
    return result


def part_2(input_data: str) -> int:
    data = parse(input_data)
    result = 0
    for d in data:
        ax, ay, bx, by, px, py = d
        px += 10000000000000
        py += 10000000000000
        result += solve_eq(ax, ay, bx, by, px, py)
    return result


def test__part1_sample():
    input_data = """
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279
    """
    assert part_1(input_data) == 480


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 35574


def test__part2_sample():
    input_data = """
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279
    """
    assert part_2(input_data) == 875318608908


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 80882098756071


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
