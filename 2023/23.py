from collections import deque

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
slopes = dict(zip("^>v<", directions))


class Graph:
    def __init__(self, graph, start, end, part_2=False):
        self.nodes = {}
        for k, v in graph.items():
            if v == ".":
                self.nodes[k] = Node(k)
            if v in slopes:
                if part_2:
                    self.nodes[k] = Node(k, direction=None)
                else:
                    self.nodes[k] = Node(k, direction=slopes[v])
        self.start = self.nodes[start]
        self.end = self.nodes[end]

        for k, v in self.nodes.items():
            for d in directions:
                y = k[0] + d[0]
                x = k[1] + d[1]
                if (y, x) in self.nodes and self.nodes[(y, x)].direction in (None, d):
                    v.edges[self.nodes[(y, x)]] = 1
        self.compress()

    def solve(self):
        ans = 0
        s = deque([(self.start, 0, [])])

        while s:
            n, dist, seen = s.popleft()
            if n == self.end:
                ans = max(ans, dist)
            for e, length in n.edges.items():
                if e not in seen:
                    s.append((e, dist + length, seen + [e]))
        return ans

    def compress(self):
        remove = []
        for pos, node in self.nodes.items():
            if node.direction is not None:
                continue
            if len(node.edges) == 2 and not any(edge.direction for edge in node.edges):
                n1, n2 = node.edges.keys()
                del n1.edges[node]
                del n2.edges[node]
                n1.edges[n2] = sum(node.edges.values())
                n2.edges[n1] = sum(node.edges.values())
                remove.append(pos)

        while remove:
            k = remove.pop()
            del self.nodes[k]


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
    grid, start, end = parse(input_data)
    graph = Graph(graph=grid, start=start, end=end, part_2=True)
    return graph.solve()


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day23.txt")
    print(part_1(input_data))
    print(part_2(input_data))

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


def test__part1_sample():
    assert part_1(input_data) == 94


def test__part1():
    input_data = read_input("inputs/2023/day23.txt")
    assert part_1(input_data) == 2086


def test__part2_sample():
    assert part_2(input_data) == 154


def test__part2():
    input_data = read_input("inputs/2023/day23.txt")
    assert part_2(input_data) == 6526
