def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    grid = [[c for c in line.strip()] for line in input_data.strip().split("\n")]
    sr, sc = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                sr, sc = r, c

    return grid, sr, sc


def step(grid, positions):
    len_r = len(grid)
    len_c = len(grid[0])
    new_positions = set()
    for r, c in positions:
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            if 0 <= r + dr < len_r and 0 <= c + dc < len_c and grid[r + dr][c + dc] != "#":
                new_positions.add((r + dr, c + dc))
    return new_positions


def part_1(input_data: str) -> int:
    grid, sr, rc = parse(input_data)  # noqa

    pos = set([(sr, rc)])
    for _ in range(64):
        pos = step(grid, pos)

    return len(pos)


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day21.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    """
    assert part_1(input_data) == 42


def test__part1():
    input_data = read_input("inputs/day21.txt")
    assert part_1(input_data) == 3853


def test__part2_sample():
    input_data = """
    xxx
    """
    assert part_2(input_data) == 0


def test__part2():
    input_data = read_input("inputs/day21.txt")
    assert part_2(input_data) == 0
