from collections import defaultdict


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.parent = {n: None for n in self.graph}

    def bfs(self, s, t):
        self.parent = {n: None for n in self.graph}
        self.parent[s] = s

        stack = [s]

        while stack:
            n = stack.pop(0)
            for e, c in self.graph[n].items():
                if c > 0 and self.parent[e] is None:
                    self.parent[e] = n
                    stack.append(e)
        return self.parent[t] is not None

    def min_cut(self, s, t):
        for v, e in self.graph.items():
            for k in e:
                self.graph[v][k] = 1

        max_flow = 0
        while self.bfs(s, t):
            flow = float("inf")
            n = t
            while n != s:
                flow = min(flow, self.graph[self.parent[n]][n])
                n = self.parent[n]

            max_flow += flow

            v = t

            while v != s:
                u = self.parent[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = u

        return max_flow

    def solve(self) -> int:
        g1 = len({n for n, p in self.parent.items() if p})
        return (len(self.graph) - g1) * g1


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    data = defaultdict(dict)

    lines = [line.strip() for line in input_data.strip().splitlines()]
    for line in lines:
        left, right = line.split(": ")
        for r in right.split():
            data[left][r] = 1
            data[r][left] = 1

    return data


def part_1(input_data: str) -> int:
    data = parse(input_data)  # noqa
    graph = Graph(data)
    s, *other = graph.graph
    for t in other:
        if graph.min_cut(s, t) == 3:
            break
    return graph.solve()


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day25.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    jqt: rhn xhk nvd
    rsh: frs pzl lsr
    xhk: hfx
    cmg: qnr nvd lhk bvb
    rhn: xhk bvb hfx
    bvb: xhk hfx
    pzl: lsr hfx nvd
    qnr: nvd
    ntq: jqt hfx bvb xhk
    nvd: lhk
    lsr: lhk
    rzs: qnr cmg lsr rsh
    frs: qnr lhk lsr
    """
    assert part_1(input_data) == 54


def test__part1():
    input_data = read_input("inputs/day25.txt")
    assert part_1(input_data) == 538368
