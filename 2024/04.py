INPUT_FILE = "inputs/2024/day4.txt"


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


# directions: right, down, left, up, right-down, left-down, left-up, right-up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]


def part_1(input_data: str) -> int:
    data = parse(input_data)
    target = "XMAS"

    def check(x, y, delta):
        # check if the direction contains xmas in the next 3 steps (including the current one)
        if data[y][x] != target[0]:
            return False
        for i in range(1, 4):
            x += delta[0]
            y += delta[1]
            if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
                return False
            if data[y][x] != target[i]:
                return False
        return True

    result = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            for direction in directions:
                result += check(x, y, direction)
    return result


def part_2(input_data: str) -> int:
    data = parse(input_data)

    def check(x, y):
        # check if the direction contains xmas in the next 3 steps (including the current one)
        if data[y][x] != "A":
            return False

        # check directions (right-down, left-down, left-up, right-up)
        for delta in [[(1, 1), (-1, -1)], [(-1, 1), (1, -1)]]:
            x1, y1 = x, y
            x2, y2 = x, y

            x1 += delta[0][0]
            y1 += delta[0][1]
            x2 += delta[1][0]
            y2 += delta[1][1]

            if x1 < 0 or x1 >= len(data[0]) or y1 < 0 or y1 >= len(data):
                return False
            if x2 < 0 or x2 >= len(data[0]) or y2 < 0 or y2 >= len(data):
                return False
            # if if x1 and x2 are either S or M but not same
            if not (
                data[y1][x1] in ["S", "M"]
                and data[y2][x2] in ["S", "M"]
                and data[y1][x1] != data[y2][x2]
            ):
                return False

        return True

    result = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            result += check(x, y)
    return result


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """
    assert part_1(input_data) == 18


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 2532


def test__part2_sample():
    input_data = """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """
    assert part_2(input_data) == 9


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 1941
