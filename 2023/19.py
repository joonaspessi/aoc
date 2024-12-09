from collections import deque


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


def new_range(op, comp, low, high):
    match op:
        case ">":
            low = max(comp + 1, low)
        case ">=":
            low = max(comp, low)
        case "<":
            high = min(comp - 1, high)
        case "<=":
            high = min(comp, high)
        case _:
            assert False

    return low, high


def new_ranges(
    rating_key, op, comp, x_low, x_high, m_low, m_high, a_low, a_high, s_low, s_high
) -> tuple[int, int, int, int, int, int, int, int]:
    match rating_key:
        case "x":
            x_low, x_high = new_range(op, comp, x_low, x_high)
        case "m":
            m_low, m_high = new_range(op, comp, m_low, m_high)
        case "a":
            a_low, a_high = new_range(op, comp, a_low, a_high)
        case "s":
            s_low, s_high = new_range(op, comp, s_low, s_high)
        case _:
            assert False
    return (x_low, x_high, m_low, m_high, a_low, a_high, s_low, s_high)


def part_2(input_data: str) -> int:
    workflows, ratings = parse(input_data)
    ret_val = 0
    stack = deque([("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
    while stack:
        state, x_low, x_high, m_low, m_high, a_low, a_high, s_low, s_high = stack.pop()
        if x_low > x_high or m_low > m_high or a_low > a_high or s_low > s_high:
            continue
        if state == "A":
            score = (
                (x_high - x_low + 1)
                * (m_high - m_low + 1)
                * (a_high - a_low + 1)
                * (s_high - s_low + 1)
            )
            ret_val += score

        elif state == "R":
            continue
        else:
            rules = workflows[state]
            for rule in rules:
                if ":" in rule:
                    condition, result = rule.split(":")
                    rule = result
                    rating_key = condition[0]
                    op = condition[1]
                    comp = int(condition[2:])
                    stack.append(
                        (
                            rule,
                            *new_ranges(
                                rating_key,
                                op,
                                comp,
                                x_low,
                                x_high,
                                m_low,
                                m_high,
                                a_low,
                                a_high,
                                s_low,
                                s_high,
                            ),
                        )
                    )
                    (
                        x_low,
                        x_high,
                        m_low,
                        m_high,
                        a_low,
                        a_high,
                        s_low,
                        s_high,
                    ) = new_ranges(
                        rating_key,
                        "<=" if op == ">" else ">=",
                        comp,
                        x_low,
                        x_high,
                        m_low,
                        m_high,
                        a_low,
                        a_high,
                        s_low,
                        s_high,
                    )
                else:
                    stack.append(
                        (
                            rule,
                            x_low,
                            x_high,
                            m_low,
                            m_high,
                            a_low,
                            a_high,
                            s_low,
                            s_high,
                        )
                    )

    return ret_val


if __name__ == "__main__":
    input_data = read_input("inputs/2023/day19.txt")
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
    input_data = read_input("inputs/2023/day19.txt")
    assert part_1(input_data) == 446517


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
    assert part_2(input_data) == 167409079868000


def test__part2():
    input_data = read_input("inputs/2023/day19.txt")
    assert part_2(input_data) == 130090458884662
