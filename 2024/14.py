from collections import defaultdict


INPUT_FILE = "inputs/2024/day14.txt"

# GRID_X = 11
# GRID_Y = 7

GRID_X = 101
GRID_Y = 103


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


class robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self):
        self.px = (self.px + self.vx) % GRID_X
        self.py = (self.py + self.vy) % GRID_Y

    def __repr__(self):
        # print in grid
        grid = [["." for _ in range(GRID_X)] for _ in range(GRID_Y)]
        grid[self.py][self.px] = "#"
        return "\n".join(["".join(row) for row in grid])

    def quadrant(self):
        if self.px < GRID_X // 2 and self.py < GRID_Y // 2:
            return 1
        elif self.px > GRID_X // 2 and self.py < GRID_Y // 2:
            return 2
        elif self.px < GRID_X // 2 and self.py > GRID_Y // 2:
            return 3
        elif self.px > GRID_X // 2 and self.py > GRID_Y // 2:
            return 4


def print_robots(robots):
    grid = [["." for _ in range(GRID_X)] for _ in range(GRID_Y)]
    for r in robots:
        grid[r.py][r.px] = "#"
    print("\n".join(["".join(row) for row in grid]))


def parse(input_data):
    robots = []
    for line in input_data.strip().split("\n"):
        p, v = line.split()
        px, py = [int(pp) for pp in p[2:].split(",")]
        vx, vy = [int(vv) for vv in v[2:].split(",")]
        robots.append(robot(px, py, vx, vy))
    return robots


def part_1(input_data: str) -> int:
    robots = parse(input_data)  # noqa
    quadrants = defaultdict(int)
    for r in robots:
        for _ in range(1, 101):
            r.move()
        quadrants[r.quadrant()] += 1

    # print_robots(robots)

    result = 1
    for v in quadrants.values():
        result *= v
    return quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


def test__part1_sample():
    input_data = """
    p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3
    """
    assert part_1(input_data) == 21


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 222208000


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0

if __name__ == "__main__":
    test__part1_sample()
    # test__part1()
    # test__part2_sample()
    # test__part2()
    # input_data = read_input(INPUT_FILE)
    # print(part_1(input_data))
    # print(part_2(input_data))
