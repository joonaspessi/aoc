from math import lcm


class TreeNode:
    def __init__(self, name, right=None, left=None):
        self.name = name
        self.right = right
        self.left = left


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str, part_2=False):
    command_data, tree_data = input_data.split("\n\n")
    commands = [c for c in command_data.strip()]
    lines = [
        line.replace("(", "").replace(")", "").replace(",", "").strip()
        for line in tree_data.strip().split("\n")
    ]
    nodes = {}
    nodes_children = {}
    for line in lines:
        name, c = line.split(" = ")
        children = c.split()
        nodes[name] = TreeNode(name)
        nodes_children[name] = children

    for name, children in nodes_children.items():
        nodes[name].left = nodes[children[0]]
        nodes[name].right = nodes[children[1]]

    if part_2:
        start_nodes = [node for node in nodes.values() if node.name[2] == "A"]
    else:
        start_nodes = [nodes["AAA"]]
    return commands, start_nodes


def dfs_r2(roots, commands):
    stack = [roots]
    ans = 0

    while stack:
        print(ans)
        nodes = stack.pop()
        if all([node.name[2] == "Z" for node in nodes]):
            return ans
        next_c = commands[ans % len(commands)]
        ans += 1
        next_nodes = []
        for node in nodes:
            if next_c == "L":
                next_nodes.append(node.left)
            else:
                next_nodes.append(node.right)
        stack.append(next_nodes)

    assert False, "Should not reach here"


def part_1(input_data: str) -> int:
    command, root = parse(input_data)
    return dfs_r2(root, command)


def part_2(input_data: str) -> int:
    command, roots = parse(input_data, part_2=True)

    values = [dfs_r2([root], command) for root in roots]
    return lcm(*values)


if __name__ == "__main__":
    input_data = read_input("inputs/day8.txt")
    print(f"part1: {part_1(input_data)}")
    print(f"part2: {part_2(input_data)}")


def test__part1_sample1():
    input_data = """
    RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)
    """
    assert part_1(input_data) == 2


def test__part1_sample2():
    input_data = """
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    """
    assert part_1(input_data) == 6


def test__part1():
    input_data = read_input("inputs/day8.txt")
    assert part_1(input_data) == 21409


def test__part2_sample1():
    input_data = """
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """
    assert part_2(input_data) == 6
