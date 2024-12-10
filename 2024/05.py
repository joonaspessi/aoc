from collections import defaultdict, deque

INPUT_FILE = "inputs/2024/day5.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    input_data = input_data.strip().split("\n\n")

    upstream_rules = defaultdict(set)
    downstream_rules = defaultdict(set)
    for rule in input_data[0].split("\n"):
        rule = rule.strip().split("|")
        i = int(rule[0])
        j = int(rule[1])
        upstream_rules[j].add(i)
        downstream_rules[i].add(j)

    updates = []
    for update in input_data[1].split("\n"):
        update = update.strip().split(",")
        updates.append([int(x) for x in update])
    return upstream_rules, downstream_rules, updates


def part_1(input_data: str) -> int:
    upstream_rules, _, updates = parse(input_data)
    result = 0
    for update in updates:
        order_ok = True
        for i, u in enumerate(update):
            for j, v in enumerate(update):
                if i < j and v in upstream_rules[u]:
                    order_ok = False

        if order_ok:
            result += update[len(update) // 2]

    return result


# Kahn algorithm
# L ← Empty list that will contain the sorted elements
# S ← Set of all nodes with no incoming edge

# while S is not empty do
#     remove a node n from S
#     add n to L
#     for each node m with an edge e from n to m do
#         remove edge e from the graph
#         if m has no other incoming edges then
#             insert m into S


# if graph has edges then
#     return error   (graph has at least one cycle)
# else
#     return L   (a topologically sorted order)


def part_2(input_data: str) -> int:
    upstream_rules, downsteam_rules, updates = parse(input_data)
    result = 0
    for update in updates:
        order_ok = True
        for i, u in enumerate(update):
            for j, v in enumerate(update):
                if i < j and v in upstream_rules[u]:
                    order_ok = False

        if not order_ok:
            L = []
            S = deque([])
            # D is a dictionary that keeps track of the number of incoming edges to each node
            D = {node: len(upstream_rules[node] & set(update)) for node in update}

            # Populate Set of all nodes with no incoming edge to start the algorithm
            for n in update:
                if D[n] == 0:
                    S.append(n)
            while S:
                n = S.popleft()
                L.append(n)
                # each node m with an edge e from n to m
                for m in downsteam_rules[n]:
                    if m in D:
                        D[m] -= 1
                        if D[m] == 0:
                            S.append(m)

            result += L[len(L) // 2]

    return result


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


def test__part2_sample():
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
    assert part_2(input_data) == 123


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 5448
