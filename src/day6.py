from functools import reduce


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str):
    times = [
        int(t) for t in input_data.strip().split("\n")[0].split(":")[1].strip().split()
    ]
    distances = [
        int(t) for t in input_data.strip().split("\n")[1].split(":")[1].strip().split()
    ]
    return list(zip(times, distances))


def calculate_distance(t, i):
    speed = i
    time_to_move = t - i
    return time_to_move * speed


def part_1(input_data: str) -> int:
    races = parse(input_data)
    result = []
    for t, d in races:
        count = 0
        for i in range(0, t + 1):
            count += int(calculate_distance(t, i) > d)
        result.append(count)

    return reduce(lambda x, y: x * y, result)


if __name__ == "__main__":
    input_data = read_input("inputs/day6.txt")
    print(part_1(input_data))
    # print(part_2(input_data))


def test__part1_sample():
    sample = """
    Time:      7  15   30
    Distance:  9  40  200
    """
    assert part_1(sample) == 288


def test__part1():
    assert part_1(read_input("inputs/day6.txt")) == 279
