INPUT_FILE = "inputs/2024/day18.txt"
from itertools import islice
import re
import heapq

GRID_SIZE = 70


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def take(n, iterable):
    return list(islice(iterable, n))


def create_grid(obstacles):
    ob = {}
    for o in obstacles:
        ob[o] = True

    grid = []
    for r in range(GRID_SIZE + 1):
        row = []
        for c in range(GRID_SIZE + 1):
            if (r, c) in obstacles:
                row.append("#")
            else:
                row.append(".")
        grid.append(row)
    return grid


def parse(input_data):
    obstacles = []
    for r in input_data.strip().split("\n"):
        x, y = re.findall(r"\d+", r)
        obstacles.append((int(x), int(y)))
    return obstacles


def part_1(input_data: str) -> int:
    obstacles = parse(input_data)
    obstacles = obstacles[:1024]
    grid = create_grid(obstacles)

    r_len = len(grid)
    c_len = len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = []
    seen = set()
    heapq.heappush(q, (0, 0, 0))

    while q:
        d, r, c = heapq.heappop(q)
        if r == r_len - 1 and c == c_len - 1:
            return d
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            if 0 <= rr < r_len and 0 <= cc < c_len and grid[rr][cc] != "#":
                heapq.heappush(q, (d + 1, rr, cc))

    return -1  # if no path is found


def djikstra(grid):
    r_len = len(grid)
    c_len = len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = []
    seen = set()
    heapq.heappush(q, (0, 0, 0))

    while q:
        d, r, c = heapq.heappop(q)
        if r == r_len - 1 and c == c_len - 1:
            return d
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            if 0 <= rr < r_len and 0 <= cc < c_len and grid[rr][cc] != "#":
                heapq.heappush(q, (d + 1, rr, cc))

    return -1


def part_2(input_data: str) -> int:
    obstacles = parse(input_data)

    index = None
    for i in range(2900, 3000):
        o = obstacles[:i]
        g = create_grid(o)
        result = djikstra(g)
        if result == -1:
            index = i
            break

    invalid_byte = obstacles[index - 1]
    result = f"{invalid_byte[0]},{invalid_byte[1]}"
    return result


def test__part1_sample():
    input_data = """
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    1,5
    0,6
    3,3
    2,6
    5,1
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    6,1
    1,0
    0,5
    1,6
    2,0
    """
    assert part_1(input_data) == 0


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 340


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == "34,32"


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
