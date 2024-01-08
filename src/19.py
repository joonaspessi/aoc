from dataclasses import dataclass


@dataclass
class Rule:
    key: str
    operator: str
    operand: int
    next: str


@dataclass
class Workflow:
    name: str
    rules: list[Rule]


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data):
    workflows_data, ratings_data = input_data.strip().split("\n\n")

    workflows = {}
    for workflow in workflows_data.strip().split("\n"):
        name, r = workflow.strip().split("{")
        r = r[:-1]
        workflows[name] = r.split(",")

    ratings = []
    for rating in ratings_data.strip().split("\n"):
        rating = rating.strip()[1:-1]
        rating = {
            rating.split("=")[0]: int(rating.split("=")[1])
            for rating in rating.split(",")
        }
        ratings.append(rating)

    return workflows, ratings


def solve(workflows, rating):
    state = "in"
    while True:
        workflow = workflows[state]
        for rule in workflow:
            rule_ok = True
            if ":" in rule:
                condition, result = rule.split(":")
                rule = result
                rating_key = condition[0]
                op = condition[1]
                comp = int(condition[2:])
                match op:
                    case ">":
                        rule_ok = rating[rating_key] > comp
                    case "<":
                        rule_ok = rating[rating_key] < comp
            if rule_ok:
                if rule == "A":
                    return True
                if rule == "R":
                    return False
                state = rule
                break


def part_1(input_data: str) -> int:
    workflows, ratings = parse(input_data)
    ret_val = 0
    for rating in ratings:
        if solve(workflows, rating):
            ret_val += sum([value for value in rating.values()])
    return ret_val


def part_2(input_data: str) -> int:
    data = parse(input_data)  # noqa
    return 0


if __name__ == "__main__":
    input_data = read_input("inputs/day19.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    input_data = """
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}

    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}
    """
    assert part_1(input_data) == 19114


def test__part1():
    input_data = read_input("inputs/day19.txt")
    assert part_1(input_data) == 0


def test__part2_sample():
    input_data = """
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}

    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}
    """
    assert part_2(input_data) == 0


def test__part2():
    input_data = read_input("inputs/day19.txt")
    assert part_2(input_data) == 0
