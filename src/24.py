import re
from typing import Optional, Tuple

from sympy import Symbol, solve_poly_system


class HailStone:
    def __init__(self, x, y, z, dx, dy, dz):
        self.p = [x, y, z]
        self.v = [dx, dy, dz]

    def intersects(self, other) -> Tuple[Optional[int], Optional[int]]:
        x, y, _ = self.p
        vx, vy, _ = self.v
        line1 = ((x, y), (x + vx, y + vy))

        x, y, _ = other.p
        vx, vy, _ = other.v
        line2 = ((x, y), (x + vx, y + vy))

        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)

        if div == 0:
            return None, None

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div

        if self.is_future(x) and other.is_future(x):
            return x, y

        return (None, None)

    def is_future(self, nx):
        x = self.p[0]
        v = self.v[0]
        return (nx - x) / v >= 0


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return [
        list(map(int, re.findall("-?\d+", line)))
        for line in input_data.strip().splitlines()
    ]


def part_1(input_data: str, ta_min=200000000000000, ta_max=400000000000000) -> int:
    data = parse(input_data)  # noqa
    hailstones = list(map(lambda d: HailStone(*d), data))

    ans = 0
    for i in range(len(hailstones) - 1):
        for j in range(i + 1, len(hailstones)):
            x, y = hailstones[i].intersects(hailstones[j])
            if x is None or y is None:
                continue
            if ta_min <= x <= ta_max and ta_min <= y <= ta_max:
                ans += 1

    return ans


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    hailstones = list(map(lambda d: HailStone(*d), data))

    x, y, z, vx, vy, vz = (Symbol(c) for c in "x,y,z,vx,vy,vz".split(","))
    p = [x, y, z]
    v = [vx, vy, vz]
    vars = [*p, *v]
    eqs = []
    for i, hs in enumerate(hailstones[:3]):
        t = Symbol(f"t_{i}")
        vars.append(t)
        for j in range(3):
            eqs.append(p[j] + v[j] * t - (hs.p[j] + hs.v[j] * t))
    return int(sum(solve_poly_system(eqs, vars)[0][:3]))


if __name__ == "__main__":
    input_data = read_input("inputs/day24.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    19, 13, 30 @ -2,  1, -2
    18, 19, 22 @ -1, -1, -2
    20, 25, 34 @ -2, -2, -4
    12, 31, 28 @ -1, -2, -1
    20, 19, 15 @  1, -5, -3
    """
    assert part_1(input_data, ta_min=7, ta_max=27) == 2


def test__part1():
    input_data = read_input("inputs/day24.txt")
    assert part_1(input_data) == 15262


def test__part2_sample():
    input_data = """
    19, 13, 30 @ -2,  1, -2
    18, 19, 22 @ -1, -1, -2
    20, 25, 34 @ -2, -2, -4
    12, 31, 28 @ -1, -2, -1
    20, 19, 15 @  1, -5, -3
    """
    assert part_2(input_data) == 47


def test__part2():
    input_data = read_input("inputs/day24.txt")
    assert part_2(input_data) == 695832176624149
