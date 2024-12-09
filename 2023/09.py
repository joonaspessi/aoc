def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str):
    return [
        [int(d) for d in line.strip().split()]
        for line in input_data.strip().split("\n")
    ]


def predict(measurement: list[int], part2: bool = False):
    stack = []
    stack.append(measurement)
    result = []
    result.append(measurement)
    while stack:
        m = stack.pop()
        r = []
        for i in range(1, len(m)):
            r.append(m[i] - m[i - 1])
        # Check if all values in r are zero
        result.append(r)
        if not all(value == 0 for value in r):
            stack.append(r)
    result.reverse()
    val = 0
    for i in range(1, len(result)):
        if part2:
            val = result[i][0] - val
        else:
            val += result[i][-1]
    return val


def part_1(input_data: str) -> int:
    parsed = parse(input_data)
    sum = 0
    for line in parsed:
        sum += predict(line)
    return sum


def part_2(input_data: str) -> int:
    parsed = parse(input_data)
    sum = 0
    for line in parsed:
        sum += predict(line, True)
    return sum


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day9.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """
    assert part_1(input_data) == 114


def test__part1():
    input_data = read_input("inputs/2023/day9.txt")
    assert part_1(input_data) == 1806615041


def test__part2_predict():
    assert predict([10, 13, 16, 21, 30, 45], True) == 5


def test__part2_sample():
    input_data = """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """
    assert part_2(input_data) == 2


def test__part2():
    input_data = read_input("inputs/2023/day9.txt")
    assert part_2(input_data) == 1211
