def read_file(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return [line.strip() for line in data]


def part_1(lines):
    numbers = []
    for line in lines:
        line_sum = []
        for c in line:
            if c.isdigit():
                line_sum.append(c)
        total = int(line_sum[0] + line_sum[-1])
        numbers.append(total)
    return sum(numbers)


def part_2(lines):
    total = 0
    for line in lines:
        line_sum = []
        for i, c in enumerate(line):
            if c.isdigit():
                line_sum.append(c)

            for d, val in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if line[i:].startswith(val):
                    line_sum.append(str(d + 1))

        line_score = int(line_sum[0] + line_sum[-1])
        total += line_score
    return total


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
