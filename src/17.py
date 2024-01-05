import heapq


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return [[c for c in line.strip()] for line in input_data.strip().split("\n")]


def solve(grid, part2=False):
    len_r = len(grid)
    len_c = len(grid[0])

    # distance, row, col, direction, dir_count
    hq = [(0, 0, 0, -1, -1)]
    memo = {}

    while hq:
        (distance, row, col, direction, dir_count) = heapq.heappop(hq)
        if (row, col, direction, dir_count) in memo:
            continue
        memo[(row, col, direction, dir_count)] = distance

        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            new_row = row + dr
            new_col = col + dc
            new_dir = i
            new_dir_count = 1 if new_dir != direction else dir_count + 1
            not_reverse = (new_dir + 2) % 4 != direction

            if not part2:
                is_valid = new_dir_count <= 3
            else:
                is_valid = new_dir_count <= 10 and (
                    dir_count >= 4 or new_dir == direction or dir_count == -1
                )

            if (
                0 <= new_row < len_r
                and 0 <= new_col < len_c
                and not_reverse
                and is_valid
            ):
                if (new_row, new_col, new_dir, new_dir_count) in memo:
                    continue
                new_distance = int(grid[new_row][new_col]) + distance
                heapq.heappush(
                    hq, (new_distance, new_row, new_col, new_dir, new_dir_count)
                )

    ret_val = float("inf")
    for (r, c, d, dc), value in memo.items():
        if r == len_r - 1 and c == len_c - 1 and (dc >= 4 if part2 else True):
            ret_val = min(ret_val, value)
    return ret_val


def part_1(input_data: str) -> int:
    grid = parse(input_data)
    return solve(grid, part2=False)


def part_2(input_data: str) -> int:
    grid = parse(input_data)
    return solve(grid, part2=True)


if __name__ == "__main__":
    input_data = read_input("inputs/day17.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    2413432311323
    3215453535623
    3255245654254
    3446585845452
    4546657867536
    1438598798454
    4457876987766
    3637877979653
    4654967986887
    4564679986453
    1224686865563
    2546548887735
    4322674655533
    """
    assert part_1(input_data) == 102


def test__part1():
    input_data = read_input("inputs/day17.txt")
    assert part_1(input_data) == 1013


def test__part2_sample():
    input_data = """
    2413432311323
    3215453535623
    3255245654254
    3446585845452
    4546657867536
    1438598798454
    4457876987766
    3637877979653
    4654967986887
    4564679986453
    1224686865563
    2546548887735
    4322674655533
    """
    assert part_2(input_data) == 94


def test__part2_sample2():
    input_data = """
    111111111111
    999999999991
    999999999991
    999999999991
    999999999991
    """
    assert part_2(input_data) == 71


def test__part2():
    input_data = read_input("inputs/day17.txt")
    assert part_2(input_data) == 0
