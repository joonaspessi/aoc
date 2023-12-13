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

    return commands, nodes["AAA"]


def dfs_r(root, commands):
    stack = [root]
    ans = 0

    while stack:
        node = stack.pop()
        if node.name == "ZZZ":
            return ans
        next_c = commands[ans % len(commands)]
        ans += 1
        if next_c == "L":
            stack.append(node.left)
        else:
            stack.append(node.right)

    assert False, "Should not reach here"


def part_1(input_data: str) -> int:
    command, root = parse(input_data)
    return dfs_r(root, command)


def part_2(input_data: str) -> int:
    return 0


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
