def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data, part2=False):
    res = []
    for line in input_data.strip().split("\n"):
        line = line.strip()
        springs, cond = line.split(" ")
        if part2:
            springs = "?".join([springs, springs, springs, springs, springs])
            cond = ",".join([cond, cond, cond, cond, cond])
        cond = [int(c) for c in cond.split(",")]
        res.append((springs, cond))
    return res


def solve(springs, cond):
    dp = {}

    def _solve(springs, cond, i, ci, current):
        key = (i, ci, current)
        if key in dp:
            return dp[key]

        if i == len(springs):
            if ci == len(cond) and current == 0:
                return 1
            elif ci == len(cond) - 1 and cond[ci] == current:
                return 1
            else:
                return 0

        ans = 0
        for c in [".", "#"]:
            if springs[i] == c or springs[i] == "?":
                if c == "." and current == 0:
                    ans += _solve(springs, cond, i + 1, ci, 0)
                elif (
                    c == "." and current > 0 and ci < len(cond) and cond[ci] == current
                ):
                    ans += _solve(springs, cond, i + 1, ci + 1, 0)
                elif c == "#":
                    ans += _solve(springs, cond, i + 1, ci, current + 1)
        dp[key] = ans
        return ans

    return _solve(springs, cond, 0, 0, 0)


def part_1(input_data: str) -> int:
    data = parse(input_data)
    ret = 0
    for springs, cond in data:
        ret += solve(springs, cond)
    return ret


def part_2(input_data: str) -> int:
    data = parse(input_data, True)
    ret = 0
    for springs, cond in data:
        ret += solve(springs, cond)
    return ret


if __name__ == "__main__":
    input_data = read_input("inputs/day12.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    ???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1
    """
    assert part_1(input_data) == 21


def test__part1():
    input_data = read_input("inputs/day12.txt")
    assert part_1(input_data) == 7506


def test__part2_sample():
    input_data = """
    ???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1
    """
    assert part_2(input_data) == 525152


def test__part2():
    input_data = read_input("inputs/day12.txt")
    assert part_2(input_data) == 548241300348335
