import dataclasses
from collections import deque


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


@dataclasses.dataclass
class FlipFlop:
    name: str
    state = False
    outputs: list = dataclasses.field(default_factory=lambda: [])
    inputs: list = dataclasses.field(default_factory=lambda: [])

    def compute(self, pulse: bool):
        if not pulse:
            self.state = not self.state
            return self.state
        else:
            None


@dataclasses.dataclass
class Conjunction:
    name: str
    mem = False
    state = False
    outputs: list = dataclasses.field(default_factory=lambda: [])
    inputs: list = dataclasses.field(default_factory=lambda: [])

    def compute(self, pulse: bool):
        if all([i.state for i in self.inputs]):
            self.state = False
        else:
            self.state = True
        return self.state


@dataclasses.dataclass
class Broadcaster:
    name: str
    outputs: list = dataclasses.field(default_factory=lambda: [])
    inputs: list = dataclasses.field(default_factory=lambda: [])
    state = False

    def compute(self, pulse: bool):
        return pulse


def parse(input_data):
    data = [d.strip().split(" -> ") for d in input_data.strip().split("\n")]
    tree = {}
    conjunction_parents = []
    for d in data:
        module, connections = d
        if module[0] == "%":
            m = FlipFlop(name=module[1:])
        elif module[0] == "&":
            m = Conjunction(name=module[1:])
        else:
            m = Broadcaster(name=module)

        connections = connections.split(", ")
        m.outputs = connections
        tree[m.name] = m

    for m in tree.values():
        for mm in tree.values():
            if m.name in mm.outputs and m.name != mm.name:
                m.inputs.append(mm)

    return tree


def part_1(input_data: str) -> int:
    modules = parse(input_data)

    current = "broadcast"
    low_count = 0
    high_count = 0

    for _ in range(1000):
        stack = deque()
        stack.append(modules["broadcaster"])
        low_count += 1
        while stack:
            m = stack.popleft()
            for om in m.outputs:
                # print(f"{m.name} -{'high' if m.state else 'low'}-> {om}")
                low_count += 1 if not m.state else 0
                high_count += 1 if m.state else 0
                if om not in modules:
                    continue
                om = modules[om]
                out = om.compute(m.state)
                if out is not None:
                    stack.append(om)

    return low_count * high_count


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day20.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test_conjunction():
    c = Conjunction(name="foo")

    out = c.compute(True)
    assert out == False
    assert c.state == False

    out = c.compute(False)
    assert out == True
    assert c.state == True


def test__part1_sample():
    input_data = """
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """
    assert part_1(input_data) == 32000000


def test__part1_sample2():
    input_data2 = """
    broadcaster -> a
    %a -> inv, con
    &inv -> b
    %b -> con
    &con -> output
    """

    assert part_1(input_data2) == 11687500


def test__part1():
    input_data = read_input("inputs/day20.txt")
    assert part_1(input_data) == 0


def test__part2_sample():
    input_data = """
    xxx
    """
    assert part_2(input_data) == 0


def test__part2():
    input_data = read_input("inputs/day20.txt")
    assert part_2(input_data) == 0
