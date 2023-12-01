def read_file(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return [line.strip() for line in data]


def part_1(lines):
    numbers = []
    for line in lines:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                first = c
                break
        for c in reversed(line):
            if c.isdigit():
                last = c
                break
        assert first is not None
        assert last is not None
        total = int(f"{first}{last}")
        numbers.append(total)
    return sum(numbers)


def part_2(lines):
    numbers = []
    for line in lines:
        first = None
        last = None
        c = 0
        while c < len(line):
            if line[c].isdigit():
                first = line[c]
                break
            if line[c:].startswith("one"):
                first = 1
                break
            if line[c:].startswith("two"):
                first = 2
                break
            if line[c:].startswith("three"):
                first = 3
                break
            if line[c:].startswith("four"):
                first = 4
                break
            if line[c:].startswith("five"):
                first = 5
                break
            if line[c:].startswith("six"):
                first = 6
                break
            if line[c:].startswith("seven"):
                first = 7
                break
            if line[c:].startswith("eight"):
                first = 8
                break
            if line[c:].startswith("nine"):
                first = 9
                break
            c += 1

        line = line[::-1]
        c = 0
        while c < len(line):
            if line[c].isdigit():
                last = line[c]
                break
            if line[c:].startswith("one"[::-1]):
                last = 1
                break
            if line[c:].startswith("two"[::-1]):
                last = 2
                break
            if line[c:].startswith("three"[::-1]):
                last = 3
                break
            if line[c:].startswith("four"[::-1]):
                last = 4
                break
            if line[c:].startswith("five"[::-1]):
                last = 5
                break
            if line[c:].startswith("six"[::-1]):
                last = 6
                break
            if line[c:].startswith("seven"[::-1]):
                last = 7
                break
            if line[c:].startswith("eight"[::-1]):
                last = 8
                break
            if line[c:].startswith("nine"[::-1]):
                last = 9
                break
            c += 1

        assert first is not None and last is not None
        total = int(f"{first}{last}")
        numbers.append(total)
    return sum(numbers)


lines = read_file("inputs/day1.txt")

print(f"part 1: {part_1(lines)}")
print(f"part 2: {part_2(lines)}")


def test__part1():
    lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert part_1(lines) == 142


def test__part2():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert part_2(lines) == 281
