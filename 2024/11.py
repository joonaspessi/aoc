INPUT_FILE = "inputs/2024/day11.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    data = input_data.strip().split()
    return data


def blink(stones):
    result = []
    for stone in stones:
        if stone == "0":
            result.append("1")
        elif len(stone) % 2 == 0:
            # split string in half
            half = len(stone) // 2
            left = stone[:half]
            right = stone[half:]
            result.append(str(int(left)))
            result.append(str(int(right)))
        else:
            # multiply by 2024
            result.append(str(int(stone) * 2024))
    return result


def part_1(input_data: str) -> int:
    stones = parse(input_data)  # noqa
    for _ in range(25):
        stones = blink(stones)
        pass
    return len(stones)


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


def test__part1_sample():
    input_data = """
    125 17
    """
    assert part_1(input_data) == 55312


# def test__part1():
#     input_data = read_input(INPUT_FILE)
#     assert part_1(input_data) == 0


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0

if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    # print(part_2(input_data))
