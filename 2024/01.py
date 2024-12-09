from collections import Counter
from bisect import insort


def read_file(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return [line.strip() for line in data]


def part_1(lines):
    x, y = [], []
    for line in lines:
        [a, b] = line.split()
        insort(x, int(a))
        insort(y, int(b))

    diff = []
    for a, b in zip(x, y):
        diff.append(abs(b - a))

    return sum(diff)


def part_2(lines):
    x, y = [], []
    for line in lines:
        [a, b] = line.split()
        x.append(int(a))
        y.append(int(b))
    counts = Counter(y)
    result = 0
    for a in x:
        result += a * counts[a]
    return result


lines = read_file("inputs/2024/day1.txt")

print(f"part 1: {part_1(lines)}")
print(f"part 2: {part_2(lines)}")


def test__part1():
    lines = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    assert part_1(lines) == 11


def test__part2():
    lines = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    assert part_2(lines) == 31
