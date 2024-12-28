from collections import defaultdict, deque
from typing import Tuple

INPUT_FILE = "inputs/2024/day10.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    grid = []
    for line in input_data.strip().split("\n"):
        row = list(line.strip())
        grid.append([int(r) for r in row])
    return grid


def bfs(grid, y, x):
    result = 0
    stack = deque([(y, x)])
    seen = set()

    while stack:
        y, x = stack.popleft()
        if (y, x) in seen:
            continue
        seen.add((y, x))
        if grid[y][x] == 0:
            result += 1
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx
            if (
                0 <= yy < len(grid)
                and 0 <= xx < len(grid[0])
                and grid[yy][xx] == grid[y][x] - 1
            ):
                stack.append((yy, xx))
    return result


def part_1(input_data: str) -> int:
    grid = parse(input_data)
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 9:
                result += bfs(grid, y, x)

    return result


def dynamic_programming(grid, y, x, cache):
    if grid[y][x] == 0:
        return 1
    if (y, x) in cache:
        return cache[(y, x)]
    result = 0
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        yy = y + dy
        xx = x + dx
        if (
            0 <= yy < len(grid)
            and 0 <= xx < len(grid[0])
            and grid[yy][xx] == grid[y][x] - 1
        ):
            result = result + dynamic_programming(grid, yy, xx, cache)
    cache[(y, x)] = result
    return result


def part_2(input_data: str) -> int:
    grid = parse(input_data)
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 9:
                result += dynamic_programming(grid, y, x, {})

    return result


def test__part1_sample():
    input_data = """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
    assert part_1(input_data) == 36


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 574


def test__part2_sample():
    input_data = """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
    assert part_2(input_data) == 81


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 1238


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
