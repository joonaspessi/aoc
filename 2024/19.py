from collections import deque


INPUT_FILE = "inputs/2024/day19.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    towels, combinations = input_data.strip().split("\n\n")

    t = []
    for towel in towels.strip().split(","):
        t.append(towel.strip())

    c = []
    for comb in combinations.strip().split("\n"):
        c.append(comb.strip())
    return t, c


def solve(towels, comb, db):
    if comb in db:
        return db[comb]
    ans = 0
    if not comb:
        ans = 1
    for t in towels:
        if comb.startswith(t):
            ans += solve(towels, comb[len(t) :], db)
    db[comb] = ans
    return ans


def part_1(input_data: str) -> int:
    towels, comb = parse(input_data)
    result = 0
    for c in comb:
        ans = solve(towels, c, {})
        if ans > 0:
            result += 1
    return result


def part_2(input_data: str) -> int:
    towels, comb = parse(input_data)
    result = 0
    for c in comb:
        result += solve(towels, c, {})
    return result


def test__part1_sample():
    input_data = """
    r, wr, b, g, bwu, rb, gb, br

    brwrr
    bggr
    gbbr
    rrbgbr
    ubwu
    bwurrg
    brgr
    bbrgwb
    """
    assert part_1(input_data) == 6


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 285


def test__part2_sample():
    input_data = """
    r, wr, b, g, bwu, rb, gb, br

    brwrr
    bggr
    gbbr
    rrbgbr
    ubwu
    bwurrg
    brgr
    bbrgwb
    """
    assert part_2(input_data) == 16


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 0


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
