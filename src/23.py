from collections import deque

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
slopes = dict(zip("^>v<", directions))


class Graph:
    def __init__(self, graph, start, end):
        self.nodes = {}
        for k, v in graph.items():
            if v == ".":
                self.nodes[k] = Node(k)
            if v in slopes:
                self.nodes[k] = Node(k, direction=slopes[v])
        self.start = self.nodes[start]
        self.end = self.nodes[end]

        for k, v in self.nodes.items():
            for d in directions:
                y = k[0] + d[0]
                x = k[1] + d[1]
                if (y, x) in self.nodes and self.nodes[(y, x)].direction in (None, d):
                    v.edges[self.nodes[(y, x)]] = 1

    def solve(self):
        ans = 0
        s = deque([(self.start, 0, [])])

        while s:
            n, dist, seen = s.popleft()
            if n == self.end:
                ans = max(ans, dist)
            for e in n.edges:
                if e not in seen:
                    s.append((e, dist + 1, seen + [e]))
        return ans


class Node:
    def __init__(self, pos, direction=None):
        self.pos = pos
        self.edges = {}
        self.direction = direction


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    lines = [line.strip() for line in input_data.strip().splitlines()]

    grid = {}
    start = None
    end = None

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(y, x)] = c
            if y == 0 and c == ".":
                start = (y, x)
            if y == len(lines) - 1 and c == ".":
                end = (y, x)
    return grid, start, end


def part_1(input_data: str) -> int:
    grid, start, end = parse(input_data)
    graph = Graph(graph=grid, start=start, end=end)
    return graph.solve()


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day23.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    #.#####################
    #.......#########...###
    #######.#########.#.###
    ###.....#.>.>.###.#.###
    ###v#####.#v#.###.#.###
    ###.>...#.#.#.....#...#
    ###v###.#.#.#########.#
    ###...#.#.#.......#...#
    #####.#.#.#######.#.###
    #.....#.#.#.......#...#
    #.#####.#.#.#########v#
    #.#...#...#...###...>.#
    #.#.#v#######v###.###v#
    #...#.>.#...>.>.#.###.#
    #####v#.#.###v#.#.###.#
    #.....#...#...#.#.#...#
    #.#########.###.#.#.###
    #...###...#...#...#.###
    ###.###.#.###v#####v###
    #...#...#.#.>.>.#.>.###
    #.###.###.#.###.#.#v###
    #.....###...###...#...#
    #####################.#
    """
    assert part_1(input_data) == 94


def test__part1():
    input_data = read_input("inputs/day23.txt")
    assert part_1(input_data) == 2086


def test__part2_sample():
    input_data = """
    xxx
    """
    assert part_2(input_data) == 0


def test__part2():
    input_data = read_input("inputs/day23.txt")
    assert part_2(input_data) == 0
