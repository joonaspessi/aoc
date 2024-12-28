INPUT_FILE = "inputs/2024/day11.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    data = [int(d) for d in input_data.strip().split()]
    return data


def blink(stone, n, cache):
    if (stone, n) in cache:
        return cache[(stone, n)]

    if n == 0:
        result = 1
    elif stone == 0:
        result = blink(1, n - 1, cache)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        half = len(stone_str) // 2
        left = stone_str[:half]
        right = stone_str[half:]
        result = blink(int(left), n - 1, cache) + blink(int(right), n - 1, cache)
    else:
        result = blink(stone * 2024, n - 1, cache)
    cache[(stone, n)] = result
    return result


def part_1(input_data: str) -> int:
    stones = parse(input_data)

    result = 0
    for stone in stones:
        result += blink(stone, 25, {})
    return result


def part_2(input_data: str) -> int:
    stones = parse(input_data)
    result = 0
    for stone in stones:
        result += blink(stone, 75, {})
    return result


def test__part1_sample():
    input_data = """
    125 17
    """
    assert part_1(input_data) == 55312


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 198089


def test__part2_sample():
    input_data = """
    125 17
    """
    assert part_2(input_data) == 65601038650482


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 236302670835517


if __name__ == "__main__":
    test__part2_sample()
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
