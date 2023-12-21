import sys
from math import ceil

sys.setrecursionlimit(50000)
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

connector_map = {
    "|": {
        (-1, 0): ("7", "F", "|"),
        (1, 0): ("L", "J", "|"),
    },
    "-": {
        (0, -1): ("F", "L", "-"),
        (0, 1): ("7", "J", "-"),
    },
    "L": {
        (0, 1): ("-", "J", "7"),
        (-1, 0): ("|", "7", "F"),
    },
    "J": {
        (0, -1): ("-", "F", "L"),
        (-1, 0): ("|", "7", "F"),
    },
    "7": {
        (0, -1): ("-", "F", "L"),
        (1, 0): ("|", "L", "J"),
    },
    "F": {
        (0, 1): ("-", "J", "7"),
        (1, 0): ("|", "L", "J"),
    },
}


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


def can_move(f, t, delta: tuple[int, int]):
    if f == "S" and t != ".":
        return True
    if f == "S":
        return False
    if delta in connector_map[f] and t in connector_map[f][delta]:
        return True
    return False


def is_start(f):
    return f == "S"


def solve(start, grid):
    def dfs(start, grid, visited, ans):
        visited[start] = True
        max_route = ans
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if abs(dy) + abs(dx) != 1:
                    continue

                new_y = start[0] + dy
                new_x = start[1] + dx

                if (
                    new_x < 0
                    or new_y < 0
                    or new_x >= len(grid[0])
                    or new_y >= len(grid)
                ):
                    continue

                if is_start(grid[new_y][new_x]) and ans > 1:
                    return ans + 1

                if (new_y, new_x) in visited:
                    continue

                if can_move(grid[start[0]][start[1]], grid[new_y][new_x], (dy, dx)):
                    candidate = dfs((new_y, new_x), grid, visited.copy(), ans + 1)
                    max_route = max(candidate, max_route)
        return max_route

    max_route = dfs(start, grid, {}, 0)
    return ceil(max_route / 2)


def part_1(input_data: str) -> int:
    start, grid = parse(input_data)
    return solve(start, grid)


def part_2(input_data: str) -> int:
    parsed = parse(input_data)
    ret = 0
    return ret


if __name__ == "__main__":
    input_data = read_input("inputs/day10.txt")
    print(part_1(input_data))


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
