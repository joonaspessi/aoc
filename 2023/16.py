def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    return [[c for c in line.strip()] for line in input_data.strip().split("\n")]


# up=0 right=1 down=2 left=3
dir_row = [-1, 0, 1, 0]
dir_col = [0, 1, 0, -1]


def move(row, col, dir):
    return (row + dir_row[dir], col + dir_col[dir], dir)


def solve(grid, row, col, dir):
    len_row = len(grid)
    len_col = len(grid[0])
    pos = [(row, col, dir)]
    seen = set()
    seen_dir = set()

    while True:
        new_pos = []
        if not pos:
            break
        for r, c, d in pos:
            if 0 <= r < len_row and 0 <= c < len_col:
                seen.add((r, c))
                if (r, c, d) in seen_dir:
                    continue
                seen_dir.add((r, c, d))

                # up=0 right=1 down=2 left=3
                match grid[r][c]:
                    case ".":
                        new_pos.append(move(r, c, d))
                    case "/":
                        match d:
                            case 0:
                                new_pos.append(move(r, c, 1))
                            case 1:
                                new_pos.append(move(r, c, 0))
                            case 2:
                                new_pos.append(move(r, c, 3))
                            case 3:
                                new_pos.append(move(r, c, 2))
                    case "\\":
                        match d:
                            case 0:
                                new_pos.append(move(r, c, 3))
                            case 1:
                                new_pos.append(move(r, c, 2))
                            case 2:
                                new_pos.append(move(r, c, 1))
                            case 3:
                                new_pos.append(move(r, c, 0))
                    case "|":
                        match d:
                            case 0 | 2:
                                new_pos.append(move(r, c, d))
                            case 1 | 3:
                                new_pos.append(move(r, c, 0))
                                new_pos.append(move(r, c, 2))
                    case "-":
                        match d:
                            case 1 | 3:
                                new_pos.append(move(r, c, d))
                            case 0 | 2:
                                new_pos.append(move(r, c, 1))
                                new_pos.append(move(r, c, 3))
                    case _:
                        assert False
        pos = new_pos
    return len(seen)


def part_1(input_data: str) -> int:
    grid = parse(input_data)
    return solve(grid, 0, 0, 1)


def part_2(input_data: str) -> int:
    grid = parse(input_data)
    len_row = len(grid)
    len_col = len(grid[0])

    ret_val = 0
    for r in range(len_row):
        ret_val = max(ret_val, solve(grid, r, 0, 1))
        ret_val = max(ret_val, solve(grid, r, len_col - 1, 3))

    for c in range(len_col):
        ret_val = max(ret_val, solve(grid, 0, c, 2))
        ret_val = max(ret_val, solve(grid, len_row - 1, c, 0))

    return ret_val


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day16.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1():
    input_data = read_input("inputs/2023/day16.txt")
    assert part_1(input_data) == 7392


def test__part2():
    input_data = read_input("inputs/2023/day16.txt")
    assert part_2(input_data) == 7665
