from collections import defaultdict
from typing import DefaultDict, Tuple


def read_input(name: str) -> str:
    with open(name) as f:
        data = f.read()
    return data.strip()


def parse(input_data: str) -> list[Tuple[int, list[int], list[int]]]:
    input_data = input_data.strip()
    lines = [line.strip() for line in input_data.split("\n")]
    scratch_cards = []
    for line in lines:
        card = int(line.split(":")[0].split()[1])
        line = line.split(":")[1].split("|")
        winning_numbers = [int(n) for n in line[0].strip().split()]
        player_numbers = [int(n) for n in line[1].strip().split()]
        winning_numbers.sort()
        player_numbers.sort()
        scratch_cards.append((card, winning_numbers, player_numbers))
    return scratch_cards


def part_1(input_data: str) -> int:
    cards = parse(input_data)
    count = 0
    for _, winning_numbers, player_numbers in cards:
        round_score = sum(1 for num in player_numbers if num in winning_numbers)
        if round_score < 2:
            count += round_score
        else:
            count += 2 ** (round_score - 1)
    return count


def part_2(input_data: str) -> int:
    cards = parse(input_data)
    card_wins: DefaultDict[int, int] = defaultdict(int)
    for card_number, winning_numbers, player_numbers in cards:
        round_score = sum(1 for num in player_numbers if num in winning_numbers)
        multiplier = card_wins[card_number]
        card_wins[card_number] += 1
        for i in range(card_number + 1, card_number + round_score + 1):
            card_wins[i] += 1 + multiplier

    return sum(card_wins.values())


if __name__ == "__main__":
    input_data = read_input("inputs/day4.txt")
    print(part_1(input_data))
    print(part_2(input_data))


def test__part1_sample():
    sample = """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """

    assert part_1(sample) == 13


def test__part1():
    input_data = read_input("inputs/day4.txt")
    assert part_1(input_data) == 21959


def test__part2_sample():
    sample = """
    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    """

    assert part_2(sample) == 30


def test__part2():
    input_data = read_input("inputs/day4.txt")
    assert part_2(input_data) == 5132675
