def read_file(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return [line.strip() for line in data]


def parse_game(game):
    game = game.split(":")[1].strip()
    cubes = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    rounds = [game.strip() for game in game.split(";")]
    for i, round in enumerate(rounds):
        g2 = [g.strip() for g in round.split(",")]
        g3 = [g3.split(" ") for g3 in g2]
        for g4 in g3:
            if cubes[g4[1]] < int(g4[0]):
                cubes[g4[1]] = int(g4[0])
    return cubes


def part_1(lines, draws):
    result = 0
    for i, line in enumerate(lines):
        game = parse_game(line)
        if all(game[color] <= draws[color] for color in draws):
            result += i + 1

    return result


def part_2(lines):
    result = 0
    for line in lines:
        game = parse_game(line)
        cube_power = 1
        for value in game.values():
            cube_power *= value
        result += cube_power
    return result


def main():
    lines = read_file("inputs/2023/day2.txt")
    draws = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    print(f"part 1: {part_1(lines, draws)}")
    print(f"part 2: {part_2(lines)}")


if __name__ == "__main__":
    main()


def test__part1():
    lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    draws = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    assert part_1(lines, draws) == 8


def test__part2():
    lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert part_2(lines) == 2286
