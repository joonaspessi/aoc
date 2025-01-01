from collections import deque


INPUT_FILE = "inputs/2024/day15.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data, part2=False):
    grid, ins = input_data.strip().split("\n\n")

    rows = []
    for line in grid.strip().split("\n"):
        i = []
        for c in list(line.strip()):
            if c == "@":
                i.append("@")
                i.append(".")
            elif c == "O":
                i.append("[")
                i.append("]")
            elif c == "#":
                i.append("#")
                i.append("#")
            elif c == ".":
                i.append(".")
                i.append(".")
        rows.append(i)

    instructions = list(ins.strip().replace("\n", ""))
    return rows, instructions


def part_1(input_data: str) -> int:
    grid, ins = parse(input_data)
    r_len = len(grid)
    c_len = len(grid[0])

    for r in range(r_len):
        for c in range(c_len):
            if grid[r][c] == "@":
                sr, sc = (r, c)
                grid[r][c] = "."

    r, c = sr, sc
    for i in ins:
        if i == "^":
            dr, dc = (-1, 0)
        elif i == "v":
            dr, dc = (1, 0)
        elif i == "<":
            dr, dc = (0, -1)
        elif i == ">":
            dr, dc = (0, 1)

        # next position
        rr, cc = r + dr, c + dc

        if grid[rr][cc] == "#":
            continue
        elif grid[rr][cc] == ".":
            r, c = rr, cc
        elif grid[rr][cc] == "O":
            q = deque([(r, c)])
            seen = set()
            valid = True
            while q:
                rr, cc = q.popleft()
                if (rr, cc) in seen:
                    continue
                seen.add((rr, cc))
                rrr, ccc = rr + dr, cc + dc

                if grid[rrr][ccc] == "#":
                    valid = False
                    break
                elif grid[rrr][ccc] == "O":
                    q.append((rrr, ccc))
            if not valid:
                continue
            while len(seen) > 0:
                for rr, cc in sorted(seen):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in seen:
                        grid[rrr][ccc] = grid[rr][cc]
                        grid[rr][cc] = "."
                        seen.remove((rr, cc))

            r = r + dr
            c = c + dc

    result = 0
    for r in range(r_len):
        for c in range(c_len):
            if grid[r][c] == "O":
                result += 100 * r + c
    return result


def part_2(input_data: str) -> int:
    grid, ins = parse(input_data, part2=True)
    r_len = len(grid)
    c_len = len(grid[0])

    for r in range(r_len):
        for c in range(c_len):
            if grid[r][c] == "@":
                sr, sc = (r, c)
                grid[r][c] = "."

    r, c = sr, sc
    for i in ins:
        if i == "^":
            dr, dc = (-1, 0)
        elif i == "v":
            dr, dc = (1, 0)
        elif i == "<":
            dr, dc = (0, -1)
        elif i == ">":
            dr, dc = (0, 1)

        # next position
        rr, cc = r + dr, c + dc

        if grid[rr][cc] == "#":
            continue
        elif grid[rr][cc] == ".":
            r, c = rr, cc
        elif grid[rr][cc] in ["[", "]"]:
            q = deque([(r, c)])
            seen = set()
            valid = True
            while q:
                rr, cc = q.popleft()
                if (rr, cc) in seen:
                    continue
                seen.add((rr, cc))
                rrr, ccc = rr + dr, cc + dc

                if grid[rrr][ccc] == "#":
                    valid = False
                    break
                elif grid[rrr][ccc] == "[":
                    q.append((rrr, ccc))
                    q.append((rrr, ccc + 1))
                elif grid[rrr][ccc] == "]":
                    q.append((rrr, ccc))
                    q.append((rrr, ccc - 1))
            if not valid:
                continue
            while len(seen) > 0:
                for rr, cc in sorted(seen):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in seen:
                        grid[rrr][ccc] = grid[rr][cc]
                        grid[rr][cc] = "."
                        seen.remove((rr, cc))

            r = r + dr
            c = c + dc
    # print
    for row in grid:
        print("".join(row))
    result = 0
    for r in range(r_len):
        for c in range(c_len):
            if grid[r][c] == "[":
                result += 100 * r + c
    return result


def test__part1_sample():
    input_data = """
    ########
    #..O.O.#
    ##@.O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########

    <^^>>>vv<v>>v<<
    """
    assert part_1(input_data) == 2028


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == 0


def test__part2_sample():
    input_data = """
    #######
    #...#.#
    #.....#
    #..OO@#
    #..O..#
    #.....#
    #######

    <vv<<^^<<^^
    """
    assert part_2(input_data) == 618


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 1432781


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
