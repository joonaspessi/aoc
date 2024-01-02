def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return [c for c in input_data.strip().split(",")]


def calc_hash(seq: str) -> int:
    curr = 0
    for c in seq:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr


def part_1(input_data: str) -> int:
    sequences = parse(input_data)
    hashes = []
    for s in sequences:
        hashes.append(calc_hash(s))

    return sum(hashes)


def part_2(input_data: str) -> int:
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day15.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    """
    assert part_1(input_data) == 1320


def test__part1():
    input_data = read_input("inputs/day15.txt")
    assert part_1(input_data) == 504449


def test__part2_sample():
    input_data = """
    xxx
    """
    assert part_2(input_data) == 0


def test__part2():
    input_data = read_input("inputs/day15.txt")
    assert part_2(input_data) == 0
