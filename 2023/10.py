def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str):
    lines = [line.strip() for line in input_data.strip().split("\n")]
    grid = []
    start = None
    for i, line in enumerate(lines):
        if "S" in line:
            start = (i, line.index("S"))
        grid.append([c for c in line])
    assert start is not None
    return start, grid


def solve1(y, x, grid):
    start_y = y
    start_x = x

    steps = 0

    if x < len(grid[0]) - 1 and grid[y][x + 1] in {"-", "J", "7"}:
        dir = 1
    elif y < len(grid) - 1 and grid[y + 1][x] in {"|", "J", "L"}:
        dir = 2
    elif x > 0 and grid[y][x - 1] in {"-", "L", "F"}:
        dir = 3
    else:
        dir = 4

    while True:
        match dir:
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1
            case 4:
                y -= 1
        match grid[y][x]:
            case "L":
                dir = 1 if dir == 2 else 4
            case "J":
                dir = 4 if dir == 1 else 3
            case "F":
                dir = 1 if dir == 4 else 2
            case "7":
                dir = 3 if dir == 4 else 2
        steps += 1

        if x == start_x and y == start_y:
            return steps // 2 + (1 if steps % 2 else 0)


def solve2(y, x, grid):
    start_y = y
    start_x = x
    field_marked = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    start_pipe = None
    # L
    if (
        y > 0
        and grid[y - 1][x] in {"|", "F", "7"}
        and x < len(grid[0]) - 1
        and grid[y][x + 1] in {"-", "J", "7"}
    ):
        start_pipe = "L"
        dir = 1
    # J
    elif (
        y > 0
        and grid[y - 1][x] in {"|", "F", "7"}
        and x > 0
        and grid[y][x - 1] in {"-", "L", "F"}
    ):
        start_pipe = "J"
        dir = 3
    # F
    elif (
        y < len(grid) - 1
        and grid[y + 1][x] in {"|", "J", "L"}
        and x < len(grid[0]) - 1
        and grid[y][x + 1] in {"-", "7", "J"}
    ):
        start_pipe = "F"
        dir = 1
    # 7
    elif (
        y < len(grid) - 1
        and grid[y + 1][x] in {"|", "J", "L"}
        and x > 0
        and grid[y][x - 1] in {"-", "L", "F"}
    ):
        start_pipe = "7"
        dir = 4
    else:
        assert False

    grid[start_y][start_x] = start_pipe

    x = start_x
    y = start_y
    while True:
        match dir:
            case 1:
                x += 1
            case 2:
                y += 1
            case 3:
                x -= 1
            case 4:
                y -= 1
        match grid[y][x]:
            case "L":
                dir = 1 if dir == 2 else 4
            case "J":
                dir = 4 if dir == 1 else 3
            case "F":
                dir = 1 if dir == 4 else 2
            case "7":
                dir = 3 if dir == 4 else 2
        field_marked[y][x] = True
        if x == start_x and y == start_y:
            break

    total = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if not field_marked[y][x]:
                n = 0
                prev = None
                for y1 in range(y + 1, len(grid)):
                    if field_marked[y1][x]:
                        if grid[y1][x] == "-":
                            n += 1
                        elif grid[y1][x] == "7" or grid[y1][x] == "F":
                            prev = grid[y1][x]
                        elif (grid[y1][x] == "J" and prev == "F") or (
                            grid[y1][x] == "L" and prev == "7"
                        ):
                            n += 1
                if n % 2 == 1:
                    total += 1
    return total


def part_1(input_data: str) -> int:
    (y, x), grid = parse(input_data)
    return solve1(y, x, grid)


def part_2(input_data: str) -> int:
    (y, x), grid = parse(input_data)
    return solve2(y, x, grid)


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day10.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample_1():
    input_data = """
    .....
    .S-7.
    .|.|.
    .L-J.
    .....
    """
    assert part_1(input_data) == 4


def test__part1_sample_2():
    input_data = """
    -L|F7
    7S-7|
    L|7||
    -L-J|
    L|-JF
    """
    assert part_1(input_data) == 4


def test__part1_sample_3():
    input_data = """
    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...
    """
    assert part_1(input_data) == 8


def test__part1():
    input_data = read_input("inputs/2023/day10.txt")
    assert part_1(input_data) == 6968


def test__part2_sample_1():
    input_data = """
    ..........
    .S------7.
    .|F----7|.
    .||OOOO||.
    .||OOOO||.
    .|L-7F-J|.
    .|II||II|.
    .L--JL--J.
    ..........
    """
    assert part_2(input_data) == 4


def test__part2_sample_2():
    input_data = """
    .F----7F7F7F7F-7....
    .|F--7||||||||FJ....
    .||.FJ||||||||L7....
    FJL7L7LJLJ||LJ.L-7..
    L--J.L7...LJS7F-7L7.
    ....F-J..F7FJ|L7L7L7
    ....L7.F7||L7|.L7L7|
    .....|FJLJ|FJ|F7|.LJ
    ....FJL-7.||.||||...
    ....L---J.LJ.LJLJ...
    """
    assert part_2(input_data) == 8


def test__part2():
    input_data = read_input("inputs/2023/day10.txt")
    assert part_2(input_data) == 413
