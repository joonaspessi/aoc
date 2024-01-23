from numpy import rint
from numpy.polynomial.polynomial import polyfit


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


def step(grid, positions, part2):
    len_r = len(grid)
    len_c = len(grid[0])
    new_positions = set()
    for r, c in positions:
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new_r, new_c = wrap(grid, r + dr, c + dc) if part2 else (r + dr, c + dc)
            if 0 <= new_r < len_r and 0 <= new_c < len_c and grid[new_r][new_c] != "#":
                new_positions.add((r + dr, c + dc))
    return new_positions


def wrap(grid, r, c):
    len_r = len(grid)
    len_c = len(grid[0])
    return r % len_r, c % len_c


def part_1(input_data: str) -> int:
    grid, sr, rc = parse(input_data)

    pos = set([(sr, rc)])
    for _ in range(64):
        pos = step(grid, pos, False)

    return len(pos)


def part_2(input_data: str) -> int:
    grid, sr, rc = parse(input_data)

    size = len(grid)
    size_2 = size // 2
    y = []
    pos = set([(sr, rc)])
    for s in range(size_2 + size * 2 + 1):
        if s % size == size_2:
            y.append(len(pos))
        pos = step(grid, pos, True)

    x = [0, 1, 2]
    poly = rint(polyfit(x, y, 2)).astype(int).tolist()

    target = (26501365 - size_2) // size

    return sum([poly[i] * target**i for i in range(3)])


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
    .................................
    .....###.#......###.#......###.#.
    .###.##..#..###.##..#..###.##..#.
    ..#.#...#....#.#...#....#.#...#..
    ....#.#........#.#........#.#....
    .##...####..##...####..##...####.
    .##..#...#..##..#...#..##..#...#.
    .......##.........##.........##..
    .##.#.####..##.#.####..##.#.####.
    .##..##.##..##..##.##..##..##.##.
    .................................
    .................................
    .....###.#......###.#......###.#.
    .###.##..#..###.##..#..###.##..#.
    ..#.#...#....#.#...#....#.#...#..
    ....#.#........#.#........#.#....
    .##...####..##..S####..##...####.
    .##..#...#..##..#...#..##..#...#.
    .......##.........##.........##..
    .##.#.####..##.#.####..##.#.####.
    .##..##.##..##..##.##..##..##.##.
    .................................
    .................................
    .....###.#......###.#......###.#.
    .###.##..#..###.##..#..###.##..#.
    ..#.#...#....#.#...#....#.#...#..
    ....#.#........#.#........#.#....
    .##...####..##...####..##...####.
    .##..#...#..##..#...#..##..#...#.
    .......##.........##.........##..
    .##.#.####..##.#.####..##.#.####.
    .##..##.##..##..##.##..##..##.##.
    .................................
    """
    assert part_2(input_data) == 475308805510348


def test__part2():
    input_data = read_input("inputs/day21.txt")
    assert part_2(input_data) == 639051580070841
