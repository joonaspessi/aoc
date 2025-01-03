import re

INPUT_FILE = "inputs/2024/day17.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


def parse(input_data):
    registers, program = input_data.strip().split("\n\n")

    a, _, _ = ints(registers)
    program = ints(program)
    return a, program


def solve(a, program, part2=False):
    b = 0
    c = 0
    ip = 0
    out = []

    def combo_op(op):
        if op in [0, 1, 2, 3]:
            return op
        elif op == 4:
            return a
        elif op == 5:
            return b
        elif op == 6:
            return c
        else:
            assert False, f"Unknown op: {op}"

    while True:
        if ip >= len(program):
            break

        cmd = program[ip]
        op = program[ip + 1]
        combo = combo_op(op)

        if cmd == 0:
            a = a // 2**combo
            ip += 2
        elif cmd == 1:
            b = b ^ op
            ip += 2
        elif cmd == 2:
            b = combo % 8
            ip += 2
        elif cmd == 3:
            if a != 0:
                ip = op
            else:
                ip += 2
        elif cmd == 4:
            b = b ^ c
            ip += 2
        elif cmd == 5:
            out.append(int(combo % 8))
            # if part2:
            #     if program[len(out) - 1] != out[len(out) - 1]:
            #         return out
            ip += 2
        elif cmd == 6:
            b = a // 2**combo
            ip += 2
        elif cmd == 7:
            c = a // 2**combo
            ip += 2
    return out


def part_1(input_data: str) -> int:
    a, program = parse(input_data)
    result = solve(a, program)
    result = ",".join(map(str, result))
    return result


def part_2(input_data: str) -> int:
    _, program = parse(input_data)

    a = 0o1  # 0
    a = 0o2  # 1,0
    a = 0o3  # 1,0
    a = 0o4  # 2,1,0
    a = 0o5  # 2,1,0
    a = 0o6  # 3,1,0
    a = 0o7  # 3,1,0

    a = 0o10  # 4,2,1,0
    a = 0o11  # 4,2,1,0
    a = 0o12  # 5,2,1,0

    a = 0o100  # 0,0,0,4,2,1,0
    a = 0o101  # 0,0,0,4,2,1,0
    a = 0o102  # 1,0,0,4,2,1,0

    result = solve(a, program, part2=True)
    result = ",".join(map(str, result))
    return 0


def test__part1_sample():
    input_data = """
    Register A: 729
    Register B: 0
    Register C: 0

    Program: 0,1,5,4,3,0
    """
    assert part_1(input_data) == "4,6,3,5,6,3,5,2,1,0"


def test__part1():
    input_data = read_input(INPUT_FILE)
    assert part_1(input_data) == "1,5,7,4,1,6,0,3,0"


# def test__part2_sample():
#     input_data = """
#     Register A: 729
#     Register B: 0
#     Register C: 0

#     Program: 0,1,5,4,3,0
#     """
#     assert part_2(input_data) == 0


# def test__part2():
#     input_data = read_input(INPUT_FILE)
#     assert part_2(input_data) == 0

if __name__ == "__main__":
    test__part1_sample()
    test__part1()
    test__part2_sample()
    # test__part2()
    # input_data = read_input(INPUT_FILE)
    # print(part_1(input_data))
    # print(part_2(input_data))
