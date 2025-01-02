from collections import deque
import heapq

INPUT_FILE = "inputs/2024/day16.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    start = (0, 0)
    end = (0, 0)
    rows = []
    for r, row in enumerate(input_data.strip().split("\n")):
        line_data = []
        for c, ch in enumerate(list(row.strip())):
            if ch == "E":
                end = (r, c)
            if ch == "S":
                start = (r, c)
            if ch == "#":
                line_data.append("#")
            else:
                line_data.append(".")
        rows.append(line_data)
    return rows, start, end


def part_1(input_data: str) -> int:
    data, start, end = parse(input_data)

    sr, sc = start
    er, ec = end

    r_len = len(data)
    c_len = len(data[0])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = []
    seen = set()
    heapq.heappush(q, (0, sr, sc, 1))
    dist = {}
    best = None
    while q:
        d, r, c, dir = heapq.heappop(q)
        if (r, c, dir) not in dist:
            dist[(r, c, dir)] = d
        if r == er and c == ec and best is None:
            best = d
            break
        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))
        dr, dc = dirs[dir]
        rr, cc = r + dr, c + dc
        if 0 <= rr < r_len and 0 <= cc < c_len and data[rr][cc] != "#":
            heapq.heappush(q, (d + 1, rr, cc, dir))
        heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))

    return best


def part_2(input_data: str) -> int:
    grid, start, end = parse(input_data)

    sr, sc = start
    er, ec = end

    r_len = len(grid)
    c_len = len(grid[0])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = []
    seen = set()
    heapq.heappush(q, (0, sr, sc, 1))
    dist = {}
    best = None
    while q:
        d, r, c, dir = heapq.heappop(q)
        if (r, c, dir) not in dist:
            dist[(r, c, dir)] = d
        if r == er and c == ec and best is None:
            best = d
        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))
        dr, dc = dirs[dir]
        rr, cc = r + dr, c + dc
        if 0 <= rr < r_len and 0 <= cc < c_len and grid[rr][cc] != "#":
            heapq.heappush(q, (d + 1, rr, cc, dir))
        heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))

    q = []
    seen = set()
    for dir in range(4):
        heapq.heappush(q, (0, er, ec, dir))
    dist2 = {}
    while q:
        d, r, c, dir = heapq.heappop(q)
        if (r, c, dir) not in dist2:
            dist2[(r, c, dir)] = d
        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))
        dr, dc = dirs[(dir + 2) % 4]
        rr, cc = r + dr, c + dc
        if 0 <= cc < c_len and 0 <= rr < r_len and grid[rr][cc] != "#":
            heapq.heappush(q, (d + 1, rr, cc, dir))
        heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))

    ok = set()
    for r in range(r_len):
        for c in range(c_len):
            for dir in range(4):
                if (
                    (r, c, dir) in dist
                    and (r, c, dir) in dist2
                    and dist[(r, c, dir)] + dist2[(r, c, dir)] == best
                ):
                    ok.add((r, c))
    return len(ok)


def test__part1_sample():
    input_data = """
    ###############
    #.......#....E#
    #.#.###.#.###.#
    #.....#.#...#.#
    #.###.#####.#.#
    #.#.#.......#.#
    #.#.#####.###.#
    #...........#.#
    ###.#.#####.#.#
    #...#.....#.#.#
    #.#.#.###.#.#.#
    #.....#...#.#.#
    #.###.#.#.#.#.#
    #S..#.....#...#
    ###############
    """
    assert part_1(input_data) == 7036


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 78428


def test__part2_sample():
    input_data = """
    ###############
    #.......#....E#
    #.#.###.#.###.#
    #.....#.#...#.#
    #.###.#####.#.#
    #.#.#.......#.#
    #.#.#####.###.#
    #...........#.#
    ###.#.#####.#.#
    #...#.....#.#.#
    #.#.#.###.#.#.#
    #.....#...#.#.#
    #.###.#.#.#.#.#
    #S..#.....#...#
    ###############
    """
    assert part_2(input_data) == 45


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 463


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
