def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return [[c for c in row.strip()] for row in input_data.strip().split("\n")]


def move(grid):
    c_len = len(grid[0])
    r_len = len(grid)
    for c in range(c_len):
        for _ in range(r_len):
            for r in range(r_len):
                if grid[r][c] == "O" and r > 0 and grid[r - 1][c] == ".":
                    grid[r][c] = "."
                    grid[r - 1][c] = "O"
    return grid


def rotate(grid):
    c_len = len(grid[0])
    r_len = len(grid)
    new_grid = [["X" for _ in range(r_len)] for _ in range(c_len)]
    for r in range(r_len):
        for c in range(c_len):
            new_grid[c][r_len - 1 - r] = grid[r][c]
    return new_grid


def clc_ld(grid):
    load = 0
    len_r = len(grid)
    len_c = len(grid[0])
    for r in range(len_r):
        for c in range(len_c):
            if grid[r][c] == "O":
                load += len_r - r
    return load


def part_1(input_data: str) -> int:
    grid = parse(input_data)
    grid = move(grid)
    return clc_ld(grid)


def part_2(input_data: str) -> int:
    grid = parse(input_data)
    target = 10**9
    grid_states = {}
    i = 0
    while i < target:
        i += 1
        for j in range(4):
            grid = move(grid)
            grid = rotate(grid)

        grid_hash = tuple(tuple(r) for r in grid)
        if grid_hash in grid_states:
            cycle_len = i - grid_states[grid_hash]
            m = (target - i) // cycle_len
            i += m * cycle_len
        grid_states[grid_hash] = i

    return clc_ld(grid)


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day14.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....
    """
    assert part_1(input_data) == 136


def test__part1():
    input_data = read_input("inputs/2023/day14.txt")
    assert part_1(input_data) == 110090


def test__part2_sample():
    input_data = """
    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....
    """
    assert part_2(input_data) == 64


def test__part2():
    input_data = read_input("inputs/2023/day14.txt")
    assert part_2(input_data) == 95254
