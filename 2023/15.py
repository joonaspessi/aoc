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
    sequences = parse(input_data)
    boxes = {}
    for s in sequences:
        if s[-1] == "-":
            k = s[:-1]
            h = calc_hash(k)
            if h in boxes:
                boxes[h] = [b for b in boxes[h] if b[0] != k]
        else:
            i = s.index("=")
            k = s[:i]
            h = calc_hash(k)
            v = int(s[(i + 1) :])
            if h not in boxes:
                boxes[h] = []
            if any([k == kk for (kk, _) in boxes[h]]):
                boxes[h] = [(k, v) if kk == k else (kk, vv) for (kk, vv) in boxes[h]]
            else:
                boxes[h].append((k, v))

    answer = 0
    for box, slots in boxes.items():
        for i, (_, fl) in enumerate(slots):
            answer += (box + 1) * (i + 1) * (fl)
            pass

    return answer


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day15.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    """
    assert part_1(input_data) == 1320


def test__part1():
    input_data = read_input("inputs/2023/day15.txt")
    assert part_1(input_data) == 504449


def test__part2_sample():
    input_data = """
    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
    """
    assert part_2(input_data) == 145


def test__part2():
    input_data = read_input("inputs/2023/day15.txt")
    assert part_2(input_data) == 262044
