from functools import reduce


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str, part_2=False):
    times = [
        int(t) for t in input_data.strip().split("\n")[0].split(":")[1].strip().split()
    ]
    distances = [
        int(t) for t in input_data.strip().split("\n")[1].split(":")[1].strip().split()
    ]

    if part_2:
        t2 = int("".join([str(t) for t in times]))
        d2 = int("".join([str(d) for d in distances]))
        return [(t2, d2)]

    return list(zip(times, distances))


def calculate_faster_count(t, d):
    return sum((t - i) * i > d for i in range(t + 1))


def part_1(input_data: str) -> int:
    races = parse(input_data)
    result = [calculate_faster_count(t, d) for t, d in races]
    return reduce(lambda x, y: x * y, result)


def part_2(input_data: str) -> int:
    races = parse(input_data, part_2=True)
    result = [calculate_faster_count(t, d) for t, d in races]
    return reduce(lambda x, y: x * y, result)


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day6.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    sample = """
    Time:      7  15   30
    Distance:  9  40  200
    """
    assert part_1(sample) == 288


def test__part1():
    assert part_1(read_input("inputs/2023/day6.txt")) == 220320


def test__part2_sample():
    sample = """
    Time:      7  15   30
    Distance:  9  40  200
    """
    assert part_2(sample) == 71503


def test__part2():
    assert part_2(read_input("inputs/2023/day6.txt")) == 34454850
