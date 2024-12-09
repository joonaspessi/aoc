def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str):
    chunks = input_data.strip().split("\n\n")

    patterns = []
    for chunk in chunks:
        chunk = [[x for x in c.strip()] for c in chunk.split("\n")]
        patterns.append(chunk)
    return patterns


def solve(patterns, part2=False) -> int:
    ret = 0
    for pattern in patterns:
        r_len = len(pattern)
        c_len = len(pattern[0])

        for r in range(r_len - 1):
            mismatches = 0
            for dr in range(r_len):
                u = r - dr
                d = r + dr + 1
                if 0 <= u < d < r_len:
                    for c in range(c_len):
                        if pattern[u][c] != pattern[d][c]:
                            mismatches += 1
            if mismatches == (1 if part2 else 0):
                ret += (r + 1) * 100

        for c in range(c_len - 1):
            mismatches = 0
            for dc in range(c_len):
                ll = c - dc
                d = c + dc + 1
                if 0 <= ll < d < c_len:
                    for r in range(r_len):
                        if pattern[r][ll] != pattern[r][d]:
                            mismatches += 1
            if mismatches == (1 if part2 else 0):
                ret += c + 1
    return ret


def part_1(input_data: str) -> int:
    return solve(parse(input_data))


def part_2(input_data: str) -> int:
    return solve(parse(input_data), True)


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day13.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#
    """
    assert part_1(input_data) == 405


def test__part1():
    input_data = read_input("inputs/2023/day13.txt")
    assert part_1(input_data) == 34993


def test__part2_sample():
    input_data = """
    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#
    """
    assert part_2(input_data) == 400


def test__part2():
    input_data = read_input("inputs/2023/day13.txt")
    assert part_2(input_data) == 29341
