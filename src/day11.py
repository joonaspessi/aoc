import itertools


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    data = []
    expand_rows = []
    lines = [line.strip() for line in input_data.strip().split("\n")]
    for y, line in enumerate(lines):
        if all(c == "." for c in line):
            expand_rows.append(y)
        data.append([c for c in line])

    expand_columns = []
    for x in range(len(data[0])):
        flag = True
        for y in range(len(data)):
            if data[y][x] != ".":
                flag = False

        if flag:
            expand_columns.append(x)

    lookup = set()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "#":
                lookup.add((y, x))
    return lookup, expand_columns, expand_rows


def distance(yx1, yx2, expand_columns, expand_rows, expansion=1):
    dis = abs(yx1[0] - yx2[0]) + abs(yx1[1] - yx2[1])
    for y in expand_rows:
        if yx1[0] < y < yx2[0] or yx2[0] < y < yx1[0]:
            dis += expansion
    for x in expand_columns:
        if yx1[1] < x < yx2[1] or yx2[1] < x < yx1[1]:
            dis += expansion
    return dis


def solve(input_data, expansion=1):
    lookup, expand_columns, expand_rows = parse(input_data)
    combinations = itertools.combinations(lookup, 2)
    distances = []
    for yx1, yx2 in combinations:
        distances.append(distance(yx1, yx2, expand_columns, expand_rows, expansion))
    return sum(distances)


def part_1(input_data: str) -> int:
    return solve(input_data, expansion=1)


def part_2(input_data: str) -> int:
    return solve(input_data, expansion=1000000 - 1)


if __name__ == "__main__":
    input_data = read_input("inputs/day11.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....
    """
    assert part_1(input_data) == 374


def test__part1():
    input_data = read_input("inputs/day11.txt")
    assert part_1(input_data) == 10289334


def test__part2_sample_1():
    input_data = """
    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....
    """
    assert solve(input_data, 10 - 1) == 1030


def test__part2_sample_2():
    input_data = """
    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....
    """
    assert solve(input_data, 100 - 1) == 8410


def test__part2():
    input_data = read_input("inputs/day11.txt")
    assert part_2(input_data) == 649862989626
