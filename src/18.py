def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data, part2=False):
    lines = [
        [c for c in line.strip().split(" ")] for line in input_data.strip().split("\n")
    ]
    if not part2:
        lines1 = []
        for line in lines:
            lines1.append((line[0], line[1]))
        return lines1
    else:
        lines2 = []
        for line in lines:
            h = line[2]
            d = {"0": "R", "1": "D", "2": "L", "3": "U"}[h[-2]]
            n = int(h[2:-2], 16)
            lines2.append((d, n))
        return lines2


def shoelace(data):
    corners = []
    pos = (0, 0)
    for d, n in data:
        n = int(n)
        if d == "U":
            pos = (pos[0], pos[1] + n)
        if d == "R":
            pos = (pos[0] + n, pos[1])
        if d == "D":
            pos = (pos[0], pos[1] - n)
        if d == "L":
            pos = (pos[0] - n, pos[1])
        corners.append(pos)

    area = 0
    for i in range(len(corners)):
        area -= corners[i][0] * corners[(i + 1) % len(corners)][1]
        area += corners[i][1] * corners[(i + 1) % len(corners)][0]

    area = area // 2
    return area


def perimeter(data):
    perimeter = 0
    for d, n in data:
        n = int(n)
        perimeter += n
    return perimeter


def part_1(input_data: str):
    data = parse(input_data)
    a = shoelace(data)
    p = perimeter(data)
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    return a + p // 2 + 1


def part_2(input_data: str) -> int:
    data = parse(input_data, part2=True)
    a = shoelace(data)
    p = perimeter(data)
    return a + p // 2 + 1


if __name__ == "__main__":
    input_data = read_input("inputs/day18.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)
    """
    assert part_1(input_data) == 62


def test__part1():
    input_data = read_input("inputs/day18.txt")
    assert part_1(input_data) == 52055


def test__part2_sample():
    input_data = """
    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)
    """
    assert part_2(input_data) == 952408144115


def test__part2():
    input_data = read_input("inputs/day18.txt")
    assert part_2(input_data) == 67622758357096
