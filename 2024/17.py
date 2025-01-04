from collections import deque
import re

INPUT_FILE = "inputs/2024/day17.txt"


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def ints(s):
    return [int(x) for x in re.findall(r"-?\d+", s)]


def parse(input_data):
    registers, program = input_data.strip().split("\n\n")

    a, _, _ = ints(registers)
    program = ints(program)
    return a, program


def solve(a, program):
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


def decompiled(a):
    # 2,4,
    b = a & 7

    # 1,3,
    b = b ^ 3

    # 7,5,
    c = a >> b

    # 4,0,
    b = b ^ c

    # 1,3,
    b = b ^ 3

    # 0,3,
    a = a >> 3

    # 5,5,
    out = b & 7

    # 3,0
    return (a, out)


def part_2(input_data: str) -> int:
    _, program = parse(input_data)

    pending = deque([(len(program), 0)])
    valid_values = []

    while pending:
        index, expected_output = pending.popleft()

        if index == 0:
            valid_values.append(expected_output)
            continue

        next_index = index - 1
        instruction = program[next_index]

        for i in range(8):
            next_value = (expected_output << 3) | i
            output, instruction_output = decompiled(next_value)
            if instruction_output == instruction and output == expected_output:
                pending.append((next_index, next_value))

    for v in valid_values:
        result = solve(v, program)
        if program == result:
            return v


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


def test__part2():
    input_data = read_input(INPUT_FILE)
    assert part_2(input_data) == 108107574778365


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)
    print(part_1(input_data))
    print(part_2(input_data))
