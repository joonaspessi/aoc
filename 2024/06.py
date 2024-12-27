import pytest

INPUT_FILE = "inputs/2024/day6.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    rows = []
    for line in input_data.strip().split("\n"):
        row = list(line.strip())
        rows.append(row)
    x0, y0 = None, None
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if rows[y][x] in "^":
                y0, x0 = y, x
    return rows, y0, x0


def part_1(input_data: str) -> int:
    data, y0, x0 = parse(input_data)
    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0

    visited = set()
    y, x = y0, x0
    while True:
        visited.add((y, x))
        dy, dx = directions[dir]

        y_candidate = y + dy
        x_candidate = x + dx

        if not (0 <= y_candidate < len(data) and 0 <= x_candidate < len(data[0])):
            break

        if data[y_candidate][x_candidate] == "#":
            dir = (dir + 1) % 4
        else:
            y, x = y_candidate, x_candidate

    return len(visited)


def part_2(input_data: str) -> int:
    data, y0, x0 = parse(input_data)
    result = 0

    for y_obstacle in range(len(data)):
        for x_obstacle in range(len(data[0])):
            # up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            dir = 0
            y, x = y0, x0
            visited = set()

            while True:
                if (y, x, dir) in visited:
                    result += 1
                    break

                visited.add((y, x, dir))
                dy, dx = directions[dir]

                y_candidate = y + dy
                x_candidate = x + dx

                if not (
                    0 <= y_candidate < len(data) and 0 <= x_candidate < len(data[0])
                ):
                    break

                if (
                    data[y_candidate][x_candidate] == "#"
                    or y_candidate == y_obstacle
                    and x_candidate == x_obstacle
                ):
                    dir = (dir + 1) % 4
                else:
                    y, x = y_candidate, x_candidate

    return result


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """
    assert part_1(input_data) == 41


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 5067


def test__part2_sample():
    input_data = """
    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...
    """
    assert part_2(input_data) == 6


@pytest.mark.skip("slow")
def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 1793
