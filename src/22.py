import re
from collections import defaultdict


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    grid = [
        list(map(int, re.findall("-?\d+", line))) + [i]
        for i, line in enumerate(input_data.strip().splitlines())
    ]
    grid.sort(key=lambda x: x[2])
    return grid


def solve(grid):
    highestZ = defaultdict(lambda: (0, -1))
    sitsOn = defaultdict(set)
    children = defaultdict(set)

    for b in grid:
        x1, y1, z1, x2, y2, z2, i = b
        newZ = 0
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                newZ = max(newZ, highestZ[(x, y)][0])
        height = z2 - z1 + 1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                old = highestZ[(x, y)]
                if old[0] == newZ:
                    sitsOn[i].add(old[1])
                    children[old[1]].add(i)
                highestZ[(x, y)] = (newZ + height, i)

    for c in children[-1]:
        del sitsOn[c]
    del children[-1]

    unsafe = set()
    for k, v in sitsOn.items():
        if len(v) == 1:
            unsafe |= v

    return unsafe, children


def part_1(input_data: str) -> int:
    grid = parse(input_data)
    unsafe, _ = solve(grid)
    return len(grid) - len(unsafe)


def getDependencies(children, b):
    inDeg = defaultdict(int)
    for kids in children.values():
        for c in kids:
            inDeg[c] += 1
    dep = -1
    q = [b]
    while q:
        i = q.pop()
        dep += 1
        for c in children[i]:
            inDeg[c] -= 1
            if inDeg[c] == 0:
                q.append(c)

    return dep


def part_2(input_data: str) -> int:
    grid = parse(input_data)
    unsafe, children = solve(grid)

    result = 0
    for u in unsafe:
        result += getDependencies(children, u)

    return result


if __name__ == "__main__":
    input_data = read_input("inputs/day22.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    1,0,1~1,2,1
    0,0,2~2,0,2
    0,2,3~2,2,3
    0,0,4~0,2,4
    2,0,5~2,2,5
    0,1,6~2,1,6
    1,1,8~1,1,9
    """
    assert part_1(input_data) == 5


def test__part1():
    input_data = read_input("inputs/day22.txt")
    assert part_1(input_data) == 0


def test__part2_sample():
    input_data = """
    1,0,1~1,2,1
    0,0,2~2,0,2
    0,2,3~2,2,3
    0,0,4~0,2,4
    2,0,5~2,2,5
    0,1,6~2,1,6
    1,1,8~1,1,9
    """
    assert part_2(input_data) == 7


def test__part2():
    input_data = read_input("inputs/day22.txt")
    assert part_2(input_data) == 79042
