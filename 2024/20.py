from collections import deque
import heapq

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

INPUT_FILE = "inputs/2024/day20.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    rows = []
    start = None
    end = None
    for line in input_data.strip().split("\n"):
        l = []
        for c in list(line.strip()):
            l.append(c)
        rows.append(l)

    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            if ch == "E":
                end = (r, c)
    return rows, start, end


def reverse_distances(grid, end):
    dist = {}
    q = deque([(0, end[0], end[1])])
    while q:
        d, r, c = q.popleft()
        if (r, c) in dist:
            continue
        dist[(r, c)] = d

        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] != "#":
                q.append((d + 1, rr, cc))
    return dist


def solve(grid, start, dist, cheat_count):
    d0 = dist[start]
    limit = 100
    r_len = len(grid)
    c_len = len(grid[0])

    q = deque()
    seen = set()
    results = set()
    # (picoseconds, cheat_start, cheat_end, cheat_available,row, col)
    q.append((0, None, None, None, start[0], start[1]))
    while q:
        d, cheat_start, cheat_end, cheat_time, r, c = q.popleft()

        if d >= d0 - limit:
            continue

        if grid[r][c] == "E":
            if cheat_end is None:
                cheat_end = (r, c)
            if d <= d0 - limit:
                assert cheat_start is not None

                results.add((d0 - d, cheat_start, cheat_end))

        if (r, c, cheat_start, cheat_end, cheat_time) in seen:
            continue

        seen.add((r, c, cheat_start, cheat_end, cheat_time))

        # always start trying to cheat
        if cheat_start is None:
            assert grid[r][c] != "#"
            q.append((d, (r, c), None, cheat_count, r, c))

        if cheat_time is not None and grid[r][c] != "#":
            if dist[(r, c)] <= d0 - limit - d:
                results.add((d0 - d - dist[(r, c)], cheat_start, (r, c)))

        if cheat_time == 0:
            continue
        else:
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if 0 <= rr < r_len and 0 <= cc < c_len:
                    if cheat_time is not None:
                        assert cheat_time > 0
                        q.append((d + 1, cheat_start, None, cheat_time - 1, rr, cc))
                    else:
                        if grid[rr][cc] != "#":
                            q.append(
                                (d + 1, cheat_start, cheat_end, cheat_time, rr, cc)
                            )

    return len(results)


def part_1(input_data: str) -> int:
    grid, start, end = parse(input_data)
    dist = reverse_distances(grid, end)
    results = solve(grid, start, dist, cheat_count=2)
    return results


def part_2(input_data: str) -> int:
    grid, start, end = parse(input_data)
    dist = reverse_distances(grid, end)
    results = solve(grid, start, dist, cheat_count=20)
    return results


def test__part1_sample():
    input_data = """
    ###############
    #...#...#.....#
    #.#.#.#.#.###.#
    #S#...#.#.#...#
    #######.#.#.###
    #######.#.#...#
    #######.#.###.#
    ###..E#...#...#
    ###.#######.###
    #...###...#...#
    #.#####.#.###.#
    #.#...#.#.#...#
    #.#.#.#.#.#.###
    #...#...#...###
    ###############
    """
    assert part_1(input_data) == 0


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 1445


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 0


if __name__ == "__main__":
    # test__part1_sample()
    test__part1()
    # test__part2_sample()
    # test__part2()
    # input_data = read_input(INPUT_FILE)
    # print(part_1(input_data))
    # print(part_2(input_data))
