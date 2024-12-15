from collections import deque


INPUT_FILE = "inputs/2024/day9.txt"


class File:
    def __init__(self, pos, size, file_id):
        self.pos = pos
        self.size = size
        self.file_id = file_id


class Space:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    files = deque([])
    spaces = deque([])
    parsed = []
    file_id = 0
    pos = 0
    for idx, c in enumerate(input_data.strip()):
        if idx % 2 == 0:
            files.append(File(pos, int(c), file_id))

            for i in range(int(c)):
                parsed.append(file_id)
                pos += 1
            file_id += 1
        else:
            spaces.append(Space(pos, int(c)))
            for i in range(int(c)):
                parsed.append(None)
                pos += 1
    return parsed, files, spaces


def part_1(input_data: str) -> int:
    data, _, _ = parse(input_data)

    left = 0
    right = len(data) - 1
    result = []
    while left <= right:
        if data[left] is None and data[right] is not None:
            result.append(data[right])
            left += 1
            right -= 1
        elif data[left] is None and data[right] is None:
            right -= 1
        else:
            result.append(data[left])
            left += 1

    ans = 0
    for i, c in enumerate(result):
        if c is not None:
            ans += i * c
    return ans


def part_2(input_data: str) -> int:
    data, files, spaces = parse(input_data)

    for file in reversed(files):
        for i, space in enumerate(spaces):
            if space.pos < file.pos and file.size <= space.size:
                for i in range(file.size):
                    data[file.pos + i] = None
                    data[space.pos + i] = file.file_id
                space.size -= file.size
                space.pos += file.size
                break

    ans = 0
    for i, c in enumerate(data):
        if c is not None:
            ans += i * c
    return ans


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    2333133121414131402
    """
    assert part_1(input_data) == 1928


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 6395800119709


def test__part2_sample():
    input_data = """
    2333133121414131402
    """
    assert part_2(input_data) == 2858


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 6418529470362
