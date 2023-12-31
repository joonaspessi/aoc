def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return [[c for c in row.strip()] for row in input_data.strip().split("\n")]


def move(grid, r, c):
    if r == 0 or grid[r - 1][c] in ["#", "O"]:
        return (r, c)
    return move(grid, r - 1, c)


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
    for c in range(len(grid[0])):
        for r in range(len(grid)):
            if grid[r][c] == "O":
                nr, nc = move(grid, r, c)
                grid[r][c] = "."
                grid[nr][nc] = "O"

    return clc_ld(grid)


def part_2(input_data: str) -> int:
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day14.txt")
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
    input_data = read_input("inputs/day14.txt")
    assert part_1(input_data) == 110090


def test__part2_sample():
    input_data = """
    xxx
    """
    assert part_1(input_data) == 0


def test__part2():
    input_data = read_input("inputs/day4.txt")
    assert part_2(input_data) == 0
