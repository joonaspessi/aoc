from collections import deque


INPUT_FILE = "inputs/2024/day12.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    rows = []
    for line in input_data.strip().split("\n"):
        row = list(line.strip())
        rows.append(row)
    return rows


def part_1(input_data: str) -> int:
    grid = parse(input_data)
    r_len = len(grid)
    c_len = len(grid[0])

    seen = set()

    result = 0

    for r in range(r_len):
        for c in range(c_len):
            if (r, c) in seen:
                continue
            q = deque([(r, c)])

            area = 0
            perim = 0

            while q:
                rr, cc = q.popleft()
                if (rr, cc) in seen:
                    continue
                seen.add((rr, cc))
                area += 1

                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    rrr = rr + dr
                    ccc = cc + dc
                    if (
                        0 <= rrr < r_len
                        and 0 <= ccc < c_len
                        and grid[rrr][ccc] == grid[rr][cc]
                    ):
                        q.append((rrr, ccc))
                    else:
                        perim += 1

            result += area * perim

    return result


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


def test__part1_sample():
    input_data = """
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
    """
    assert part_1(input_data) == 1930


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 1424472


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0

if __name__ == "__main__":
    test__part1()
    # input_data = read_input(INPUT_FILE)
    # print(part_1(input_data))
    # print(part_2(input_data))
