from collections import defaultdict
import itertools


INPUT_FILE = "inputs/2024/day8.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    rows = []
    for line in input_data.strip().split("\n"):
        row = list(line.strip())
        rows.append(row)

    nodes = defaultdict(list)

    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if rows[y][x] != ".":
                nodes[rows[y][x]].append((y, x))

    permutations = {}
    for node_type, locations in nodes.items():
        permutations[node_type] = list(itertools.combinations(locations, 2))

    return rows, permutations


def extrapolate_points(y1, x1, y2, x2):
    delta_y = y2 - y1
    delta_x = x2 - x1

    # Extend in the "positive" direction
    y_new1 = y2 + delta_y
    x_new1 = x2 + delta_x

    # Extend in the "negative" direction
    y_new2 = y1 - delta_y
    x_new2 = x1 - delta_x

    return (y_new1, x_new1), (y_new2, x_new2)


def extrapolate_points_2(grid, y1, x1, y2, x2):
    delta_y = y2 - y1
    delta_x = x2 - x1

    points = []
    while True:
        y_new1 = y2 + delta_y
        x_new1 = x2 + delta_x
        if not is_in_bounds(y_new1, x_new1, grid):
            break
        points.append((y_new1, x_new1))
        y2 = y_new1
        x2 = x_new1

    while True:
        y_new2 = y1 - delta_y
        x_new2 = x1 - delta_x
        if not is_in_bounds(y_new2, x_new2, grid):
            break
        points.append((y_new2, x_new2))
        y1 = y_new2
        x1 = x_new2

    return points


def is_in_bounds(y, x, rows):
    return 0 <= y < len(rows) and 0 <= x < len(rows[0])


def part_1(input_data: str) -> int:
    grid, permutations = parse(input_data)  # noqa
    result = set()
    for pairs in permutations.values():
        for (y1, x1), (y2, x2) in pairs:
            p1, p2 = extrapolate_points(y1, x1, y2, x2)
            if is_in_bounds(*p1, grid):
                result.add(p1)
            if is_in_bounds(*p2, grid):
                result.add(p2)

    return len(result)


def part_2(input_data: str) -> int:
    grid, permutations = parse(input_data)  # noqa
    result = set()
    for pairs in permutations.values():
        for (y1, x1), (y2, x2) in pairs:
            result.add((y1, x1))
            result.add((y2, x2))
            points = extrapolate_points_2(grid, y1, x1, y2, x2)
            for p in points:
                result.add(p)

    # print grid with results
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in result:
                print("X", end="")
            else:
                print(grid[y][x], end="")
        print()

    return len(result)


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """
    assert part_1(input_data) == 14


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 361


def test__part2_sample():
    input_data = """
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """
    assert part_2(input_data) == 34


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 1249
