from collections import defaultdict

INPUT_FILE = "inputs/2024/day5.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    input_data = input_data.strip().split("\n\n")

    ordering_rules = defaultdict(set)
    for rule in input_data[0].split("\n"):
        rule = rule.strip().split("|")
        i = int(rule[0])
        j = int(rule[1])
        ordering_rules[j].add(i)

    updates = []
    for update in input_data[1].split("\n"):
        update = update.strip().split(",")
        updates.append([int(x) for x in update])
    return ordering_rules, updates


def part_1(input_data: str) -> int:
    ordering_rules, updates = parse(input_data)
    result = 0
    for update in updates:
        order_ok = True
        for i, u in enumerate(update):
            for j, v in enumerate(update):
                if i < j and v in ordering_rules[u]:
                    order_ok = False

        if order_ok:
            result += update[len(update) // 2]

    return result


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """
    assert part_1(input_data) == 143


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 4814


# def test__part2_sample():
#     input_data = """
#     xxx
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0
